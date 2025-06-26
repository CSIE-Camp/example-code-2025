import os
import re
import json
from io import BytesIO

import vertexai
from vertexai.generative_models import GenerativeModel, Part, GenerationConfig
from vertexai.preview.vision_models import ImageGenerationModel

import functions_framework
from flask import jsonify
from google.cloud import language_v2, storage
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# --- 全域設定 ---
import google.auth

# 取得 GCP 預設 project_id
_, default_project = google.auth.default()

PROJECT_ID = os.getenv("GCP_PROJECT", default_project)
LOCATION = os.getenv("GCP_LOCATION", "us-central1")
BUCKET_NAME = os.getenv("GCP_BUCKET", "csiecamp-mbti-pictures")


# 初始化 Vertex AI 和其他 GCP 用戶端
vertexai.init(project=PROJECT_ID, location=LOCATION)
language_client = language_v2.LanguageServiceClient()
storage_client = storage.Client()

@functions_framework.http
def mbti_analyzer(request):
    """ 
    接收對話和暱稱，使用 Gemini 進行分析與圖像提示詞生成，
    再使用 Imagen 進行圖像生成。
    """
    headers = {
        "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Methods": "POST",
        "Access-Control-Allow-Headers": "Content-Type",
    }
    if request.method == "OPTIONS": return "", 204, headers
    if request.method != "POST": return "僅接受 POST 請求", 405, headers

    request_json = request.get_json(silent=True)
    if not request_json or "text" not in request_json or "user_name" not in request_json:
        return jsonify({"error": "請求中缺少文字內容或使用者暱稱"}), 400, headers

    raw_text = request_json["text"]
    user_name = request_json["user_name"]
    
    cleaned_log = clean_chat_log(raw_text)
    if not cleaned_log:
        return jsonify({"error": "清理後無有效對話內容"}), 400, headers

    try:
        gemini_result = analyze_and_create_image_prompt(cleaned_log, user_name)
        image_prompt_for_imagen = gemini_result.get("image_prompt", "A cute, abstract character representing a creative personality.")

        image_buffer = generate_image_with_imagen(image_prompt_for_imagen)
        avatar_url = upload_to_gcs(image_buffer, f"mbti-character-{user_name}-{os.urandom(4).hex()}.png")
        
        keywords = analyze_text_entities(cleaned_log, user_name)
        wordcloud_url = generate_and_upload_wordcloud(keywords, user_name)

        final_response = {
            "mbtiResult": gemini_result,
            "wordcloudUrl": wordcloud_url,
            "avatarUrl": avatar_url,
        }
        return jsonify(final_response), 200, headers

    except Exception as e:
        import traceback
        print(f"發生嚴重錯誤: {e}")
        traceback.print_exc()
        return jsonify({"error": f"後端分析服務發生錯誤: {e}"}), 500, headers

def analyze_and_create_image_prompt(full_log: str, user_name: str) -> dict:
    """
    使用新版 SDK (GenerativeModel) 進行分析，並生成專屬的 AI 繪圖提示詞。
    """
    model = GenerativeModel("gemini-2.0-flash")

    prompt = f"""
    ROLE: 你是一位結合了心理學專業與圖像生成詠唱專家(Prompt Engineer)的AI。
    PRIMARY TASK: 請依據下方提供的對話紀錄，針對使用者「{user_name}」，完成兩項任務。
    ---
    任務一：性格分析
    1.  根據「{user_name}」在對話中的發言、語氣和互動模式，推斷出其最可能的 MBTI 人格類型。
    2.  從對話中找出 3 個最關鍵的證據來支持你的判斷。
    3.  用溫暖且鼓勵的中文語氣，給予「{user_name}」一句個人化建議。

    任務二：提示詞生成代表圖像
    Based on the inferred MBTI personality, create a creative, descriptive, and imaginative prompt in English for an AI image generator.
    - **Primary Style**: The main style must be 'a cute, blocky, 3D voxel character, similar to Minecraft or Crossy Road style, cinematic lighting, simple colored background'.
    - **Character Details**: Describe the character's appearance, clothing, and a key item they are holding or interacting with that reflects their personality (e.g., a book for an INTP, a paintbrush for an ISFP, a microphone for an ENFP).
    - **Mood & Expression**: Describe the character's facial expression and the overall mood of the scene (e.g., 'a focused expression while reading a book', 'a joyful expression while singing').
    ---
    OUTPUT FORMAT: 你必須嚴格按照以下 JSON 格式回傳，不得包含任何 JSON 結構外的文字。
    ```json
    {{
      "mbti_type": "string",
      "evidence": [
        "string",
        "string",
        "string"
      ],
      "suggestion": "string",
      "image_prompt": "string"
    }}
    ```
    ---
    對話紀錄:
    ```
    {full_log}
    ```
    """
    
    generation_config = GenerationConfig(
        temperature=0.7,
        max_output_tokens=2048,
        response_mime_type="application/json",
    )
    
    response = model.generate_content(prompt, generation_config=generation_config)
    
    return json.loads(response.text)

def generate_image_with_imagen(prompt: str) -> BytesIO:
    model = ImageGenerationModel.from_pretrained("imagegeneration@005")
    response = model.generate_images(prompt=prompt, number_of_images=1)
    image_bytes = response.images[0]._image_bytes
    return BytesIO(image_bytes)

def clean_chat_log(text: str) -> str:
    lines = text.strip().split('\n')
    cleaned_lines = []
    skip_patterns = [
        re.compile(r"^\d{4}\.\d{2}\.\d{2}\s\w+$"), 
        re.compile(r"^(Stickers|Photos|Videos)$"),
        re.compile(r"^(貼圖|圖片|影片)$"),
        re.compile(r"^https?://\S+$"), 
        re.compile(r"^[\+\=\-\s]*$"),
    ]
    for line in lines:
        line = line.strip()
        if not line or any(pattern.match(line) for pattern in skip_patterns):
            continue
        cleaned_line = re.sub(r"^\d{2}:\d{2}\s", "", line)
        cleaned_line = re.sub(r"@\S+", "", cleaned_line).strip()
        if ' ' in cleaned_line:
            cleaned_lines.append(cleaned_line)
    return "\n".join(cleaned_lines)

def clean_keywords_for_wordcloud(keywords: dict) -> dict:
    """
    清理關鍵詞字典，移除包含換行符或其他多行字符的詞彙，
    以避免 WordCloud 的 "anchor not supported for multiline text" 錯誤
    """
    cleaned_keywords = {}
    for word, frequency in keywords.items():
        # 移除包含換行符的詞彙
        if '\n' in word or '\r' in word:
            continue
        # 移除空字符串或只包含空格的詞彙
        if not word or not word.strip():
            continue
        # 替換可能導致問題的字符
        clean_word = word.replace('\t', ' ').strip()
        # 確保詞彙不為空且不包含特殊字符
        if clean_word and len(clean_word.strip()) > 0:
            cleaned_keywords[clean_word] = frequency
    
    return cleaned_keywords

def analyze_text_entities(full_log: str, user_name: str) -> dict:
    user_lines = [line.replace(f"{user_name} ", "", 1) for line in full_log.split('\n') if line.startswith(user_name + " ")]
    if not user_lines:
        return {}
    my_text_only = "\n".join(user_lines)
    document = language_v2.Document(content=my_text_only, type_=language_v2.Document.Type.PLAIN_TEXT)
    
    try:
        response = language_client.analyze_entities(document=document)
        
        # 使用 entity.mentions 長度作為詞雲的權重
        raw_keywords = {
            entity.name: getattr(entity, "importance", len(entity.mentions) if entity.mentions else 1)
            for entity in response.entities[:30]
        }
        
        # 清理關鍵詞以避免 WordCloud 錯誤
        return clean_keywords_for_wordcloud(raw_keywords)
        
    except Exception as e:
        print(f"實體分析失敗: {e}")
        return {}

def upload_to_gcs(buffer: BytesIO, filename: str) -> str:
    try:
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(f"results/{filename}")
        blob.upload_from_file(buffer, content_type='image/png')
        return blob.public_url
    except Exception as e:
        print(f"上傳到 GCS 失敗: {e}")
        return ""

def generate_and_upload_wordcloud(keywords: dict, filename_prefix: str) -> str:
    if not keywords: 
        print("沒有關鍵詞可生成詞雲")
        return ""
    
    try:
        # 額外的安全檢查：確保所有關鍵詞都是單行文本
        safe_keywords = {k: v for k, v in keywords.items() if isinstance(k, str) and '\n' not in k and '\r' not in k and k.strip()}
        
        if not safe_keywords:
            print("清理後沒有有效的關鍵詞")
            return ""
        
        # 創建詞雲時使用更保守的參數
        wordcloud = WordCloud(
            width=800, 
            height=400, 
            background_color='white', 
            font_path="NotoSansTC-VariableFont_wght.ttf", 
            max_words=100,  # 限制詞彙數量
            relative_scaling=0.5,  # 調整字體大小比例
            colormap='viridis'
        ).generate_from_frequencies(safe_keywords)
        
        # 生成圖片
        buf = BytesIO()
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.savefig(buf, format='png', bbox_inches='tight', dpi=150)
        plt.close()
        buf.seek(0)
        
        filename = f"wordcloud-{filename_prefix}-{os.urandom(4).hex()}.png"
        return upload_to_gcs(buf, filename)
        
    except Exception as e:
        print(f"生成詞雲失敗: {e}")
        import traceback
        traceback.print_exc()
        return ""
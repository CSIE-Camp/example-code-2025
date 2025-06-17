
import google.generativeai as genai

genai.configure(api_key="YOUR GEMINI API KEY")  # 替換成你的 API Key

# 設定模型
model = genai.GenerativeModel('gemini-2.0-flash')

# 與 gemini 對話
prompt = "請問你是誰？"
response = model.generate_content(prompt)
print(response.text)
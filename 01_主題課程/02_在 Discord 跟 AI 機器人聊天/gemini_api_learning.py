
import google.generativeai as genai

# 填入你的 gemini 的 API key
GEMINI_API_KEY = "YOUR GEMINI API KEY"

# 啟動 gemini
genai.configure(api_key=GEMINI_API_KEY)

# 設定模型
model = genai.GenerativeModel('gemini-2.0-flash')

# 與 gemini 對話
prompt = "請問你是誰？"
response = model.generate_content(prompt)
print(response.text)
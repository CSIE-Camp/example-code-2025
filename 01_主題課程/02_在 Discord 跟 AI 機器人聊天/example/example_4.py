
import google.generativeai as genai

genai.configure(api_key="YOUR GEMINI API KEY")  # 替換成你的 API Key

# 設定模型
model = genai.GenerativeModel('gemini-2.0-flash')

# 與 gemini 對話
while True:
    prompt = input("你：")

    # 檢查是否輸入退出
    if prompt.lower() in ['exit', 'quit']:
        print("結束對話。")
        break

    # gemini 回傳的回答
    response = model.generate_content(prompt)
    print("Gemini：" + response.text)
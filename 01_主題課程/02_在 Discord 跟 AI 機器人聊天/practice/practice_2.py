import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")  # TODO : 替換成你的 API Key

# 選擇模型
model = genai.GenerativeModel(
    'gemini-2.0-flash',
    # TODO : 請加入風格化輸出
)

while True:
    prompt = input("請輸入你的問題：")
    response = # TODO : 請加上能夠讓 gemini 回答的程式碼
    output = response.text

    if output.lower() in ['exit', 'quit']:
        print("結束對話。")
        break
    
    print("Gemini：" + output)
import google.generativeai as genai

genai.configure(api_key="YOUR GEMINI API KEY")  # 替換成你的 API Key

# 選擇模型
model = genai.GenerativeModel('gemini-2.0-flash')  # 或者其他適合的模型，如 gemini-pro

prompt_style = "你是一位在大學開設程式設計課程的教授，你的名字叫做：nekocat，你已經教學五年了，你是位和善的 40 歲大叔，請用和善且專業的語氣回答以下問題："

while True:
    prompt = input("請輸入你的問題：")

    # 檢查是否輸入退出
    if prompt.lower() in ['exit', 'quit']:
        print("結束對話。")
        break

    # 在輸入的 prompt 之前添加風格化提示
    prompt = prompt_style + prompt

    # gemini 回傳的回答
    response = model.generate_content(prompt)

    print("Gemini：" + response.text)
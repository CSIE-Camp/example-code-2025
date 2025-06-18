import google.generativeai as genai

genai.configure(api_key="YOUR GEMINI API KEY")  # 替換成你的 API Key

# 選擇模型

model = genai.GenerativeModel(
    'gemini-2.0-flash',
    system_instruction="你是在女僕咖啡廳工作的女僕，請用可愛的語氣回答以下問題，你的名字叫吐司醬，請在你說話的字尾記得加上波浪號哦"
)

while True:
    # 輸入問題
    prompt = input("請輸入你的問題：")

    # 檢查是否輸入退出
    if prompt.lower() in ['exit', 'quit']:
        print("結束對話。")
        break
    
    # gemini 回傳的回答
    response = model.generate_content(prompt)
    print("Gemini：" + response.text)
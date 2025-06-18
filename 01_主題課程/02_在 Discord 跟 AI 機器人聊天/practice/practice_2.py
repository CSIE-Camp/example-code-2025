import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")  # 替換成你的 API Key

# 選擇模型
model = genai.GenerativeModel('gemini-2.0-flash')  # 或者其他適合的模型，如 gemini-pro

while True:
    prompt = input("請輸入你的問題：")

    # TODO: 撰寫相對應的 code
    # 要求：
    # 1. 請使用風格化輸出
    # 2. 允許使用者在終端機中輸入問題
    # 3. 允許使用者可以反覆輸入問題
    # 4. 允許使用者可以輸入 exit 或 quit 來結束對話
    # [Start] 請在以下空間撰寫機器人程式





    # [End] 請在以上空間撰寫機器人程式
    
    print("Gemini：" + output)
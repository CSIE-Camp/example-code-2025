import google.generativeai as genai
import os

genai.configure(api_key="YOUR GEMINI API KEY")  # 替換成你的 API Key

model = genai.GenerativeModel("gemini-2.0-flash")

def main():
    print("Gemini 對話機器人已啟動！")
    print("輸入 'exit' 或 'quit' 即可結束對話。")
    print("-" * 30)

    # 初始化對話歷史
    # 這裡的 history 參數可以用來傳遞之前的對話歷史
    chat = model.start_chat(history=[])

    while True:
        # 獲取使用者輸入
        prompt = input("你: ")

        # 檢查是否要結束對話
        if prompt.lower() in ["exit", "quit"]:
            print("-" * 30)
            print("感謝使用，對話結束！")
            break

        # 將訊息傳送給 Gemini，Gemini 會自動處裡對話歷史
        response = chat.send_message(prompt)
        
        print("Gemini:", response.text)
        print("\n") # 確保換行


    # (可選) 印出完整的對話歷史
    print("\n--- 完整對話歷史 ---")
    for message in chat.history:
        print(message)


if __name__ == "__main__":
    main()
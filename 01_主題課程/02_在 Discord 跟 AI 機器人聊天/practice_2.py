import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")  # 替換成你的 API Key

# 選擇模型
model = genai.GenerativeModel('gemini-2.0-flash')  # 或者其他適合的模型，如 gemini-pro

# TODO：在這之下撰寫程式


# 在這之上撰寫程式
print(output)
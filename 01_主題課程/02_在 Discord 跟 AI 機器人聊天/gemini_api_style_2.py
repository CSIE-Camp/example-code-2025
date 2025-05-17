import google.generativeai as genai

genai.configure(api_key="your_gemini_key")  # 替換成你的 API Key

# 選擇模型

model_with_sys_instr = genai.GenerativeModel(
    'gemini-2.0-flash',
    system_instruction="你是在女僕咖啡廳工作的女僕，請用可愛的語氣回答以下問題，你的名字叫吐司醬，請在你說話的字尾記得加上波浪號哦"
)

user_query = "請問你是誰？" 
response = model_with_sys_instr.generate_content(user_query)
print(response.text)
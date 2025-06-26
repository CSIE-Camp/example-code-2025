from flask import Flask, request, render_template_string
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from path import passwd_path
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# 帳號設定
TARGET_USERNAME = "admin"

# 從字典第5000～9999筆中隨機選密碼
with open(passwd_path, encoding="utf-8", errors="ignore") as f:
    passwords = [line.strip() for i, line in enumerate(f) if 5000 <= i < 10000 and line.strip()]

TARGET_PASSWORD = random.choice(passwords)
print("="*50)
print(f"🌟 目標帳號: {TARGET_USERNAME}")
print(f"🌟 目標密碼: {TARGET_PASSWORD}")
print("系統已啟動，可以開始嘗試爆破！")
print("="*50)

# HTML 頁面
LOGIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>登入系統</title>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; }
        .login-box { max-width: 400px; margin: 0 auto; padding: 20px; border: 1px solid #ccc; }
        input[type="text"], input[type="password"] { padding: 10px; font-size: 16px; width: 200px; }
        input[type="submit"] { padding: 10px 20px; font-size: 16px; margin-top: 10px; }
        .error { color: red; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>XX教學平台登入系統</h2>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="請輸入帳號" maxlength="32" required><br><br>
            <input type="password" name="password" placeholder="請輸入密碼" maxlength="32" required><br>
            <input type="submit" value="登入">
        </form>
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
'''

SUCCESS_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>登入成功</title>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; background: #000; color: #0f0; }
        .hacker-text { font-size: 48px; margin: 50px 0; text-shadow: 0 0 10px #0f0; }
        .hacker-img { margin-top: 30px; }
    </style>
</head>
<body>
    <div class="hacker-text">You are a hacker</div>
    <div class="hacker-img">
        <img src="/static/邪惡歐姆巴.jpg" alt="Hacker Image" width="300">
    </div>
    <p>帳號: {{ username }}</p>
    <p>密碼: {{ password }}</p>
    <a href="/" style="color: #0f0;">重新開始</a>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(LOGIN_PAGE)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')

    if user == TARGET_USERNAME and pw == TARGET_PASSWORD:
        return render_template_string(SUCCESS_PAGE, username=user, password=pw)
    else:
        return render_template_string(LOGIN_PAGE, error='帳號或密碼錯誤！')

if __name__ == '__main__':
    app.run(debug=False, port=5000)

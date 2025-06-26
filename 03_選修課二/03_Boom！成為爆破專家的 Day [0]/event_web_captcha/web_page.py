from flask import Flask, request, render_template_string, send_file, session
from captcha import generate_captcha_image
import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from path import passwd_path

app = Flask(__name__)
app.secret_key = 'super-secret-key'

# 隨機密碼（從字典第 5000～10000 筆抽取）
with open(passwd_path, encoding="utf-8") as f:
    lines = f.readlines()[300:500]
PASSWORD = random.choice(lines).strip()
USERNAME = "admin"

print("="*50)
print(f"🎯 登入帳號: {USERNAME}")
print(f"🔐 登入密碼: {PASSWORD}")
print("="*50)

LOGIN_HTML = '''
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>登入系統（含驗證碼）</title>
    <style>
        body {
            font-family: "微軟正黑體", sans-serif;
            background: #f2f2f2;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login-box {
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            width: 350px;
            text-align: center;
        }
        h2 {
            margin-bottom: 30px;
        }
        input[type=text], input[type=password] {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
            font-size: 16px;
        }
        button {
            margin-top: 20px;
            padding: 10px 30px;
            font-size: 16px;
            background: #4CAF50;
            border: none;
            color: white;
            border-radius: 6px;
            cursor: pointer;
        }
        button:hover {
            background: #45a049;
        }
        .error {
            color: red;
            margin-top: 15px;
        }
        .captcha-img {
            margin-top: 10px;
            border: 1px solid #ccc;
            width: 100%;
        }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>登入系統</h2>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="帳號" required><br>
            <input type="password" name="password" placeholder="密碼" required><br>
            <input type="text" name="captcha" placeholder="請輸入驗證碼" maxlength="5" required><br>
            <img src="/captcha" class="captcha-img" onclick="this.src='/captcha?'+Math.random()" title="點擊圖片刷新驗證碼"><br>
            <button type="submit">登入</button>
        </form>
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
'''

SUCCESS_HTML = '''
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>登入成功</title>
    <style>
        body {
            background: #000;
            color: #0f0;
            text-align: center;
            font-family: monospace;
            padding-top: 100px;
        }
        .hacker-text {
            font-size: 48px;
            text-shadow: 0 0 10px #0f0;
        }
        a {
            color: #0f0;
            text-decoration: underline;
        }
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
    return render_template_string(LOGIN_HTML)

@app.route('/captcha')
def serve_captcha():
    filename, text = generate_captcha_image()
    session['captcha'] = text.lower()
    return send_file(filename, mimetype='image/png')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')
    cap = request.form.get('captcha', '').lower()
    cap_session = session.get('captcha', '').lower()

    if cap != cap_session:
        return render_template_string(LOGIN_HTML, error="驗證碼錯誤，請再試一次")
    if user == USERNAME and pw == PASSWORD:
        return render_template_string(SUCCESS_HTML, password=PASSWORD, username=USERNAME)
    return render_template_string(LOGIN_HTML, error="帳號或密碼錯誤，已重設驗證碼")

if __name__ == '__main__':
    app.run(debug=False, port=5000)

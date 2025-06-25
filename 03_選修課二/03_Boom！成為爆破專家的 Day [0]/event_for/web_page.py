# server.py
from flask import Flask, request, render_template_string
import random

app = Flask(__name__)
app.secret_key = 'secret'

TARGET_PASSWORD = str(random.randint(10000, 13000))
print(f"🎯 目標密碼: {TARGET_PASSWORD}")

LOGIN_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>身分證後五碼登入系統</title>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; }
        .login-box { max-width: 400px; margin: 0 auto; padding: 20px; border: 1px solid #ccc; }
        input[type="text"] { padding: 10px; font-size: 16px; width: 200px; }
        input[type="submit"] { padding: 10px 20px; font-size: 16px; margin-left: 10px; }
        .error { color: red; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>身分證後五碼登入系統</h2>
        <form method="POST" action="/login">
            <input type="text" name="password" placeholder="請輸入身分證後五碼" maxlength="5" required>
            <input type="submit" value="登入">
        </form>
        {% if error %}
        <div class="error">{{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
'''  # 你的 HTML

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
        <img src="https://via.placeholder.com/400x300/000000/00ff00?text=HACKER" alt="Hacker Image">
    </div>
    <p>密碼: {{ password }}</p>
    <a href="/" style="color: #0f0;">重新開始</a>
</body>
</html>
'''  # 你的 HTML

@app.route('/')
def index():
    return render_template_string(LOGIN_PAGE)

@app.route('/login', methods=['POST'])
def login():
    pw = request.form.get('password')
    if pw == TARGET_PASSWORD:
        return render_template_string(SUCCESS_PAGE, password=TARGET_PASSWORD)
    else:
        return render_template_string(LOGIN_PAGE, error='密碼錯誤！')

if __name__ == '__main__':
    # 啟動 Flask HTML 登入頁
    app.run(port=5000, debug=False)

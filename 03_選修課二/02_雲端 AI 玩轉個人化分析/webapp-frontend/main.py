import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 從環境變數讀取後端 Cloud Function 的 URL
FUNCTION_URL = os.environ.get("FUNCTION_URL", "http://localhost:8081")

@app.route("/")
def index():
    """渲染主頁面。"""
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    """
    作為代理，將請求轉發到後端的 Cloud Function。
    """
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "請求中缺少文字"}), 400

    try:
        # 將請求發送到真正的後端
        headers = {"Content-Type": "application/json"}
        response = requests.post(FUNCTION_URL, json=data, headers=headers, timeout=120)
        response.raise_for_status() # 如果後端回傳錯誤，這裡會拋出異常
        return jsonify(response.json()), response.status_code
        
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"無法連接到分析服務: {e}"}), 502

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
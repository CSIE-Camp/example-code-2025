from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
import os
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from path import captha_save_dir
# 改這裡：設定絕對儲存路徑
SAVE_DIR = captha_save_dir
SAVE_FILENAME = os.path.join(SAVE_DIR, "captcha_mild.png")

def generate_captcha_image(filename=SAVE_FILENAME, text=None, width=160, height=60, font_size=36):
    if not text:
        text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)).lower()

    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    spacing = width // len(text)
    for i, char in enumerate(text):
        angle = random.randint(-5, 5)
        char_img = Image.new('RGBA', (spacing, height), (255, 255, 255, 0))
        char_draw = ImageDraw.Draw(char_img)
        char_draw.text((5, 10), char, font=font, fill=(0, 0, 0))
        char_img = char_img.rotate(angle, resample=Image.BICUBIC, expand=1)
        image.paste(char_img, (i * spacing, 0), char_img)

    for _ in range(2):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        draw.line([(x1, y1), (x2, y2)], fill=(150, 150, 150), width=1)

    for _ in range(40):
        x, y = random.randint(0, width), random.randint(0, height)
        draw.point((x, y), fill=(random.randint(120, 180),)*3)

    image = image.transform(
        (width, height),
        Image.AFFINE,
        (1, 0.05 * random.uniform(-1, 1), 0, 0.05 * random.uniform(-1, 1), 1, 0),
        Image.BICUBIC
    )
    image = image.filter(ImageFilter.GaussianBlur(0.2))

    image.save(filename)
    return filename, text

# 測試
if __name__ == "__main__":
    fname, text = generate_captcha_image()
    print(f"✅ 圖片儲存於: {fname}")
    print(f"✅ 驗證碼為: {text}")

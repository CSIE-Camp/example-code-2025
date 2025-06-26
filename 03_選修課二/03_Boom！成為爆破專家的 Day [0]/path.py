# path.py
import os

# 取得 path.py 所在的資料夾路徑
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 路徑
captha_save_dir = os.path.join(BASE_DIR, 'event_web_captcha')

passwd_path = os.path.join(BASE_DIR, 'password','xato-net-10-million-passwords-10000.txt')
captha_get_path = os.path.join(captha_save_dir, 'captcha_get.png')

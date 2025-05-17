import discord
import random
import asyncio

# 啟用所有 intents，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件，並啟用 intents
bot = discord.Client(intents=intents)

# 猜拳選項
choices = ["剪刀", "石頭", "布"]

# Boss 選項
bosses_name = ["狗頭人領主阿爾方", "青眼惡魔", "封弊者"]
bosses_avatar_url = ["https://i1.kknews.cc/g66DCL7nYT8RuZjBrLXeCzxsEqb72xPm_w/0.jpg", "https://i.ytimg.com/vi/GYk_ns2iPQI/maxresdefault.jpg", "https://p2.bahamut.com.tw/HOME/creationCover/00/0004777800.JPG"]

# 用來儲存使用者連勝的次數
bot.rps_streak = 0

# 用來驗證是否啟動機器人
@bot.event
async def on_ready():
    print(f'已登入為 {bot.user}')

@bot.event
async def on_message(message):
    """當使用者輸入訊息時執行"""

    # 忽略機器人訊息
    if message.author.bot:
        return

    # 使用者輸入以 ?rps 開頭的指令，後面接選項
    # 例如 ?rps 剪刀、?rps 石頭、?rps 布
    if message.content.startswith("?rps"): 

        # 取得使用者的選項
        player_choice = message.content.split(" ")[1]

        # 如果輸入選項不正確，則不理會
        if player_choice not in choices:
            await message.channel.send("請輸入正確的選項: 剪刀、石頭、布")
            return
    
        # 隨機選擇 Webhook 角色的出拳
        boss_choice = random.choice(choices)  
    
        # 決定猜拳結果
        result = determine_winner(player_choice, boss_choice, bosses_name[bot.rps_streak])
        
        # 創建 Webhook
        webhook = await message.channel.create_webhook(name="RPS_Webhook")
    
        # 已指定名稱跟指定頭像發送他出的拳型
        await webhook.send(boss_choice, username = bosses_name[bot.rps_streak], avatar_url = bosses_avatar_url[bot.rps_streak])
    
        # 等待 Webhook 訊息確實送達
        def check(m):
            return m.author.id == webhook.id and m.content == boss_choice  # 確保是 Webhook 發出的訊息
        try:
            await bot.wait_for("message", check=check, timeout=5)  # 最多等 5 秒
        except asyncio.TimeoutError:
            print("error")

        # 休息 0.5 秒
        await asyncio.sleep(0.5)
        
        # 判定勝負
        await message.channel.send(result)
        
        # 勝則換下一個 boss，負則重頭開始
        if result ==  "你贏了！": 
            """如果贏了"""
            # 如果還沒挑戰完所有 boss，則換下一個 boss
            if bot.rps_streak < len(bosses_name)-1:
                await webhook.send(f"一切都還沒結束呢...\n{bosses_name[bot.rps_streak+1]}會繼承我的意志的", username = bosses_name[bot.rps_streak], avatar_url = bosses_avatar_url[bot.rps_streak])
            # 贏了連勝 + 1
            bot.rps_streak += 1
        else: 
            """如果輸了"""
            # 連勝次數歸零
            bot.rps_streak = 0
            await webhook.send("真菜，再多練練吧", username = bosses_name[bot.rps_streak], avatar_url = bosses_avatar_url[bot.rps_streak])

# 這裡是用來判斷猜拳輸贏的函式
def determine_winner(player, boss, boss_name):
    """判斷猜拳輸贏"""
    if player == boss:
        return "平手！"
    elif (player == "剪刀" and boss == "布") or \
         (player == "石頭" and boss == "剪刀") or \
         (player == "布" and boss == "石頭"):
        return "你贏了！"
    else:
        return f"{boss_name}贏了！"

# 啟動機器人（請填入你的 Token）
bot.run(token)
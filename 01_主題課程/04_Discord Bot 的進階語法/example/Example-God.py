import discord
import random

# 啟用所有 intents，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件，並啟用 intents
bot = discord.Client(intents=intents)

# 猜大小選項
choices = ["大", "小"]

@bot.event
async def on_ready():
    print(f'已登入為 {bot.user}')

@bot.event
async def on_message(message):
    """當使用者輸入猜拳指令時執行"""
    if message.author.bot:  # 忽略機器人訊息
        return

    if message.content.startswith("?猜大小 "):  # 確保訊息是猜拳指令
        player_choice = message.content.split(" ")[1]

        if player_choice not in choices:
            await message.channel.send("請輸入正確的選項: 大、小")
            return
    
        point = random.randint(1, 6)  # 隨機選擇骰子點數
        
        # 創建 Webhook
        webhook = await message.channel.create_webhook(name="RPS_Webhook")
    
        # 決定猜拳結果
        if (player_choice == "大" and point >= 4) or (player_choice == "小" and point <= 3):
            # 已指定名稱發送結果
            await webhook.send("猜對了，愉悅吧少年", username = "莊家", avatar_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcBewITKG2y8i9gW_i9ad3FRN22g6GoIO0tA&s")
        else:
            # 已指定名稱發送結果
            await webhook.send("猜錯了，一切都是命中注定", username = "莊家", avatar_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcBewITKG2y8i9gW_i9ad3FRN22g6GoIO0tA&s")
        
# 啟動機器人（請填入你的 Token）
bot.run(token)
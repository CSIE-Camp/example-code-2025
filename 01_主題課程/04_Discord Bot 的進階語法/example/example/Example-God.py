import discord
import random

# 啟用所有 intents，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件，並啟用 intents
bot = discord.Client(intents=intents)

# 猜大小選項
choices = ["大", "小"]

@bot.event
async def on_message(message):
    """當收到訊息時觸發的事件"""

    # 忽略機器人的訊息 (避免無限迴圈)
    if message.author.bot: 
        return

    # 如果訊息是以 ?猜大小 且空格後面是選項
    # 例如 ?猜大小 大
    if message.content.startswith("?猜大小 "):

        # 取得玩家的選擇
        # 例如 ?猜大小 大 -> player_choice = 大  
        player_choice = message.content.split(" ")[1]

        # 檢查玩家的選擇是否正確
        # 如果玩家的選擇不在 choices 中，則回覆錯誤訊息
        # 例如 ?猜大小 中等 -> 觸發 if player_choice not in choices
        if player_choice not in choices:
            await message.channel.send("請輸入正確的選項: 大、小")
            return
    
        # 隨機選擇骰子點數 (1~6)
        point = random.randint(1, 6)
        
        # 創建 Webhook
        webhook = await message.channel.create_webhook(name="RPS_Webhook")
    
        # 決定猜大小結果
        if (player_choice == "大" and point >= 4) or (player_choice == "小" and point <= 3):
            # 利用 webhook 指定名稱與頭像發送結果
            await webhook.send("猜對了，愉悅吧少年", username = "莊家", avatar_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcBewITKG2y8i9gW_i9ad3FRN22g6GoIO0tA&s")
        else:
            # 利用 webhook 指定名稱與頭像發送結果
            await webhook.send("猜錯了，一切都是命中注定", username = "莊家", avatar_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcBewITKG2y8i9gW_i9ad3FRN22g6GoIO0tA&s")
        
# 啟動機器人（請填入你的 Token）
bot.run(token)
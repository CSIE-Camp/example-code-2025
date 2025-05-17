"""
這段程式碼的功能是：

創建 30 個 webhook，並模擬點名。
"""

# 引入需要的模組 (像是新增桌遊的擴充)
import discord
import json

with open('my.json') as f:
    d = json.load(f)

token = d['token']

# 啟用所有 intents(意圖)，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件 (像是召喚出這隻你的 DC 機器人)
# 並啟用 intents (讓機器人能夠聽到所有事件)
bot = discord.Client(intents=intents)

@bot.event
async def on_message(message):
    """當收到訊息時觸發的事件"""
    # 如果訊息是 ?webhook 
    if message.content == "?webhook":

        # TODO: 創建 30 個 Webhook (提示: 使用迴圈)，
        # 編號 i 的 Webhook 名稱改為「i 號」發送訊息「嗨!」
        """
        迴圈 30 次:
            創建一個 Webhook
            使用 Webhook 發送訊息
        """

# 執行機器人
# token 請填入你的機器人 token
bot.run(token)
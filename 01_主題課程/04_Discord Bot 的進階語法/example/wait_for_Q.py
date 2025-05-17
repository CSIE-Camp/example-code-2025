"""
這段程式碼的功能是：

等待訊息，回覆訊息，並在 3 秒內檢查使用者的回覆。
"""

# 引入需要的模組 (像是新增桌遊的擴充)
import discord

# 啟用所有 intents(意圖)，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件 (像是召喚出這隻你的 DC 機器人)
# 並啟用 intents (讓機器人能夠聽到所有事件)
bot = discord.Client(intents=intents)

@bot.event
async def on_message(message):
    """當收到訊息時觸發的事件"""

    # 忽略機器人的訊息 (避免無限迴圈)
    if message.author.bot:
        return
    
    # 如果訊息為 ?DC醬，則發送「嗨~」的訊息
    if message.content == '?DC醬':
        await message.channel.send('嗨~')
    
    # TODO: 等待使用者的回覆，檢查回覆是否為：「你喜歡什麼」，等待 3 秒
    """
    def check(m):
        檢查回覆是否為：「你喜歡什麼」，是則回傳 True，否則回傳 False
    """
    # your code here

    """
    等待使用者的回覆，並檢查回覆是否符合條件，而且在 3 秒內回答
    """
    # your code here

    await message.channel.send(f'比起 python，我更喜歡 {msg.author}')

# 執行機器人
# token 請填入你的機器人 token
bot.run(token)
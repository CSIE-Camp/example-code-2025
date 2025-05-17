"""
這段程式碼的功能是：

一個接龍搶答的小遊戲
當使用者發送「?接龍搶答」時，機器人會回覆「蘋果」
接著，機器人會等待使用者的回覆
如果使用者的回覆是以「果」開頭，並且是對「蘋果」的回覆
則機器人會回覆「讚讚！」，並顯示使用者的名稱
"""

import discord

intents = discord.Intents.all()
bot = discord.Client(intents=intents)

@bot.event
async def on_message(message):
    """當收到訊息時觸發的事件"""

    # 忽略機器人的訊息 (避免無限迴圈)
    if message.author.bot:
        return
    
    # 如果訊息為 ?接龍搶答，則發送「蘋果」的訊息
    if message.content == '?接龍搶答':
        question = await message.channel.send('蘋果')

    # 等待使用者的回覆，「檢查」是否為：「果」開頭 而且 是對「蘋果」回覆的訊息
    # 如果是，則發送「讚讚！」的訊息
    # 如果不是，則不做任何事

    # 製作檢查函式
    # 檢查訊息是否為：「果」開頭 而且 是對「蘋果」回覆的訊息
    def check(m):
        return m.content.startswith('果') and m.reference.message_id == question.id
    
    # 等待使用者的回覆，並檢查是否符合條件
    # 如果符合條件，才繼續往下執行
    msg = await bot.wait_for('message', check=check, timeout=3)
    await message.channel.send(f'{msg.author}，讚讚！')

# 執行機器人
# token 請填入你的機器人 token
bot.run(token)
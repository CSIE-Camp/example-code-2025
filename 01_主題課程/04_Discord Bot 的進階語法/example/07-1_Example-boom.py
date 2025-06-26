import discord

# 啟用所有 intents，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件，並啟用 intents
bot = discord.Client(intents=intents)

@bot.event
async def on_message(message):
    """當收到訊息時觸發的事件"""

    # 忽略機器人的訊息 (避免無限迴圈)
    if message.author.bot: 
        return
    
    # 如果訊息是 ?boom 
    if message.content == '?boom':

        # 發送一個訊息，並將其儲存到變數 question 中
        question = await message.channel.send('好...好想...爆裂')

        # 檢測反應的函數
        # 當使用者對訊息添加反應時，檢查反應是否為 💣
        def check(reaction, user):
            return str(reaction.emoji) == '💣' and reaction.message.id == question.id
        
        # 等待使用者添加反應，並檢查是否符合條件
        msg = await bot.wait_for('reaction_add', check = check, timeout = 3)

        # 如果在 3 秒內添加反應，則發送訊息
        await message.channel.send(f'{msg.author}：Drain Touch！')
        await message.channel.send("可...可惡...")

# 啟動機器人（請填入你的 Token）
bot.run(token)
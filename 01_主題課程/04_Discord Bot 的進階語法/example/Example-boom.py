import discord

# 啟用所有 intents，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件，並啟用 intents
bot = discord.Client(intents=intents)

@bot.event
async def on_message(message):
    if message.content == '?boom':
        question = await message.channel.send('好...好想...爆裂')

        def check(reaction, user):
            return str(reaction.emoji) == '💣' and reaction.message.id == question.id
        
        msg = await bot.wait_for('reaction_add', check = check, timeout = 3)
        await message.channel.send(f'{msg.author}：Drain Touch！')

        await message.channel.send("可...可惡...")

# 啟動機器人（請填入你的 Token）
bot.run(token)
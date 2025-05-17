"""
這段程式碼的功能是：

有人新增一個反應時，移除反應。
"""

import discord

intents = discord.Intents.all()
bot = discord.Client(intents=intents)

@bot.event
async def on_reaction_add(reaction, user):
    """當收到訊息時觸發的事件"""

    # 忽略機器人的反應 (避免無限迴圈)
    if user.bot: 
        return
    
    # 如果有人按下反應，則移除他
    await reaction.message.remove_reaction(reaction.emoji, user)

# 執行機器人
# token 請填入你的機器人 token
bot.run(token)
"""
這段程式碼的功能是：

當有人按「👍」，機器人會誇獎他。
當有人按「❌」，機器人會刪掉那則訊息。
"""

import discord

intents = discord.Intents.all()
bot = discord.Client(intents=intents)

@bot.event
async def on_reaction_add(reaction, user):
    """這個事件，當使用者按下反應時會觸發""" 
    
    # 如果按 👍，則發送訊息，說按下讚的人很棒
    if reaction.emoji == "👍": 
        await reaction.message.channel.send(f"{user.name} 很棒")

    # 如果按 ❌，則移除訊息
    elif reaction.emoji == "❌": 
        await reaction.message.delete()  

# 執行機器人
# token 請填入你的機器人 token
bot.run(token)
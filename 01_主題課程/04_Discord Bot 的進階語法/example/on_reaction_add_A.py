"""
這段程式碼的功能是：

當有人按「👍」，機器人會誇獎他。
當有人按「❌」，機器人會刪掉那則訊息。
"""

# 引入需要的模組 (像是新增桌遊的擴充)
import discord

# 啟用所有 intents(意圖)，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件 (像是召喚出這隻你的 DC 機器人)
# 並啟用 intents (讓機器人能夠聽到所有事件)
bot = discord.Client(intents=intents)

@bot.event
async def on_reaction_add(reaction, user):
    """on_reaction_add"""
    """這個事件，當使用者按下反應時會觸發""" 
    # 提供這個事件，相當於叫他聽話。
    # 當按下反應時，就是叫他做事。(像是家人叫你做家事)
    """reaction, user"""
    """此事件需要兩個東西，reaction 和 user，"""
    # 叫他做事，要給他做事必須要的東西 (像是家人叫你洗碗，他要給你碗)
    # reaction 是按下的反應，user 是按下反應的人

    if reaction.emoji == "👍": # 如果按 👍
        # 則發送訊息，說按下讚的人很棒
        await reaction.message.channel.send(f"{user.name} 很棒")

    elif reaction.emoji == "❌": # 如果按 ❌
        # 則移除訊息
        await reaction.message.delete()  

# 執行機器人
# token 請填入你的機器人 token
bot.run(token)
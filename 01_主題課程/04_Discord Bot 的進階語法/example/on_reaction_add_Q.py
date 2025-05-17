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
async def  # TODO: 某個事件( 這個事件需要什麼 ):
    """如果按 👍，則發送訊息，說按下讚的人很棒"""
    if reaction.emoji == "👍": 
        await reaction.message.channel.send(f"{user.name} 很棒")
        
    # TODO: 如果按 ❌，則移除訊息
    """
    如果按 ❌ :
        刪除訊息
    """

# 執行機器人
# token 請填入你的機器人 token
bot.run(token)
"""
這段程式碼的功能是：

使用者按下反應，回「對<某訊息>按下<某反應>」
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
    """這個事件，當使用者按下反應時會觸發""" 

    # 如果有人對 emoji 按下反應，則回覆「對<某訊息>按下<某反應>」
    await reaction.message.channel.send( f"*{user.name}* 你在**{reaction.message.content}**加了{reaction.emoji}" )

# 執行機器人
# token 請填入你的機器人 token
bot.run(token)
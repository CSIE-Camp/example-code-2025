"""
這段程式碼的功能是：

收到訊息時，幫訊息新增一個反應。
"""

import discord

intents = discord.Intents.all()
bot = discord.Client(intents=intents)

@bot.event
async def on_message(message):
    """當收到訊息時觸發的事件"""

    # 如果訊息是以 ?add 且空格後面是反應
    # 例如 ?add 👍
    if message.content.startswith("?add"):
        # 取得要添加的反應
        reaction = message.content.split(" ")[1]
        # 添加反應到訊息
        await message.add_reaction(reaction)

# 執行機器人
# token 請填入你的機器人 token
bot.run(token)
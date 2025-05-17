import discord  # 引入 discord API 的套件

# 啟用所有 intents，讓機器人能夠監聽各種事件
intents = discord.Intents.all()
bot = discord.Client(intents=intents)

# 存儲等待反應的訊息
bot.message_wait_for_reaction = None
bot.good_reaction_amount = 0  

@bot.event
async def on_message(message):
    if message.content == "?good":
        bot.message_wait_for_reaction = await message.channel.send("我需要更多的讚")
        await bot.message_wait_for_reaction.add_reaction("👍")

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    if reaction.message == bot.message_wait_for_reaction and reaction.emoji == "👍":
        bot.good_reaction_amount += 1
        status_w = discord.Status.idle
        activity_w = discord.Activity(type=discord.ActivityType.playing, name= f"總共按了 {bot.good_reaction_amount} 個讚")

        await bot.change_presence(status=status_w, activity=activity_w)
        
@bot.event
async def on_reaction_remove(reaction, user):
    """當使用者移除反應時觸發"""
    if user.bot:  
        return  # 如果是機器人自己移除反應，就不執行任何動作

    # 確保這個被移除反應的訊息，是我們記住的那則訊息
    if reaction.message == bot.message_wait_for_reaction and reaction.emoji == "👍":
        # 編輯訊息內容，通知其他人這個使用者移除了反應
        await reaction.message.edit(content=f"{user.name} 收回了一個讚")

# 讓機器人上線（需填入 Token）
bot.run(token)
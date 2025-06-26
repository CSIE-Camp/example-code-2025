import discord  # 引入 discord API 的套件

# 啟用所有 intents，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件，並啟用 intents
bot = discord.Client(intents=intents)

# 用來儲存機器人要等待的訊息
bot.message_wait_reaction = None

# 用來儲存收到按讚的數量
bot.good_reaction_amount = 0  

# 用來驗證是否啟動機器人
@bot.event
async def on_ready():
    print(f'已登入為 {bot.user}')

@bot.event
async def on_message(message):
    """當收到訊息時觸發的事件"""

    # 忽略機器人的訊息 (避免無限迴圈)
    if message.author.bot:
        return
    
    # 如果訊息是以 ?good 開頭
    if message.content == "?good":
        # 機器人會回覆「我需要更多的讚」，並將這個訊息儲存到 bot.message_wait_for_reaction
        # 儲存訊息是為了讓機器人在 on_reaction_add、on_reaction_remove 事件中，辨識機器人傳的是哪則訊息
        bot.message_wait_for_reaction = await message.channel.send("我需要更多的讚")

        # 在這則訊息添加一個「👍」的反應
        await bot.message_wait_for_reaction.add_reaction("👍")

@bot.event
async def on_reaction_add(reaction, user):
    """當收到訊息時觸發的事件"""

    # 忽略機器人的反應 (避免無限迴圈)
    if user.bot:
        return
    
    # 如果按反應的訊息，是機器人之前傳的
    # 並且按下的反應是「👍」
    if reaction.message == bot.message_wait_for_reaction and reaction.emoji == "👍":

        # 讚數 + 1
        bot.good_reaction_amount += 1

        """更新狀態欄，在狀態欄顯示讚數"""
        # 會讓機器人的狀態欄顯示「總共按了 {讚數} 個讚」
        status_w = discord.Status.idle
        activity_w = discord.Activity(type=discord.ActivityType.playing, name= f"總共按了 {bot.good_reaction_amount} 個讚")

        # 更新狀態欄
        await bot.change_presence(status=status_w, activity=activity_w)
        
@bot.event
async def on_reaction_remove(reaction, user):
    """當使用者移除反應時觸發"""

    # 忽略機器人的反應 (避免無限迴圈)
    if user.bot:  
        return 

    # 如果移除反應的訊息，是機器人之前傳的
    # 並且移除的反應是「👍」
    if reaction.message == bot.message_wait_for_reaction and reaction.emoji == "👍":
        # 編輯訊息內容，通知其他人這個使用者移除了反應
        await reaction.message.edit(content=f"{user.name} 收回了一個讚")

# 啟動機器人（請填入你的 Token）
bot.run(token)
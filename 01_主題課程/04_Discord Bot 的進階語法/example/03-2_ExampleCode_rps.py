import discord
import random

# 啟用所有 intents，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件，並啟用 intents
bot = discord.Client(intents=intents)

# 猜拳選項
emoji_to_string = {"✌️":"剪刀", "✊":"石頭", "🖐️":"布"}

# 用來儲存機器人要等待的訊息
bot.message_wait_for_reaction = None

# 用來驗證是否啟動機器人
@bot.event
async def on_ready():
    print(f'已登入為 {bot.user}')

@bot.event
async def on_message(message):
    """當收到訊息時觸發的事件"""

    # 忽略機器人訊息 (避免無限迴圈)
    if message.author.bot: 
        return

    # 如果訊息是 ?rps，則開始猜拳遊戲
    if message.content == "?rps":
        # 機器人會回覆「猜拳拚輸贏」，並將這個訊息儲存到 bot.message_wait_for_reaction
        # 儲存訊息是為了讓機器人在 on_reaction_add、on_reaction_remove 事件中，辨識機器人傳的是哪則訊息
        bot.message_wait_for_reaction = await message.channel.send("猜拳拚輸贏")

# 用來判斷猜拳結果
def determine_winner(player, boss):
    """判斷猜拳輸贏"""
    if player == boss:
        return "平手！"
    elif (player == "剪刀" and boss == "布") or \
        (player == "石頭" and boss == "剪刀") or \
        (player == "布" and boss == "石頭"):
        return "你贏了！"
    else:
        return f"對手贏了！"

@bot.event
async def on_reaction_add(reaction, user):
    """當收到訊息時觸發的事件"""

    # 忽略機器人反應 (避免無限迴圈)
    if user.bot: 
        return
    
    # 如果按反應的訊息，是機器人之前傳的
    if reaction.message == bot.message_wait_for_reaction:

        # 如果按下的反應不是剪刀、石頭、布
        # 則發送訊息，說沒有這個拳型
        if reaction.emoji not in emoji_to_string.keys():
            await reaction.message.channel.send(f"沒有{reaction.emoji}拳啦=n=")
            return
        
        # 如果按下的反應是剪刀、石頭、布
        # 則電腦隨機選擇一個拳型
        pc_choice = random.choice(list(emoji_to_string.values()))  # 隨機選擇的拳型
        player_choice = emoji_to_string[reaction.emoji]

        # 決定猜拳結果
        result = determine_winner(player_choice, pc_choice)

        # 發送訊息，說明結果
        await reaction.message.channel.send(f"對手出了{pc_choice}，因此{result}")

# 啟動機器人（請填入你的 Token）
bot.run(token)
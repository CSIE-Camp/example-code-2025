import discord
import random

# 啟用所有 intents，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件，並啟用 intents
bot = discord.Client(intents=intents)

# 猜拳選項
emoji_to_string = {"✌️":"剪刀", "✊":"石頭", "🖐️":"布"}

bot.message_wait_for_reaction = None

@bot.event
async def on_ready():
    print(f'已登入為 {bot.user}')

@bot.event
async def on_message(message):
    """當使用者輸入猜拳指令時執行"""
    if message.author.bot:  # 忽略機器人訊息
        return

    if message.content == "?rps":
        bot.message_wait_for_reaction = await message.channel.send("猜拳拚輸贏")

        for emoji in emoji_to_string.keys():
            await bot.message_wait_for_reaction.add_reaction(emoji)

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
    if reaction.message == bot.message_wait_for_reaction:
        if reaction.emoji not in emoji_to_string.keys():
            await reaction.message.channel.send(f"沒有{reaction.emoji}拳啦=n=")
            return
        
        pc_choice = random.choice(list(emoji_to_string.values()))  # 隨機選擇的拳型
        player_choice = emoji_to_string[reaction.emoji]
        # 決定猜拳結果
        result = determine_winner(player_choice, pc_choice)
        await reaction.message.channel.send(f"對手出了{pc_choice}，因此{result}")

bot.run(token)
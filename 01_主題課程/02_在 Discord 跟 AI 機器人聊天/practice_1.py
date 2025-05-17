import discord
import asyncio

from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='#', intents=intents, enable_cache=True)

# TODO: 建立對應的 event 與 command
# 要求：
# 1. 當有人對訊息按下表情符號時，機器人在伺服器頻道內可以傳訊息（訊息形式不拘）
# 2. 使用 # 作為前綴詞
# 3. 製作可以兩個小數四則運算（加減乘除）的計算機
# 4. 向機器人輸出 #Hello 時，機器人可以自我介紹
# 5(選擇性). 製作擁有更多功能的計算機(開根號、取餘數、次方等)
# [Begin] 請在以下空間撰寫機器人程式



# [End] 請在以上空間撰寫機器人程式
async def main():
    await bot.start(dc_token)

asyncio.run(main())
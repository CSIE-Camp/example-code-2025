import discord
import asyncio

from discord.ext import commands

dc_token = "YOUR DCBOT TOKEN" # 請填入你的 Discord Bot Token

# intents 為機器人的權限，這裡設定為全開
intents = discord.Intents.all()

# bot 是機器人的本體，這邊是設定他前綴，這邊設定為 %
bot = commands.Bot(command_prefix='%', intents=intents, enable_cache=True)

# event
@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        # 機器人不回覆自己的訊息
        return
    # print -> 顯示在終端機
    print(f"收到訊息: {message.content} (來自: {message.author.name})")
    
    # await message.channel.send -> 發送訊息到頻道
    await message.channel.send(f"收到訊息: {message.content} (來自: {message.author.name})")

async def main():
    await bot.start(dc_token)

asyncio.run(main())
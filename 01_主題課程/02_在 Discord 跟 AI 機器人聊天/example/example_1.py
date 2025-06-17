import discord
import asyncio

from discord.ext import commands

dc_token = "YOUR DCBOT TOKEN" # 請填入你的 Discord Bot Token

# intents 為機器人的權限，這裡設定為全開
intents = discord.Intents.all()

# bot 是機器人的本體，這邊是設定他前綴，這邊設定為 %
bot = commands.Bot(command_prefix='%', intents=intents, enable_cache=True)

@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
# 輸入%Hello呼叫指令
async def Hello(ctx):
    # 回覆Hello, world!
    await ctx.send("Hello, world!")

async def main():
    await bot.start(dc_token)

# 啟動機器人
asyncio.run(main())
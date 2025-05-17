import discord
import asyncio

from discord.ext import commands

dc_token = 'dc_token' # 請填入你的 Discord Bot Token

intents = discord.Intents.all()

# 這邊可以設定前綴，這邊設定為!
bot = commands.Bot(command_prefix='!', intents=intents, enable_cache=True)

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Hello World!"))

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")

# 接收參數其他參數
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(f"{a} + {b} = {a + b}")

async def main():
    await bot.start(dc_token)

asyncio.run(main())
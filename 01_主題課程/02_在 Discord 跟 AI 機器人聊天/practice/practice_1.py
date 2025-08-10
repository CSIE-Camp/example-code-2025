import discord
import asyncio

from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents) # TODO : 把前綴詞改成 #

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
async def Hello(ctx):
    await ctx.send("") # TODO : 把這行填入你想要的自我介紹

@bot.command()
async def add(ctx, a: float, b: float):
    c = a + b
    await ctx.send(str(a) + " + " + str(b) + " = " + str(c)) # TODO : 把這行填入你想要的加法結果

# TODO : 完成之後的減法、乘法、除法
# 請參考上面的 command


async def main():
    await bot.start('dc_token') # TODO : 填入你的 discord token

asyncio.run(main())
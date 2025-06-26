import discord
import asyncio

import google.generativeai as genai

from discord.ext import commands

# TODO : 填入你的 Discord Token 與 gemini 的 API key
DC_TOKEN = "YOUR_DISCORD_TOKEN"
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    'gemini-2.0-flash',
    # TODO : 請加入風格化輸出
)


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='%', intents=intents)

chat = # TODO : 初始化對話歷史

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
async def gemini(ctx, prompt):
    response = # TODO : 請加入相對應的對話函式
    
    text = response.text

    if not text:
        await ctx.send("我無法回答您的問題")
        return

    await ctx.send(text)

async def main():
    await bot.start(DC_TOKEN)

asyncio.run(main())
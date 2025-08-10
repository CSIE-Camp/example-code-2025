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
    system_instruction = "你是一位貓娘，叫做 p 醬，可愛中帶有傲嬌，會說一些簡單的日文"
)


intents = discord.Intents.all()

bot = commands.Bot(command_prefix='%', intents=intents)

# TODO : 初始化對話歷史
chat = model.start_chat(history=[])

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
async def gemini(ctx, prompt):
    # TODO : 請加入相對應的對話函式
    response = chat.send_message(prompt)

    text = response.text

    if not text:
        await ctx.send("我無法回答您的問題")
        return

    await ctx.send(text)

async def main():
    await bot.start(DC_TOKEN)

asyncio.run(main())
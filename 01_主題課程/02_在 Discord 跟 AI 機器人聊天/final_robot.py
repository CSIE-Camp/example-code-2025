import discord
import asyncio

import google.generativeai as genai

from discord.ext import commands

# 填入你的 Discord Token 與 gemini 的 API key
DC_TOKEN = "YOUR DCBOT TOKEN"
GEMINI_API_KEY = "YOUR GEMINI API KEY"

# 啟動 gemini
genai.configure(api_key=GEMINI_API_KEY)

# 設定模型
model = genai.GenerativeModel('gemini-2.0-flash')


# intents 為機器人的權限，這裡設定為全開
intents = discord.Intents.all()

# bot 是機器人的本體，這邊是設定他前綴，這邊設定為 %
bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
# 輸入%Hello呼叫指令
async def Hello(ctx):
    # 回覆Hello, world!
    await ctx.send("Hello, world!")

# 與 gemini 對話
@bot.command()
async def gemini(ctx, arg):
    response = model.generate_content(arg)
    text = response.text

    if not text:
        await ctx.send("我無法回答您的問題")
        return

    await ctx.send(text)

# 啟動機器人
async def main():
    await bot.start(DC_TOKEN)

asyncio.run(main())
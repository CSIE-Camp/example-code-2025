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

# TODO: 建立對應的 event 與 command
# 要求：
# 1. 利用 command 與 gemini 進行對話
# 2. 要使用風格化輸出，請加入自己的創意
# 3. 請加入預設的回答，防止 gemini 無法回答時，機器人回覆「我無法回答您的問題」
# [Start] 請在以下空間撰寫機器人程式






# [End] 請在以上空間撰寫機器人程式

# 啟動機器人
async def main():
    await bot.start(DC_TOKEN)

asyncio.run(main())
import discord
from discord.ext import commands
import requests
import base64
from io import BytesIO

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!',intents=intents)

NGROK_URL = ""  # 請替換成您的 ngrok URL

@bot.command()
async def generate(ctx, *, prompt):

    # 發送等待訊息
    await ctx.send("正在生成圖片,請稍候...")
    
    # 呼叫 API
    response = requests.post(
        f"{NGROK_URL}/generate",
        json={"prompt": prompt}
    )

    data = response.json()
    if data['status'] == 'success':
        #將 base64 轉回圖片
        image_data = base64.b64decode(data['image'])
        im = BytesIO(image_data)
        
        # 發送圖片
        await ctx.send(file=discord.File(im, 'generated_image.png'))
    else:
        await ctx.send("生成圖片時發生錯誤")

bot.run('') # 請替換成您的 token
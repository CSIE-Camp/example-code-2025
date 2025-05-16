import discord
import json

with open('my.json') as f:
    d = json.load(f)

token = d['token']
# 啟用所有 intents，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件，並啟用 intents
bot = discord.Client(intents=intents)

bot.message_wait_reaction = None
bot.file = None
# 猜大小選項
bot.characters_info = []
bot.choices = []
bot.left_choices = []

@bot.event
async def on_ready():
    print(f'已登入為 {bot.user}')

@bot.event
async def on_message(message):
    """當使用者輸入猜拳指令時執行"""
    if message.author.bot:  # 忽略機器人訊息
        return

    if message.content == "?start":

        try: 
            bot.characters_info = eval(generate_character())
        except Exception as e:
            print(f"發生錯誤: {str(e)}")
            return

        for character in bot.characters_info:
            print(character)
            character['avatar_url'] = await generate(ctx=message, prompt=f"給我一個角色的圖，這個角色是「{character['name']}」")

        bot.message_wait_reaction = await message.channel.send("好像發生什麼異變了，跟眾人打聽看看吧")

        print(bot.characters_info)
        for character in bot.characters_info:
            print(character)
            await bot.message_wait_reaction.add_reaction(character["emoji"])
            bot.choices.append(character["emoji"])
            bot.left_choices.append(character["emoji"])
    

import requests
import base64
from io import BytesIO

NGROK_URL = "https://e276-34-126-110-61.ngrok-free.app"  # 請替換成您的 ngrok URL

async def get_photo(prompt) -> requests.Response:
    return requests.post(
                f"{NGROK_URL}/",
                json={"prompt": prompt}
            )

async def generate(ctx, *, prompt):
    try:
        response = await get_photo(prompt)

        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'success':
                #將 base64 轉回圖片
                image_data = base64.b64decode(data['image'])
                im = BytesIO(image_data)
                
                # 發送圖片
                file = await ctx.author.send(file = discord.File(im, filename='generated_image.png'))
                url = file.attachments[0].url
                # await file.delete()
                return url
            else:
                print("生成圖片時發生錯誤")
                return ""
        else:
            print("API 請求失敗")
            return ""
            
    except Exception as e:
        print(f"發生錯誤: {str(e)}")
        return ""


import google.generativeai as genai

# 填入你的 gemini 的 API key
GEMINI_API_KEY = "AIzaSyAJtRZ4wAAq7cP0k3vL5v4u9G5n5U5RArg"

# 啟動 gemini
genai.configure(api_key=GEMINI_API_KEY)

# 設定模型
model = genai.GenerativeModel('gemini-2.0-flash')

def gemini(arg):
    response = model.generate_content(arg)
    text = response.text
    text = text.split("[")
    text = text[1].split("]")
    text = "[" + text[0] + "]"
    print(text)
    if not text:
        return ""

    return text

def generate_character():
    context = "在一個古老的新手小鎮裡，勇者踏上了征途，他遇到了三位角色"
    character = [{'name': '小丑', 'say': '吧啦布布吧啦布布', 'emoji': '🤹'}, {'name': '農夫', 'say': '農農 農', 'emoji': '👨‍🌾'}, {'name': '法師', 'say': '命運般的邂逅是世界選擇的結果，吾正期盼著遇到你們這樣的人', 'emoji': '🧙‍♂️'}]
    prompt = f"給我三個角色的描述，背景是「{context}」，三個資料用「,」隔開表示不同筆資料，不要多```python```這種東西，並全部用「[]」包起來，不要回答我任何口語化的文字，單純用 python 的 dict 格式回答，要求格式如下： {str(character)}"
    
    return gemini(prompt)

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    if reaction.message == bot.message_wait_reaction:
        if reaction.emoji not in bot.choices: 
            return
        # 創建 Webhook
        webhook = await reaction.message.channel.create_webhook(name="RPG_Webhook")
        
        chosen_index = bot.choices.index(reaction.emoji)

        async def Talk():
            await webhook.send(bot.characters_info[chosen_index]['say'], username=bot.characters_info[chosen_index]['name'], avatar_url=bot.characters_info[chosen_index]['avatar_url'])

        await reaction.message.edit(content=f"你決定跟{bot.characters_info[chosen_index]['name']}搭話")
        await Talk()
        await reaction.message.remove_reaction(reaction.emoji, bot.user)

        if reaction.emoji in bot.left_choices: 
            bot.left_choices.remove(reaction.emoji)
            
        await reaction.message.remove_reaction(reaction.emoji, user)
        await webhook.delete()

        if not bot.left_choices:
            await bot.message_wait_reaction.edit(content="你已經跟所有人搭話完畢")

        return

# 啟動機器人（請填入你的 Token）
bot.run(token)


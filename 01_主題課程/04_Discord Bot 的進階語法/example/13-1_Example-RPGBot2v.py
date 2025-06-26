import discord

# 設定
DISCORDBOT_TOKEN=""
GEMINI_API_KEY=""
NGROK_URL=""

# 啟用所有 intents，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件，並啟用 intents
bot = discord.Client(intents=intents)

# 用來儲存機器人要等待的訊息
bot.message_wait_reaction = None

# 用來儲存會出現的角色資訊
bot.characters_info = []

# 用來判斷你選了哪個角色
bot.choices = []

# 用來儲存還沒選的角色
bot.left_choices = []

@bot.event
async def on_ready():
    print(f'已登入為 {bot.user}')

@bot.event
async def on_message(message):
    """當收到訊息時觸發的事件"""

    # 忽略機器人訊息
    if message.author.bot:  
        return

    # 使用者輸入 ?start 則執行
    if message.content == "?start":

        # 嘗試生成角色資訊
        # 這裡的 generate_character() 是一個函式，會回傳一個字串，這個字串是用來生成角色資訊的
        try: 
            # 這裡的 eval() 是用來將字串轉換為字典
            bot.characters_info = eval(generate_character())

        # 如果發生錯誤，則印出錯誤訊息
        # 這裡的 Exception 是用來捕捉所有的錯誤
        except Exception as e:
            print(f"發生錯誤: {str(e)}")
            return

        # 生成角色的圖片
        # 這裡的 generate() 是一個函式，會回傳一個字串，這個字串是 byteIO
        for character in bot.characters_info:
            character['avatar_byteIO'] = await generate(ctx=message, prompt=f"給我一個角色的圖，這個角色是「{character['name']}」")

        # 發送訊息並儲存到 bot.message_wait_reaction
        bot.message_wait_reaction = await message.channel.send("好像發生什麼異變了，跟眾人打聽看看吧")

        # 幫 message 添加 choices 中的所有 emoji
        for character in bot.characters_info:
            await bot.message_wait_reaction.add_reaction(character["emoji"])
            bot.choices.append(character["emoji"])
            bot.left_choices.append(character["emoji"])
    

@bot.event
async def on_reaction_add(reaction, user):
    """當使用者點選一個反應時執行"""

    # 忽略機器人的反應
    if user.bot:
        return
    
    # 如果添加反應的訊息，是之前發送的那則訊息
    # 這裡的 bot.message_wait_reaction 是用來儲存機器人之前傳送的訊息
    if reaction.message == bot.message_wait_reaction:

        # 如果不是可選的選項則不理會
        if reaction.emoji not in bot.choices: 
            return
        
        # 創建 Webhook
        buffer = bot.characters_info[bot.choices.index(reaction.emoji)]['avatar_byteIO']
        webhook = await reaction.message.channel.create_webhook(name="RPG_Webhook", avatar=buffer.read())

        # 取得使用者選擇的角色
        chosen_index = bot.choices.index(reaction.emoji)

        # 創建 AI 生成 NPC 要講什麼的函式
        async def Talk():
            await webhook.send(bot.characters_info[chosen_index]['say'], username=bot.characters_info[chosen_index]['name'])

        # 選擇跟某個角色搭話
        await reaction.message.edit(content=f"你決定跟{bot.characters_info[chosen_index]['name']}搭話")
        await Talk()

        # 移除機器人新增的選擇用 emoji
        await reaction.message.remove_reaction(reaction.emoji, bot.user)

        # 如果選擇的 emoji 在 left_choices 中，則從 left_choices 中移除
        if reaction.emoji in bot.left_choices: 
            bot.left_choices.remove(reaction.emoji)
            
        # 移除用戶新增的 emoji
        await reaction.message.remove_reaction(reaction.emoji, user)

        # 移除 webhook
        await webhook.delete()

        # 如果沒有剩下的選擇，代表都對過話了
        if not bot.left_choices:
            await bot.message_wait_reaction.edit(content="你已經跟所有人搭話完畢")

        return

# ============== 生成圖片的函式 ============== #
import requests
import base64
from io import BytesIO

# 用來發送請求到 ngrok 的網址
async def request_photo(prompt) -> requests.Response:
    return requests.post(
                f"{NGROK_URL}/",
                json={"prompt": prompt}
            )

# 用來生成圖片的函式，回傳圖片的網址
async def generate(ctx, *, prompt):
    try:
        response = await request_photo(prompt)

        if response.status_code != 200:
            print("API 請求失敗")
            return ""

        data = response.json()

        if data['status'] != 'success':
            print("生成圖片時發生錯誤")
            return ""
      
        #將 base64 轉回圖片
        image_data = base64.b64decode(data['image'])
        return BytesIO(image_data)                      
    except Exception as e:
         raise e # 暫時不處理錯誤
    
# =========================================== #    

# ============== 生成文字的函式 ============== #

import google.generativeai as genai

# 啟動 gemini
genai.configure(api_key=GEMINI_API_KEY)

# 設定模型
model = genai.GenerativeModel('gemini-2.0-flash')

# 用來發送請求到 gemini 的網址，回傳生成的文字
# 這裡的 arg 是用來生成文字的提示詞( prompt )
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

# 用來生成角色的函式，回傳生成的角色資訊
# 這裡的 context 是用來生成角色的背景
# 這裡的 character 是用來生成角色的提示詞( prompt )
# 這裡的 prompt 是用來生成角色的提示詞( prompt )
def generate_character():
    context = "在一個古老的新手小鎮裡，勇者踏上了征途，他遇到了三位角色"
    character = [{'name': '小丑', 'say': '吧啦布布吧啦布布', 'emoji': '🤹'}, {'name': '農夫', 'say': '農農 農', 'emoji': '👨🌾'}, {'name': '法師', 'say': '命運般的邂逅是世界選擇的結果，吾正期盼著遇到你們這樣的人', 'emoji': '🧙♂️'}]
    prompt = f"給我三個角色的描述，背景是「{context}」，三個資料用「,」隔開表示不同筆資料，不要多```python```這種東西，並全部用「[]」包起來，不要回答我任何口語化的文字，單純用 python 的 dict 格式回答，要求格式如下： {str(character)}"
    
    return gemini(prompt)

# =========================================== #

# 啟動機器人（請填入你的 Token）
bot.run(DISCORDBOT_TOKEN)
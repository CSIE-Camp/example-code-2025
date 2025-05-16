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
# 猜大小選項
choices = ["👨‍🌾", "🧙‍♂️", "🤹"]

@bot.event
async def on_ready():
    print(f'已登入為 {bot.user}')

@bot.event
async def on_message(message):
    """當使用者輸入訊息時執行"""
    if message.author.bot:  # 忽略機器人訊息
        return

    if message.content == "?start": # 使用者輸入 ?start 則執行
        bot.message_wait_reaction = await message.channel.send("好像發生什麼異變了，跟眾人打聽看看吧")
        
        for emoji in choices: # 幫 message 添加 choices 中的所有 emoji ("👨‍🌾", "🧙‍♂️", "🤹")
            await bot.message_wait_reaction.add_reaction(emoji)

@bot.event
async def on_reaction_add(reaction, user):
    """當使用者點選一個反應時執行"""
    if user.bot:  # 忽略機器人的反應
        return
    
    if reaction.message == bot.message_wait_reaction: # 如果添加反應的訊息是我們所期待的
        if reaction.emoji not in choices: # 如果不是可選的選項則不理會
            return
        
        # 創建 Webhook
        webhook = await reaction.message.channel.create_webhook(name="RPG_Webhook")
        
        # 創建農夫要講什麼的函式
        async def farmerTalk():
            await webhook.send("農農 農 (魔王與他的部下的施壓讓大家都不敢離開城鎮，但正因如此農作物價格翻了好幾倍，賺翻了賺翻了)", username="農夫", avatar_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIuAJFVA9Gtytzf2Qb8jmcyqvt45ATlT8vaA&s")
        
        # 創建法師要講什麼的函式
        async def wizardTalk():
            await webhook.send("命運般的邂逅是世界選擇的結果，吾正期盼著遇到你們這樣的人", username="法師", avatar_url="https://megapx-assets.dcard.tw/images/d5d489d4-9f71-45ae-b1fc-2f9e9a824da2/1280.jpeg")

        # 創建小丑要講什麼的函式
        async def clownTalk():
            await webhook.send("吧啦布布吧啦布布", username="小丑", avatar_url="https://cdn-icons-png.freepik.com/512/1232/1232570.png")
        
        
        if reaction.emoji == "👨‍🌾": # 選擇跟農夫對話
            await reaction.message.edit(content="你決定跟農夫搭話")
            await farmerTalk()
            await reaction.message.remove_reaction(reaction.emoji, bot.user) # 把 bot 新增的 emoji 移除
            
        elif reaction.emoji == "🧙‍♂️": # 選擇跟法師對話
            await reaction.message.edit(content="你決定跟法師搭話")
            await wizardTalk()
            await reaction.message.remove_reaction(reaction.emoji, bot.user) # 把 bot 新增的 emoji 移除
            
        elif reaction.emoji == "🤹": # 選擇跟小丑對話
            await reaction.message.edit(content="你決定跟小丑搭話")
            await clownTalk()
            await reaction.message.remove_reaction(reaction.emoji, bot.user) # 把 bot 新增的 emoji 移除

        if reaction.emoji in choices: 
            choices.remove(reaction.emoji) # 講過話就不可以再講了
            
        await reaction.message.remove_reaction(reaction.emoji, user) # 把使用者新增的 emoji 移除
        await webhook.delete() # 移除 Webhook

        if not choices: # 如果 choices 為空，代表都對過話了
            await bot.message_wait_reaction.edit(content="你已經跟所有人搭話完畢")

        return
    
# 啟動機器人（請填入你的 Token）
bot.run(token)
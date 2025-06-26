"""
這段程式碼的功能是：

當有人按「👍」，機器人會誇獎他。
當有人按「❌」，機器人會刪掉那則訊息。
** 而且不論訊息有多舊都有效！**
"""

# 引入需要的模組 (像是新增桌遊的擴充)
import discord

# 啟用所有 intents(意圖)，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件 (像是召喚出這隻你的 DC 機器人)
# 並啟用 intents (讓機器人能夠聽到所有事件)
bot = discord.Client(intents=intents)

@bot.event
async def on_raw_reaction_add(payload):
    """on_raw_reaction_add"""
    """這個事件，當使用者按下反應時會觸發""" 
    # 提供這個事件，相當於叫他聽話。
    # 當按下反應時，就是叫他做事。(像是家人叫你做家事)
    # 此事件不論按下反應的訊息有多舊都有效。
    """payload"""
    """此事件需要一個東西，payload"""
    # 叫他做事，要給他做事必須要的東西。(像是家人叫你洗碗，他要給你碗)
    # payload 是一個包含多種 id 的東西。
    # payload 像是菜單，上面有很多菜名，可以跟廚師點菜名得到菜。
    # 我們可以透過 payload 上的 id (菜名)，透過 api(廚師)，獲取到我們想要的東西(菜)，像是 user、reaction、message 等等。
    
    # 透過 payload 上的 id 點菜 
    guild = bot.get_guild(payload.guild_id) # 得到在 哪個伺服器 按下反應
    channel = guild.get_channel(payload.channel_id) # 得到在某伺服器下的 哪個頻道 按下反應
    message = await channel.fetch_message(payload.message_id) # 得到在某頻道下的 哪個訊息 按下反應
    user = guild.get_member(payload.user_id) # 得到在某伺服器下的 哪個使用者 按下反應
    reaction = payload.emoji # 得到按下的反應

    # 如果按 👍，則發送訊息，說按下讚的人很棒
    if reaction.name == "👍":  
        await channel.send(f"{user.name} 很棒")

    # 如果按 ❌，則移除訊息
    elif reaction.name == "❌":
        await message.delete()

# 執行機器人
# token 請填入你的機器人 token
bot.run(token)
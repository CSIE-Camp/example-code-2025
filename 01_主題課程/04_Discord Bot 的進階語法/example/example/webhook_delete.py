"""
這段程式碼的功能是：

創建一個 webhook，並使用這個 webhook 發送訊息。
發送訊息後，刪除這個 webhook，避免超過 Discord 的 webhook 數量限制。
"""

# 引入需要的模組 (像是新增桌遊的擴充)
import discord

# 啟用所有 intents(意圖)，使機器人能夠監聽所有事件（包括成員、訊息、反應等）
intents = discord.Intents.all()
# 建立 Discord Client 物件 (像是召喚出這隻你的 DC 機器人)
# 並啟用 intents (讓機器人能夠聽到所有事件)
bot = discord.Client(intents=intents)

@bot.event
async def on_message(message):
    """當收到訊息時觸發的事件"""

    # 如果訊息是以 ?webhook 開頭
    if message.content == "?webhook":

        # 檢查機器人是否有管理 Webhook 的權限
        # 如果沒有，則發送訊息告訴使用者
        if not message.channel.permissions_for(message.guild.me).manage_webhooks:
            await message.channel.send("我沒有管理 Webhook 的權限啦=v=")
            return
        
        # 創建一個 Webhook
        # name 是 Webhook 的名稱，avetar_url 是 Webhook 的頭像
        webhook = await message.channel.create_webhook(name="AutoWebhook")

        # 使用 Webhook 發送訊息
        await webhook.send("創建成功", username="HeHe")

        # ========== 刪除 Webhook ========== #
        await webhook.delete()
        # ================================== #

# 執行機器人
# token 請填入你的機器人 token
bot.run(token)
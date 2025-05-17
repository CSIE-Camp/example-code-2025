"""
這段程式碼的功能是：

透過 url 取得 Discord webhook 的物件，
使用這個 webhook 發送訊息到此物件所在的頻道。
"""

# 引入需要的模組 (像是新增桌遊的擴充)
import discord

# 從 Discord 的 webhook 頁面取得的 webhook_url
webhook_url = "https://discord.com/api/webhooks/1373329862214946968/Mta6emxGadCW8zj0xrkogV1sviqaTxfvfH_yLA7y-xa9QvC_91y5ti-79rZJyCkCok4O"

# 透過 url 取得 Discord webhook 的物件
webhook = discord.SyncWebhook.from_url(webhook_url)

# 使用這個 webhook 發送訊息到此 webhook 所在的頻道
webhook.send(
    content = "Never gonna give you up", 
    username = "Rick", 
    avatar_url = "https://i1.sndcdn.com/artworks-x8zI2HVC2pnkK7F5-4xKLyA-t1080x1080.jpg"
)
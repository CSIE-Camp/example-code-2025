import discord
import asyncio

from discord.ext import commands

dc_token = 'dc_token'  # 請填入你的 Discord Bot Token

# intents 為機器人的權限，這裡設定為全開
intents = discord.Intents.all()

# bot 是機器人的本體，這邊是設定他前綴，這邊設定為 %
bot = commands.Bot(command_prefix='%', intents=intents, enable_cache=True)

# event
@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

# 當機器人加入伺服器時
@bot.event
async def on_guild_join(guild):
    print(f"加入伺服器: {guild.name} (ID: {guild.id})")

# 當機器人離開伺服器時
@bot.event
async def on_guild_remove(guild):
    print(f"離開伺服器: {guild.name} (ID: {guild.id})")

# 當有新成員加入時
@bot.event
async def on_member_join(member):
    # print -> 顯示在終端機
    print(f"{member.name} 加入了伺服器 {member.guild.name} (ID: {member.guild.id})")
    # await member.guild.system_channel.send -> 發送訊息到伺服器的系統頻道
    await member.guild.system_channel.send(f"{member.name} 加入了伺服器 {member.guild.name} (ID: {member.guild.id})")

# 當有新成員離開時
@bot.event
async def on_member_remove(member):
    # print -> 顯示在終端機
    print(f"{member.name} 離開了伺服器 {member.guild.name} (ID: {member.guild.id})")
    # await member.guild.system_channel.send -> 發送訊息到伺服器的系統頻道
    await member.guild.system_channel.send(f"{member.name} 離開了伺服器 {member.guild.name} (ID: {member.guild.id})")

@bot.event
async def on_message(message):
    # 機器人不回覆自己的訊息
    if message.author == bot.user:
        return
    # print -> 顯示在終端機
    print(f"收到訊息: {message.content} (來自: {message.author.name})")
    # await message.channel.send -> 發送訊息到頻道
    await message.channel.send(f"收到訊息: {message.content} (來自: {message.author.name})")

@bot.event
async def on_message_edit(before, after):
    # 機器人不回覆自己的訊息
    if after.author == bot.user:
        return
    # print -> 顯示在終端機
    print(f"訊息編輯: {before.content} -> {after.content} (來自: {after.author.name})")
    # await after.channel.send -> 發送訊息到頻道
    await after.channel.send(f"訊息編輯: {before.content} -> {after.content} (來自: {after.author.name})")

@bot.event
async def on_message_delete(message):
    # 機器人不回覆自己的訊息
    if message.author == bot.user:
        return
    # print -> 顯示在終端機
    print(f"訊息被刪除: {message.content} (來自: {message.author.name})")
    # await message.channel.send -> 發送訊息到頻道
    await message.channel.send(f"訊息被刪除: {message.content} (來自: {message.author.name})")

@bot.event
async def on_reaction_add(reaction, user):
    # print -> 顯示在終端機
    print(f"{user.name} 在訊息 {reaction.message.id} 上添加了反應: {reaction.emoji}")
    # await reaction.message.channel.send -> 發送訊息到頻道
    await reaction.message.channel.send(f"{user.name} 在訊息 {reaction.message.id} 上添加了反應: {reaction.emoji}")

@bot.event
async def on_reaction_remove(reaction, user):
    # print -> 顯示在終端機
    print(f"{user.name} 在訊息 {reaction.message.id} 上移除了反應: {reaction.emoji}")
    # await reaction.message.channel.send -> 發送訊息到頻道
    await reaction.message.channel.send(f"{user.name} 在訊息 {reaction.message.id} 上移除了反應: {reaction.emoji}")

async def main():
    await bot.start(dc_token)

asyncio.run(main())
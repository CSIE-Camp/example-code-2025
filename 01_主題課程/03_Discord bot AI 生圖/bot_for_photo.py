import discord
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$',intents=intents) # We need to type '$' before we make a command

@bot.command()
async def web(ctx):

@bot.command()
async def local(ctx):

@bot.command()
async def web_em(ctx):
    #code by website：https://cog-creators.github.io/discord-embed-sandbox/

bot.run('') # 請替換成您的 token

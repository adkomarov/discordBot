import discord
from discord.ext import commands
from mylibs import confidenc
from mylibs import mycolors
import os
import requests
import asyncio
import time

#import json
#import youtube_dl
#import ffmpeg
#from Cybernator import Paginator
#from discord import Member

from discord_together import DiscordTogether

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=confidenc.config['prefix'], 
            intents=discord.Intents.all() # ВНИМАНИЕ: теперь обязательно надо вводить параметр intents.
                                              # Если Вы не знаете, что это такое - введите, как у меня.
        )
    '''
    async def setup_hook(self): # Подлючение когов.
        for ext in cog_list:
            await self.load_extension(ext)
    '''  
    async def on_ready(self):
        print(f"{bot.user} запущен!")
bot = MyBot()
#bot = commands.Bot(intents=discord.Intents.all())
together_client = DiscordTogether(bot)

cog_list = [
    "cogs.admin", # Точка заменяет нам '/', поэтому '.py' в конце писать не надо.
    "cogs.cogtest"
    ]

@bot.is_owner
@bot.command(name="load",
             brief="load cog",
             usage="load <cog>",
             description ='load cog file , warning',
             hidden = True)
async def load(ctx, extension):
    await bot.load_extension(f'cogs.{extension}')
    print('load')
    
@bot.is_owner
@bot.command(name="unload",
             brief="unload cog",
             usage="unload <cog>",
             description ='unload cog file , warning',
             hidden = True)
async def unload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    print('unload')
    
@bot.is_owner
@bot.command(name="reload",
             brief="reload cog",
             usage="reload <cog>",
             description ='reload cog file , warning',
             hidden = True)
async def reload(ctx, extension):
    await bot.unload_extension(f'cogs.{extension}')
    await bot.load_extension(f'cogs.{extension}')
    print('reload.{extension}')
   
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")
            
async def main():
    async with bot:
        await load_extensions()
        await bot.start(confidenc.config['token'])

asyncio.run(main())

#bot.run(confidenc.config['token'])

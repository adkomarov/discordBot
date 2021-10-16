import discord
#from discord import Member
from discord.ext import commands
#from discord.ext.commands import Bot
#from discord.ext.commands import has_permissions
#from discord.utils import get
from Cybernator import Paginator
from mylibs import confidenc
from mylibs import mycolors
import os
import json
import requests
import asyncio
#import youtube_dl
#import ffmpeg
bot = commands.Bot(command_prefix = confidenc.config['prefix'],intents=discord.Intents.all(),)

@bot.is_owner
@bot.command(name="load",
             brief="load cog",
             usage="load <cog>",
             description ='load cog file , warning',
             hidden = True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print('load')
    
@bot.is_owner
@bot.command(name="unload",
             brief="unload cog",
             usage="unload <cog>",
             description ='unload cog file , warning',
             hidden = True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print('unload')
    
@bot.is_owner
@bot.command(name="reload",
             brief="reload cog",
             usage="reload <cog>",
             description ='reload cog file , warning',
             hidden = True)
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print('reload{extension}')
    
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
    else:
       print(f'Unable to load {filename[:-3]}')
bot.run(confidenc.config['token'])

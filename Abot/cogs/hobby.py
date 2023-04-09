#from mylibs import confidenc as bt

#from mylibs import confidenc
import json
import requests
import discord
from discord.ext import commands
import random
from discord_together import DiscordTogether
#bot = commands.Bot(command_prefix = ['='],intents=discord.Intents.all())
#together_client =DiscordTogether('ODE0NDc4NDM4MDM4ODk2Njky.YDecJw.co6Eg-Imi3zRugN9qWyW_Q4ZcwA')
mytokenhash='ODE0NDc4NDM4MDM4ODk2Njky.YDecJw.co6Eg-Imi3zRugN9qWyW_Q4ZcwA'
#DiscordTogether


#together_client = DiscordTogether(bot)
class Group(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.guild_only()    
    @commands.Cog.listener()
    async def on_ready(self):
        self.togetherControl = await DiscordTogether(mytokenhash) 
        # Remember to only use this if you haven't already made a bot variable for `togetherControl` in your bot.py file.
        # If you have already declared a bot variable for it, you can use `self.client.togetherControl` to access it's functions
       
    @commands.guild_only()
    @commands.command()
    async def yt(self, ctx):
        global together_client
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
        await ctx.send(f"!\n{link}")

    @commands.guild_only()
    @commands.command()
    async def poker(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'poker')
        await ctx.send(f"!\n{link}")

    @commands.guild_only()
    @commands.command()
    async def chess(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'chess')
        await ctx.send(f"!\n{link}")

    @commands.guild_only()
    @commands.command()
    async def fishing(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')
        await ctx.send(f"!\n{link}")

    @commands.guild_only()
    @commands.command()
    async def betrayal(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal')
        await ctx.send(f"!\n{link}")

    @commands.guild_only()
    @commands.command()
    async def lettertile(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'letter-tile')
        await ctx.send(f"!\n{link}")

    @commands.guild_only()
    @commands.command()
    async def wordsnack(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'word-snack')
        await ctx.send(f"!\n{link}")

    @commands.guild_only()
    @commands.command()
    async def doodlecrew(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'doodle-crew')
        await ctx.send(f"!\n{link}")

    @commands.guild_only()
    @commands.command()
    async def start(self, ctx):
        # Here we consider that the user is already in a VC accessible to the bot.
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
        await ctx.send(f"Click the blue link!\n{link}")
       
async def setup(bot: commands.Bot):
   await bot.add_cog(Group(bot))
#activity = {
#    "Youtube Together": "755600276941176913"
#    "Betrayal.io": "773336526917861400"
#    "Fishington.io": "814288819477020702"
#    "Poker Night": "755827207812677713"
#    "Chess": "832012774040141894"
#    }
print('Group')

'''
    @commands.event
    async def on_ready():
        commands.togetherControl = await DiscordTogether("BOT_TOKEN_HERE")
        print('Bot is online!')
'''

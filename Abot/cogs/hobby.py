from Abot import confidenc as bt
import json
import requests
import discord
from discord.ext import commands
import random
class Hobby(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command(name="gl",
                      brief="gl on activity",
                      usage="=gl <number hobby>",
                      description = 'generated link activity')
    async def gl(self, ctx, act = 0):
        if act == 0:
            c = random.randint(1,5)
            if c == 1:
                a = {"b":"755600276941176913"}#YT
            elif c == 2:
                a = {"b":"773336526917861400"}#BI
            elif c == 3:
                a = {"b":"814288819477020702"}#FI
            elif c == 4:
                a = {"b":"755827207812677713"}#PN
            else:
                a = {"b":"832012774040141894"}#CS
        elif act == 1:
            a = {"b":"755600276941176913"}#YT
        elif act == 2:
            a = {"b":"773336526917861400"}#BI
        elif act == 3:
            a = {"b":"814288819477020702"}#FI
        elif act == 4:
            a = {"b":"755827207812677713"}#PN
        else:
            a = {"b":"832012774040141894"}#CS
        data = {
            "max_age": 3600,
            "max_uses": 7,
            "target_application_id": a["b"],
            "target_type": 2,
            "temporary": True,
            "validate": None
            }
        headers = {
            "Authorization": "Bot" + ' ' + bt.config['token'],
            "Content-Type": "application/json"
            }
        if ctx.author.voice is not None:
            if ctx.author.voice.channel is not None:
                channel = ctx.author.voice.channel.id
            else:
                await ctx.send("Go to the voice channel")
        else:
            await ctx.send("Go to the voice channel")
        response = requests.post(f"https://discord.com/api/v8/channels/{channel}/invites", data=json.dumps(data), headers=headers)
        link = json.loads(response.content)
        await ctx.send(f"https://discord.com/invite/{link['code']}")

    @commands.command(usage='test <member>',
                      hidden = True)
    async def test(self, ctx, member: discord.Member):
        print(member)
       
def setup(bot: commands.Bot):
   bot.add_cog(Hobby(bot))
#activity = {
#    "Youtube Together": "755600276941176913"
#    "Betrayal.io": "773336526917861400"
#    "Fishington.io": "814288819477020702"
#    "Poker Night": "755827207812677713"
#    "Chess": "832012774040141894"
#    }
print('Hobby cog')

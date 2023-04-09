import discord
from discord.ext import commands

class Process(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game(name="CHARGE YOUR IDEA", type=3)
        await self.bot.change_presence(status=discord.Status.idle,activity=activity) 
        print('BOT ONLINE')
    
async def setup(bot: commands.Bot):
   await bot.add_cog(Process(bot))
print('Process cog')

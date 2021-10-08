import discord
from discord.ext import commands
import time

class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="avatar",
                      brief= 'avatar user',
                      usage='=avatar @Member')
    async def avatar(self, ctx, member : discord.Member = None):
      user = ctx.message.author if (member == None) else member
      embed = discord.Embed(title=f'Аватар пользователя {user}',colour = discord.Color.green())
      embed.set_image(url=user.avatar_url)
      await ctx.send(embed=embed)

    @commands.command(name="ping",
                      brief= 'ping user')
    async def ping(self, ctx: commands.Context):
        start_time = time.time()
        await ctx.send('Testing...')
        end_time = time.time()
        await ctx.send(content=f"USER:{round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")

def setup(bot):
    bot.add_cog(Member(bot))
print('Member cog')

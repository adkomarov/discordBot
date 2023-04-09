import discord
from discord.ext import commands
import time
#import asyncio

class Admin(commands.Cog):
   def __init__(self, bot: commands.Bot):
      self.bot = bot

   @commands.guild_only()
   @commands.has_permissions(manage_messages=True)
   @commands.command(name="clear",
                     brief="Clearing messages.",
                     usage="clear <amount>",
                     description = 'clear message(none) in chat')
   async def clear(self, ctx: commands.Context, amount=70):
      await ctx.channel.purge(limit=amount)
      emb = discord.Embed(title = 'Clearing.',colour = discord.Color.green())
      emb.add_field(name= amount ,value='Message cleared.')
      await ctx.send(embed = emb)

   @commands.guild_only()
   @commands.has_permissions(manage_messages=True)
   @commands.command(name="mute",
                     brief="Give member mute role.",
                     usage="mute <@member>",
                     description = 'Give member mute role forever')
   async def mute(self, ctx, member: discord.Member):
      await member.add_roles(discord.utils.get(member.guild.roles, name='mute'))
      emb = discord.Embed(title = 'Member mute.',colour = discord.Color.green())
      await ctx.send(embed = emb)

   muted = ('mute')
   @commands.guild_only()
   @commands.has_permissions(manage_messages=True)
   @commands.command(name="timemute",
                     brief="Give member timemute role.",
                     usage="timemute <@member> <time(minute)>",
                     description = 'Give member mute role time')
   async def timemute(self, ctx, member: discord.Member = None, time: int = None, reason = None ):
	   mute_role = discord.utils.get( ctx.message.guild.roles, name = muted )
	   if member is None:
		   await ctx.send(embed = discord.Embed(description = f'{ ctx.author.name }, **Be sure to specify (@S1nys example) member!**', color = 0x4f4db3 ))
		   await ctx.message.add_reaction( '❌' )
	   else:
		   if time is None:
			   await ctx.send(embed = discord.Embed(description = f'{ ctx.author.name }, **Be sure to specify the time (minutes)!**', color = 0x4f4db3 ))
			   await ctx.message.add_reaction( '❌' )
		   else:
			   if mute_role is None:
				   await ctx.send(embed = discord.Embed(description = f'{ ctx.author.name }, **Be sure to create a (@mute) role!**', color = 0x4f4db3 ))
				   await ctx.message.add_reaction( '❌' )
			   else:
				   await member.add_roles(mute_role, reason = reason, atomic = True)
				   await ctx.message.add_reaction( '✅' )
				   await asyncio.sleep(time * 60)
				   await member.remove_roles(mute_role)

   @commands.guild_only()
   @commands.has_permissions(kick_members=True)
   @commands.command(name="kick",
                     brief="Kick member.",
                     usage="kick <@member>",
                     description = 'kick member into guild')
   async def kick(self, ctx, member: discord.Member, *, reason=None):
      await ctx.message.delete(delay=1) # Если желаете удалять сообщение после отправки с задержкой
      await member.send(f"You was kicked from server") # Отправить личное сообщение пользователю
      await ctx.send(f"Member {member.mention} was kicked from this server!")
      await member.kick(reason=reason)

   @commands.guild_only()
   @commands.has_permissions(ban_members=True)
   @commands.command(name="ban",
                     brief="Ban member.",
                     usage="ban <@user>",
                     description = 'Ban member forever')
   async def ban(self, ctx, member: discord.Member, *, reason=None):
      await member.send(f"You was banned on server") # Отправить личное сообщение пользователю
      await ctx.send(f"Member {member.mention} was banned on this server")
      await member.ban(reason=reason)

async def setup(bot: commands.Bot): # Подключение кога.
    await bot.add_cog(Admin(bot))
print('Admin cog')

import discord
from discord.ext import commands
import time
import ast
import cval
import requests

api_key = "68eb2a500652f874d422103886c7a7ab"

def rpl(x:str):
    x=str(x)
    x = x.replace('(', '')
    x = x.replace(')', '')
    x = x.replace('[', '')
    x = x.replace(']', '')
    x = x.replace("'", '')
    x = x.replace(",", '')
    return(x)

def get_wind_direction(deg):
    l = ['С ','СВ',' В','ЮВ','Ю ','ЮЗ',' З','СЗ']
    for i in range(0,8):
        step = 45.
        min = i*step - 45/2.
        max = i*step + 45/2.
        if i == 0 and deg > 360-45/2.:
            deg = deg - 360
        if deg >= min and deg <= max:
            res = l[i]
            break
    return res

def request_forecast(s_city_name):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'q': s_city_name,'units': 'metric', 'lang': 'ru', 'APPID': api_key})#'id': city_id,
        data = res.json()
        print('city:', data['city']['name'], data['city']['country'])
        for i in data['list']:
            print( (i['dt_txt'])[:16], '{0:+3.0f}'.format(i['main']['temp']),
                   '{0:2.0f}'.format(i['wind']['speed']) + " м/с",
                   get_wind_direction(i['wind']['deg']),
                   i['weather'][0]['description'] )
    except Exception as e:
        print("Exception (forecast):", e)
        pass

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
        end_time = time.time()
        await ctx.send(content=f"USER:{round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")
        
    @commands.command(name="code",
                      brief= 'input code')
    async def code(self, ctx,*,selfcode):
        selfcode=str(selfcode)
        coderesult=cval.cval(source=selfcode,calls=False,
                        globals=globals(),gscope=False,
                        locals=locals(),lscope=False,modules=False,)#modules=False,
        coderesult=str(coderesult)
        await ctx.send(content=coderesult)

    @commands.command(name="rain")
    async def rain(self, ctx,*,cname):
        try:
            weth=[]
            res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'q': cname,'units': 'metric', 'lang': 'ru', 'APPID': api_key})#'id': city_id,
            data = res.json()
            w=('city:', data['city']['name'], data['city']['country'])
            w=str(w)
            w=rpl(w)
            #await ctx.send(content=w)
            for i in data['list']:
                e=((i['dt_txt'])[:16], '{0:+3.0f}'.format(i['main']['temp']),
                   '{0:2.0f}'.format(i['wind']['speed']) + " м/с",
                   get_wind_direction(i['wind']['deg']),
                   i['weather'][0]['description'])
                e=str(e)
                e=rpl(e)
                weth.append(e)
            emb1 = discord.Embed(title=w,colour = discord.Color.blue())
            for i in range(0,8):
                emb1.add_field(name=weth[i][0:17],value=weth[i][17:], inline=False)#value=new1,
            await ctx.send(embed=emb1)
            emb1 = discord.Embed(title=w,colour = discord.Color.blue())
            for i in range(9,16):
                emb1.add_field(name=weth[i][0:17],value=weth[i][17:], inline=False)#value=new1,
            await ctx.send(embed=emb1)
            for i in range(17,24):
                emb1.add_field(name=weth[i][0:17],value=weth[i][17:], inline=False)#value=new1,
            await ctx.send(embed=emb1)
            emb2 = discord.Embed(title=w,colour = discord.Color.blue())
            for i in range(25,32):
                emb1.add_field(name=weth[i][0:17],value=weth[i][17:], inline=False)#value=new1,
            await ctx.send(embed=emb1)
            emb1 = discord.Embed(title=w,colour = discord.Color.blue())
            for i in range(33,40):
                emb1.add_field(name=weth[i][0:17],value=weth[i][17:], inline=False)#value=new1,
            await ctx.send(embed=emb1)       
                #await ctx.send(content=e)
        except Exception as e:
            print("Exception (forecast):", e)
            pass
        
#        result=str(request_forecast(name))
#        await ctx.send(content=result)

#68eb2a500652f874d422103886c7a7ab

        

async def setup(bot):
    await bot.add_cog(Member(bot))
print('Member cog')

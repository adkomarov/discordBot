import discord
from discord.ext import commands
import requests
import wikipedia
from bs4 import BeautifulSoup
import deepl

def FormingRequestLink(BrowserLink:str,UserRequest:str):
    UserRequest = UserRequest.replace(' ', '+')
    FinalUrl = BrowserLink + UserRequest
    return FinalUrl

def FormingPopularBrowserLink(q,w:list):
    for i in range(len(q)-1):
        if q[i]=='yandex':
            w.append('https://www.'+q[i]+'.ru/text?q=')
        else:
            w.append('https://www.'+q[i]+'.ru/search?q=')

class Education(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.command(name="f",
                      brief="find",
                      usage="f {word}+{word} (etc.)",
                      description = 'Browser link')
    async def f(self, ctx,*,UserRequest):
        BrowserLink=['google','yandex','go.mail'];PopularBrowserLink=[];FormedLink=[];FormedAttachments=[]
        FormingPopularBrowserLink(BrowserLink,PopularBrowserLink)
        TitlePopularBrowser=['Google','Yandex','Mail']
        MainColour=discord.Color.green()
        for i in range(len(BrowserLink)-1):
            FormedLink.append(FormingRequestLink(PopularBrowserLink[i],UserRequest))
            del PopularBrowserLink;del UserRequest
            FormedAttachments.append(discord.Embed(title=TitlePopularBrowser[i],colour = MainColour,url=FormedLink[i]))
            del TitlePopularBrowser;del MainColour;del FormedLink
            await ctx.send(embed=FormedAttachments[i])

    @commands.command(name="wiki",
                      brief="wikipedia",
                      usage="wiki {word} {word} (etc.)",
                      description = 'Browser link')
    async def wiki(self, ctx,lan,sent,*,ser):
        wikipedia.set_lang(lan)
        search=ser
        ser=ser.replace(' ','_')
        url1='https://ru.wikipedia.org/wiki/'+ser
        emb1 = discord.Embed(title='Wiki',colour = discord.Color.green())
        emb1.add_field(name=ser, value=wikipedia.summary(search,sentences=sent), inline=True)
        emb2 = discord.Embed(title='Etc?',colour = discord.Color.green(),url=url1)
        await ctx.send(embed=emb1)
        await ctx.send(embed=emb2)
            
    @commands.command(name="art",
                      brief="translator",
                      usage="art {source} {required} {formality_tone} {text}",
                      description = 'Deepl translator')
    async def art(self, ctx,source,target,*,resp):
        responce = deepl.translate(source_language=source,
                target_language=target,
                text=resp,
                formality_tone="informal")# text="formality_tone="informal")
        responce1 = deepl.translate(source_language=target,
                target_language=source,
                text=responce,
                formality_tone="informal")
        title1 = source +' -> '+ target
        title2 = target +' -> '+ source
        url1='https://www.deepl.com/en/translator'
        emb1 = discord.Embed(title=title1,colour = discord.Color.green())
        emb1.add_field(name=target, value=responce, inline=True)
        emb2 = discord.Embed(title=title2,colour = discord.Color.green())
        emb2.add_field(name=target, value=responce1, inline=True)
        emb3 = discord.Embed(title='Etc?',colour = discord.Color.green(),url=url1)
        await ctx.send(embed=emb1)
        await ctx.send(embed=emb2)

async def setup(bot: commands.Bot): # Подключение кога.
    await bot.add_cog(Education(bot))
print('educ cog')

'''
def get_html(url):
    response = requests.get(url)#Запрос страницы
    return response.text# Возвращение HTML кода
'''
'''
def get_ynews(html):
    soup = BeautifulSoup(html, 'lxml')
    spans = soup.find('ol', class_='news__list').findAll('span', class_='news__item-content') #Поиск первых четрыех строк
    span_last = soup.find('ol', class_='news__animation-list').find('span', class_='news__item-content') #Поиск пятой анимированной строки
    news = []
    for s in spans:
        news.append(s.get_text())
    news.append(span_last.get_text())
    return news
'''
'''
def get_mnews(html):
    soup = BeautifulSoup(html, 'lxml')
    spans = soup.find('ol', class_='news-visited').findAll('span', class_='svelte-1pm37ss') #Поиск первых четырех строк  
    news = []
    for s in spans:
        news.append(s.get_text())
    news.append(span_last.get_text())
    return news
#news-visited svelte-1pm37ss
'''
'''
@commands.command(name="news",
                      brief="news.",
                      usage="news",
                      description = 'embed message news')
    async def news(self, ctx):
        url1 = 'https://yandex.ru/'
#        url2 = 'https://www.go.mail.ru/'
        all_news1 = get_ynews(get_html(url1))
#        all_news2 = get_mnews(get_html(url1))
        for line in all_news1[0:1]:
            new1=(line+'\n')
        for line in all_news1[1:2]:
            new2=(line+'\n')
        for line in all_news1[2:3]:
            new3=(line+'\n')
        for line in all_news1[3:4]:
            new4=(line+'\n')
        for line in all_news1[4:5]:
            new5=(line+'\n')
        emb1 = discord.Embed(title="Russian's news(yandex)",colour = discord.Color.green())
        emb1.add_field(name="Yandex:",value=new1, inline=False)
        emb1.add_field(name="Yandex:",value=new2, inline=False)
        emb1.add_field(name="Yandex:",value=new3, inline=False)
        emb1.add_field(name="Yandex:",value=new4, inline=False)
        emb1.add_field(name="Yandex:",value=new5, inline=False)
#        emb1.add_field(name="Mail:",value=new6, inline=False)
        await ctx.send(embed=emb1)
        print('y')
'''

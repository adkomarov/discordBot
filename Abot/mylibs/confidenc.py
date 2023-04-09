config = {
    'token': 'ODE0NDc4NDM4MDM4ODk2Njky.GBNjEA.qIQ4m3yipkqHAQUSRcBdbht5wJb3m43LO-9QJY',
    'bot': 'IDEA',
    'id': 814478438038896692,#BOT
    'prefix': '='
}
# This example requires the 'message_content' intent.
'''
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('ODE0NDc4NDM4MDM4ODk2Njky.GBNjEA.qIQ4m3yipkqHAQUSRcBdbht5wJb3m43LO-9QJY')
'''

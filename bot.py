import discord
import requests
import json

def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))
#this block of code is going to interact with the discord API when certain events happen 


    async def on_message(self, message):
        # method in our class that allows our bot to respond to string given in the channel
        if message.author == self.user:
            return
        # makes sure the the bot doesnt talk to itself and is only responding to users that are putting in an input into the chat
        if message.content.startswith('$hello'):
            await message.channel.send("What's Up Budday Budday!!!")
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())


intents = discord.Intents.default()
intents.message_content = True
# intents are the things that our discord bot will be looking out for
# we explicitly allowed it to interact with messages

Client = MyClient(intents=intents)
Client.run('MTA3OTgzNTEyMjg5NzAxNDg5NQ.GyMQm8.C4w6vjBb8-sVk368COUru5V6XN5LnAgd1SuiHU') #replace with a token of my choosing
# Calling the client and running it
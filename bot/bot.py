import os 
import discord
import openai
from dotenv import load_dotenv
# from app.chatgpt_ai.openai import chatgpt_response

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

openai.api_key = OPENAI_KEY

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user in message.mentions:
    
        response = openai.Completion.create(
            engine ="text-davinci-003",
            prompt = f"{message.content}",
            max_tokens = 2048,
            temperature = 0.5,
        )
    
    
    await message.channel.send(response.choices[0].text)
    
# starting the bot
client.run(TOKEN)

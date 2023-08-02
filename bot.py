import discord
import responses
import json
from discord.ext import commands

f = open('config.json')
config = json.load(f)
token = str(config['token'])
prefix = str(config['prefix'])

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await bot.change_presence(activity=discord.Game(name='!elvedin'))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel.name)

    print(f'{username} said: {user_message} ({channel})')

    if user_message.startswith(prefix):
        user_message = user_message[len(prefix):]
        await send_message(message, user_message, is_private=False)

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

bot.run(token)

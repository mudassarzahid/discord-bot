import discord
import logging
from discord.ext import commands

def log_errors:
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

client = discord.Client()
with open('token.txt','r') as f:
    lines = f.readlines()
    TOKEN = lines[0].strip()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


log_errors()
client.run(TOKEN)

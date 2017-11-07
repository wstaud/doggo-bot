import discord
import asyncio
import config

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'Pong!')
    elif message.content.startswith('!good bot'):
        await client.send_message(message.channel, 'Bark!')

client.run(config.token)

import random

@client.event
async def on_message(message):
    if message.content.startswith('!roll-d20'):
        await client.send_message(message.channel, random.randint(1,20))

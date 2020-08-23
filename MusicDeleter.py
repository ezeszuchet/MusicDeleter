# Work with Python 3.6
import discord

TOKEN = 'NzQ2ODUwMTE0NzMwOTgzNTg1.X0GUXw.j47YNT2-Ec3XHqO3yBeLUvcVNFk'

client = discord.Client()

@client.event
async def on_message(message):

    if "-p" in message.content or "-die" in message.content or "-next" in message.content or "-skip" in message.content or "-queue" in message.content or "-loop" in message.content:
        await message.channel.purge(limit=1)

client.run(TOKEN)
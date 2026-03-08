import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot is online: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!ping":
        await message.channel.send("Pong!")

TOKEN = os.getenv("TOKEN")
client.run("TOKEN")

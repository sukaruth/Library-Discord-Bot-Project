import discord

intents = discord.Intents.default()
intents.message_content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("BOT IS RUNNING")


client.run("TOKEN")
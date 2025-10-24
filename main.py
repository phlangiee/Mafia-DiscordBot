import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



client.run(os.getenv('DISCORD_BOT_TOKEN'))
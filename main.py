import discord
import os
from dislash import InteractionClient

# Loads in .env variables
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



client.run(os.getenv('DISCORD_BOT_TOKEN'))
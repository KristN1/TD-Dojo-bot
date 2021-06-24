import discord
import os
from db_actions import Database
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix= ".", intents=intents, case_insensitive=True)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

@client.event
async def on_ready():
    print("Bot is ready")

with open("token.txt","r") as f:
    token = f.read()

client.run(token)
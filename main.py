import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Helo, {bot.user.name}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Try using !h for help")
    else:
        raise error

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
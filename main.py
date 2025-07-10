#+------------------ import section ------------------+
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import utils

#+------------------ bot booting section ------------------+
load_dotenv()

token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

#+------------------ on events ------------------+
@bot.event
async def on_ready():
    print(f"Helo, {bot.user.name}")

@bot.event
async def on_command_error(ctx, error):
    """Handles wrong user input as commands"""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Try using !h for help")
    else:
        raise error

#+------------------ commands ------------------+
@bot.command()
async def h(ctx):
    await ctx.send(utils.help_text)

@bot.command()
async def add(ctx, *, task:str):
    utils.add_task(task=task)
    await ctx.send(f"Added **{task}** to your list")

@bot.command()
async def undone(ctx):
    await ctx.send(utils.get_undone_tasks())

@bot.command()
async def finish(ctx, *, task_id):
    utils.finish_task(utils.get_real_id(task_id))
    await ctx.send(f"Finished task!")

@bot.command()
async def done(ctx):
    await ctx.send(utils.get_done_tasks())

@bot.command()
async def list(ctx):
    await ctx.send(utils.get_all_tasks())

@bot.command()
async def about(ctx):
    ctx.send(utils.about)


#+------------------ run bot ------------------+

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
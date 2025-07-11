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
    print(f"Connected as {bot.user.name}")

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
    user_id = ctx.author.id
    guild_id = ctx.guild.id
    utils.add_task(task=task, user_id=user_id, guild_id=guild_id)
    await ctx.send(f"Added **{task}** to {ctx.author.mention} list")

@bot.command()
async def undone(ctx):
    user_id = ctx.author.id
    guild_id = ctx.guild.id
    await ctx.send(utils.get_undone_tasks(user_id=user_id, guild_id=guild_id))

@bot.command()
async def finish(ctx, *, task_id):
    user_id = ctx.author.id
    guild_id = ctx.guild.id
    utils.finish_task(task_id=task_id, user_id=user_id, guild_id=guild_id)
    await ctx.send(f"Finished task!")

@bot.command()
async def done(ctx):
    user_id = ctx.author.id
    guild_id = ctx.guild.id
    await ctx.send(utils.get_done_tasks(user_id=user_id, guild_id=guild_id))

@bot.command()
async def list(ctx):
    user_id = ctx.author.id
    guild_id = ctx.guild.id
    await ctx.send(utils.get_all_tasks(user_id=user_id, guild_id=guild_id))

@bot.command()
async def about(ctx):
    await ctx.send(utils.about)


#+------------------ run bot ------------------+

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
import os
from dotenv import load_dotenv
from discord.ext import commands
import discord

import RoleRandomiser

role_randomize = RoleRandomiser.role_randomize

load_dotenv()

BOT_KEY = os.getenv('BOT_KEY')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.dm_messages = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def test(ctx):
    await ctx.send('🤏 pp')
    print("Good test")

@bot.command()
async def give_roles(ctx, num: int, *exclude: str):
    role_randomize(num, exclude)
    while user
    users = [user async for user in reaction.users()]


bot.run(BOT_KEY)

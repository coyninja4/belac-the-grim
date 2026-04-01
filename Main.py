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
    print(f"{ctx.author}'s confidence shattered in {ctx.channel}")

@bot.command()
async def give_roles(ctx, *exclude: str):
    print("roles distri")
    #role_randomize(num, exclude)


@bot.command()
async def begone(ctx):
    if ctx.author.id == 571322376491368477:
        await ctx.send('booo 👎')
        quit()
    else:
        await ctx.send(f'{ctx.author} is not worthy')

@bot.command()
async def reactest(ctx):
    await ctx.send("React \"✅\" to join")
    await ctx.reaction_add("✅")
    tracked_message_id = ctx.id
    async def on_reaction_add(reaction, user):


bot.run(BOT_KEY)

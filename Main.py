import os
from dotenv import load_dotenv
from discord.ext import commands
import discord

import RoleRandominterface

RRI = RoleRandominterface

load_dotenv()

BOT_KEY = os.getenv('BOT_KEY')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.dm_messages = True
intents.reactions = True
global queue

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def test(ctx):
    await ctx.send('🤏 pp')
    print(f"{ctx.author}'s confidence shattered in {ctx.channel}")

@bot.command()
async def open_queue(ctx):
    global queue
    queue = set()
    msg = await ctx.send(f"React \"✅\" to join. Remove reaction to leave queue.\nType !game_start to start game.")
    global tracked_message_id
    tracked_message_id = msg.id
    await msg.add_reaction("✅")

@bot.command()
async def game_start(ctx, game, exclusions*):
    RRI.start_game(queue, game, exclusions)
    
@bot.command()
async def begone(ctx):
    if ctx.author.id == 571322376491368477:
        await ctx.send('booo 👎')
        quit()
    else:
        await ctx.send(f'{ctx.author} is not worthy')

@bot.event
async def on_reaction_add(reaction, user):
    global tracked_message_id
    if reaction.message.id == tracked_message_id and user.id != 1488281701867065395:
        if reaction.emoji == "✅":
            queue.add(user.name)
        else:
            pass
    print(queue)

@bot.event
async def on_reaction_remove(reaction, user):
    global tracked_message_id
    if reaction.message.id == tracked_message_id and user.id != 1488281701867065395:
        if reaction.emoji == "✅":
            try:
                queue.remove(user.name)
            except(KeyError):
                pass
    print(queue)

bot.run(BOT_KEY)


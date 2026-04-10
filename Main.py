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
    global queue 
    queue = set()
    msg = await ctx.send(f"Game starting with exclusions: {exclude}\nReact \"✅\" to join. React \"❌\" to leave queue.\nReact \"🃏\" to start game.")
    global tracked_message_id
    tracked_message_id = msg.id
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")
    await msg.add_reaction("🃏")

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
        elif reaction.emoji == "❌":
            try:
                queue.remove(user.name)
            except(KeyError):
                pass
        elif reaction.emoji == "🃏":
            #role_randomize(len(queue), exclusions)
            print("hi")
            tracked_message_id = None
            pass
        else:
            pass
    print(queue)

bot.run(BOT_KEY)

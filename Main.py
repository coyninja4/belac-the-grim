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
    msg = await ctx.send("React \"✅\" to join. React \"❌\" to leave queue.\nReact \"🃏\"")
    global tracked_message_id
    tracked_message_id = msg.id
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")
    await msg.add_reaction("🃏")
    global queue 
    queue = set()

@bot.command()
async def exconfig(ctx):
    global exclusions
    exclusions = []

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message.id == tracked_message_id:
        if reaction.emoji == "✅":
            queue.add(user.name)
        elif reaction.emoji == "🃏":
            role_randomize(len(queue), exclusions)
        else:
            pass
    print(queue)

bot.run(BOT_KEY)

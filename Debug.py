from discord import app_commands
from discord.ext import commands
import discord

class DebugCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sync(self, ctx):
        await ctx.send("Hello!")
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send('🤏 pp')
        print(f"{ctx.author}'s confidence shattered in {ctx.guild}, {ctx.channel}")

    @commands.command()
    async def begone(ctx):
        if ctx.author.id == 571322376491368477:
            await ctx.send('booo 👎')
            quit()
        else:
            await ctx.send(f'{ctx.author} is not worthy')

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
from discord import app_commands
from discord.ext import commands
import discord

class DebugCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sync(self, ctx):
        await ctx.send("sync slash commands")

    @commands.command()
    async def reload(self, ctx, extension: str):
        await commands.reload_extension(extension)
        await ctx.send(f'Reloaded {extension}')
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send('🤏 pp')
        print(f"{ctx.author}'s confidence shattered in {ctx.guild}, {ctx.channel}")

    @commands.command()
    async def begone(self, ctx):
        if ctx.author.id == 571322376491368477:
            await ctx.send('booo 👎')
            quit()
        else:
            await ctx.send(f'{ctx.author} is not worthy')

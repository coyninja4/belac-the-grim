from discord.ext import commands
import discord

async def setup(bot):
    await bot.add_cog(DebugCog(bot))


class DebugCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    @commands.is_owner()
    async def sync(self, ctx):
        await self.bot.tree.sync(guild=ctx.guild)
        await ctx.send("sync slash commands")
        print(f"{ctx.author} synced in {ctx.channel}")

    @commands.hybrid_command()
    async def reload(self, ctx, extension: str):
        await self.bot.reload_extension(extension)
        await ctx.send(f'Reloaded {extension}')
        print(f"{ctx.author} reloaded {extension} in {ctx.channel}")
    
    @commands.hybrid_command()
    async def test(self, ctx):
        await ctx.send('🤏 pp')
        print(f"{ctx.author}'s confidence shattered in {ctx.guild}, {ctx.channel}")

    @commands.hybrid_command()
    async def begone(self, ctx):
        if ctx.author.id == 571322376491368477:
            await ctx.send('booo 👎')
            quit()
        else:
            await ctx.send(f'{ctx.author} is not worthy')

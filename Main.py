import os
from dotenv import load_dotenv
from discord.ext import commands
import discord

import Debug

load_dotenv()

BOT_KEY = os.getenv('BOT_KEY')

class Belac(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.dm_messages = True
        intents.reactions = True
        super().__init__(command_prefix='!', intents=intents)

    async def on_ready(self):
        print(f'We have logged in as {self.user}')
    
    async def setup_hook(self):
        await bot.add_cog(Debug.DebugCog(bot))

    @commands.command()
    async def reload(self, ctx, extension: str):
        await .reload_extension(extension)
        await ctx.send(f'Reloaded {extension}')

bot = Belac()
bot.run(BOT_KEY)
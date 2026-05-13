import os
from dotenv import load_dotenv
from discord.ext import commands
import discord

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
        await bot.load_extension("cog.Debug")
        await bot.load_extension("cog.Game")

bot = Belac()
bot.run(BOT_KEY)
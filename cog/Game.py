from discord import app_commands
from discord.ext import commands
import json

async def setup(bot):
    await bot.add_cog(GameCog(bot))

class GameCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def list_games(self, ctx):
        with open('../games-config.json', 'r') as f:
            JSON = json.load(f)
        string = "Games list: \n"
        for i in JSON["games"]:
            string += f"{i} \n"
        await ctx.send(string)

# @commands.app_command()
# async def openq(ctx, roles_config):
#     global queue
#     queue = set()
#     msg = await ctx.send(f"React \"✅\" to join. Remove reaction to leave queue.\nWhen ready type !game_start followed by the game.")
#     global tracked_message_id
#     tracked_message_id = msg.id
#     await msg.add_reaction("✅")

# @bot.command()
# async def game_start(ctx, *exclusions):
#     players = list()
#     global queue
#     for i in queue:
#         # now that this is going in a class do it properly
#         pass
#     print(f"game started with queue: {players}")
#     queue = set()

# @bot.event
# async def on_reaction_add(reaction, user):
#     global tracked_message_id
#     if reaction.message.id == tracked_message_id and user.id != 1488281701867065395:
#         if reaction.emoji == "✅":
#             queue.add(user.name)
#         else:
#             pass
#     print(queue)

# @bot.event
# async def on_reaction_remove(reaction, user):
#     global tracked_message_id
#     if reaction.message.id == tracked_message_id and user.id != 1488281701867065395:
#         if reaction.emoji == "✅":
#             try:
#                 queue.remove(user.name)
#             except(KeyError):
#                 pass
#     print(queue)
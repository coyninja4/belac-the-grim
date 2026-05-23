from discord import app_commands
from discord.ext import commands
import json
from Role_distri import Role_distri

async def setup(bot):
    await bot.add_cog(GameCog(bot))

class GameCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.games = dict()
    
    @app_commands.command()
    async def list_games(self, interaction):
        with open('games-config.json', 'r') as f:
            JSON = json.load(f)
        string = "Games list: \n"
        for i in JSON["games"]:
            string += f"{i} \n"
        await interaction.response.send_message(string)

    @app_commands.command()
    async def openq(self, interaction):
        self.games[interaction.channel_id] = set()
        msg = await interaction.response.send_message(f"React \"✅\" to join. Remove reaction to leave queue.\nWhen ready type !game_start followed by the game.")
        await msg.add_reaction("✅")

    @app_commands.command()
    async def game_start(self, interaction, roles_config: str, exclusions: str):
        queue = self.games[interaction.channel_id]
        Game = Role_distri(roles_config, queue)
        roles = Game.role_randomize(exclusions)
        for i in queue:
            print(roles[i])
            pass
        print(f"game started with queue: {queue}")
        

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
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
        await interaction.response.send_message(f"React \"✅\" to join. Remove reaction to leave queue.\nWhen ready type !game_start followed by the game.")
        msg = await interaction.original_response()
        self.games[interaction.channel_id] = dict([(msg.id, set())])
        await msg.add_reaction("✅")

    @app_commands.command()
    async def game_start(self, interaction, roles_config: str, exclusions: str = ""):
        queue = self.games[interaction.channel_id]
        Game = Role_distri(roles_config, queue)
        roles = Game.role_randomize(exclusions)
        for i in roles:
            print(roles)
        print(f"game started with queue: {queue}")
        self.games.pop(interaction.channel_id)
        

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.message.channel.id in self.games and user.id != 1488281701867065395:
            queue = self.games[reaction.message.channel.id][reaction.message.id]
            if reaction.message.id in self.games[reaction.message.channel.id]:
                if reaction.emoji == "✅":
                    queue.add(user.name)
                else:
                    pass
            print(queue)

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
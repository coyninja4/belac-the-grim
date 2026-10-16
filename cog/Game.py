from discord import app_commands
from discord.ext import commands
import json
import asyncio
import discord
from Role_distri import Role_distri

async def setup(bot):
    await bot.add_cog(GameCog(bot))

class GameCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.games = {}       # channel_id -> set of user ids
        self.queue_msgs = {}  # message_id -> channel_id

    @app_commands.command(name="list games", description="shows a list of games that can be used in the game_start command")
    async def list_games(self, interaction: discord.Interaction):
        with open('games-config.json', 'r') as f:
            JSON = json.load(f)
        string = "Games list: \n" + "\n".join(JSON["games"])
        await interaction.response.send_message(string)

    @app_commands.command(name="open queue", description="Opens a queue to start a game")
    async def openq(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "React \"✅\" to join. Remove reaction to leave queue.\n"
            "When ready use /game_start followed by the game."
        )
        msg = await interaction.original_response()
        self.games[interaction.channel_id] = set()
        self.queue_msgs[msg.id] = interaction.channel_id
        await msg.add_reaction("✅")

    @app_commands.command(name="game start", description="Starts a game, must have a queue active in the channel to use.")
    async def game_start(self, interaction: discord.Interaction, roles_config: str, exclusions: str = ""):
        await interaction.response.defer()

        queue = self.games.get(interaction.channel_id)
        if not queue:
            await interaction.followup.send("Nobody is in the queue. Use /openq and react first.")
            return

        game = Role_distri(roles_config, queue)
        result = game.role_randomize(exclusions)
        if result is None:
            await interaction.followup.send("Too many exclusions, try again.")
            return
        roles, content = result

        bot_lines = []
        for uid, text in roles.items():
            try:
                user = await self.bot.fetch_user(uid)
                if user.bot:
                    bot_lines.append(f"**{user.name}**\n{text}")
                    continue
                await user.send(text)
            except discord.HTTPException as e:
                await interaction.followup.send(f"Couldn't DM <@{uid}> ({e.code}).")
            await asyncio.sleep(0.3)

        if bot_lines:
            await interaction.followup.send("Test bot roles:\n\n" + "\n\n".join(bot_lines), ephemeral=True)
            
        print(f"game started with queue: {queue}, roles: {content}")
        await interaction.followup.send("Roles in this game: " + ", ".join(content))

        self.games.pop(interaction.channel_id, None)
        for mid in [m for m, c in self.queue_msgs.items() if c == interaction.channel_id]:
            del self.queue_msgs[mid]

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.message_id not in self.queue_msgs:
            return
        if payload.user_id == self.bot.user.id or str(payload.emoji) != "✅":
            return
        self.games[self.queue_msgs[payload.message_id]].add(payload.user_id)
        print(self.games[self.queue_msgs[payload.message_id]])

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        if payload.message_id not in self.queue_msgs:
            return
        if str(payload.emoji) != "✅":
            return
        self.games[self.queue_msgs[payload.message_id]].discard(payload.user_id)
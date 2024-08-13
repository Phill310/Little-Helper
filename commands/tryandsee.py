from discord import app_commands
from discord.ext import commands
import discord
import utils


class TryAndSeeCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @app_commands.command(name="try", description="Try it and see video")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def tryandsee(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            content="Why don't you [try it and see](https://tryitands.ee)",
            ping=reply_to
        )


async def setup(bot):
    await bot.add_cog(TryAndSeeCog(bot=bot))

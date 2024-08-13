from discord import app_commands
from discord.ext import commands
import discord
import utils


class AskCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @app_commands.command(description="Don't ask to ask website")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def ask(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            content="[Don't ask to ask](https://dontasktoask.com) ",
            ping=reply_to
        )


async def setup(bot):
    await bot.add_cog(AskCog(bot=bot))

from discord import app_commands
from discord.ext import commands
import discord

from utils import DeleteButton


class IssuesCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @app_commands.command(description="Links to the Skript issues page")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def issues(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await interaction.response.send_message(
            content="To report a Skript bug or make a suggestion, make a [New Issue](https://github.com/SkriptLang/Skript/issues/new/choose) "
                    + (reply_to.mention if reply_to is not None else ""),
            view=DeleteButton(interaction.user.id)
        )


async def setup(bot):
    await bot.add_cog(IssuesCog(bot=bot))

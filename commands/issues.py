from discord import app_commands
from discord.ext import commands
import discord


class IssuesCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @app_commands.command(description="Links to the Skript issues page")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def issues(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="To report a Skript bug or make a suggestion, make a [New Issue]("
                                                        "https://github.com/SkriptLang/Skript/issues/new/choose)")


async def setup(bot):
    await bot.add_cog(IssuesCog(bot=bot))

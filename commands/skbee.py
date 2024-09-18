from discord import app_commands
from discord.ext import commands
import discord


class SkBeeCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @app_commands.command(description="Explains what happened to SkBee")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def skbee(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        ping = "" if reply_to is None else (reply_to.mention + " ")
        file = discord.File("SkBee-3.6.1.jar")
        await interaction.response.send_message(
            content=ping + "SkBee has been discontinued by its owner. Other addons or forks may exist or be made to "
                           "replace it. In the meantime, the latest SkBee jar is attached below and documentation can "
                           "be found [here](https://web.archive.org/web/20240405064337/https://skripthub.net/docs"
                           "/?addon=SkBee)",
            file=file
        )


async def setup(bot):
    await bot.add_cog(SkBeeCog(bot=bot))

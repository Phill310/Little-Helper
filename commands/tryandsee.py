from discord import app_commands
from discord.ext import commands
import discord

from utils import DeleteButton


class TryAndSeeCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @app_commands.command(name="try", description="Try it and see video")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def tryandsee(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        msg = "Why don't you [try it and see](https://tryitands.ee)"
        if reply_to is not None:
            msg = msg + " " + reply_to.mention
        await interaction.response.send_message(
            content=msg,
            view=DeleteButton(interaction.user.id)
        )


async def setup(bot):
    await bot.add_cog(TryAndSeeCog(bot=bot))

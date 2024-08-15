from discord import app_commands
from discord.ext import commands
import discord
import random

import utils


class ShutUpCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @app_commands.command(description="Get lost")
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.allowed_contexts(guilds=True, dms=False, private_channels=False)
    @app_commands.checks.has_permissions(moderate_members=True)
    async def shutup(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="Enjoy :D", ephemeral=True)
        await interaction.channel.send(["BaeFell", "Kenzie"][random.randint(0, 1)] + " suggests that you shut the fuck up")

    @shutup.error
    async def shutup_error(self, interaction: discord.Interaction, error) -> None:
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(content="You are missing the permissions to do that", ephemeral=True)
        else:
            utils.print_error(interaction, error)


async def setup(bot):
    await bot.add_cog(ShutUpCog(bot=bot))

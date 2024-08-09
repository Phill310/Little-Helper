from discord import app_commands
from discord.ext import commands
import discord

from utils import DeleteButton


class CooldownsCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @app_commands.command(description="Links to cooldown tutorial")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def cooldowns(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await interaction.response.send_message(
            content=self.bot.default_message.format(
                ping="" if reply_to is None else reply_to.mention,
                user=interaction.user.display_name,
                message="[Custom Cooldown Tutorial](https://docs.skunity.com/guides/tutorial/19354)"
            ),
            view=DeleteButton(interaction.user.id)
        )


async def setup(bot):
    await bot.add_cog(CooldownsCog(bot=bot))

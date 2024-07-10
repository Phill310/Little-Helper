from discord import app_commands
from discord.ext import commands
import discord


class CooldownsCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @app_commands.command(description="Links to cooldown tutorial")
    @app_commands.allowed_installs(guilds=False, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def cooldowns(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Custom Cooldown Tutorial]("
                                                        "https://docs.skunity.com/guides/tutorial/19354)")


async def setup(bot):
    await bot.add_cog(CooldownsCog(bot=bot))

from discord import app_commands
from discord.ext import commands
import discord
from typing import Optional


class TryAndSeeCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @app_commands.command(name="try", description="Try it and see video")
    @app_commands.describe(member="The member you want to ping")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def tryandsee(self, interaction: discord.Interaction, member: Optional[discord.Member] = None) -> None:
        msg = "why don't you [try it and see](https://tryitands.ee)"
        if member is not None:
            msg = msg + " " + member.mention
        await interaction.response.send_message(content=msg)


async def setup(bot):
    await bot.add_cog(TryAndSeeCog(bot=bot))

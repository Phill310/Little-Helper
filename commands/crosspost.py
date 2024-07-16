from typing import Optional

from discord import app_commands
from discord.ext import commands
import discord

from utils import DeleteButton


class crosspostCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @app_commands.command(description="Message advising not to crosspost")
    @app_commands.describe(member="The member you want to ping")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def crosspost(self, interaction: discord.Interaction, member: Optional[discord.Member] = None) -> None:
        msg = "Please do not crosspost"
        if member is not None:
            msg = msg + " " + member.mention
        msg += (". We have multiple channels to make sure that everyone's questions can be seen. Please pick one "
                "channel to ask your question in and then wait for someone to assist you.")
        await interaction.response.send_message(content=msg, view=DeleteButton(interaction.user.id))


async def setup(bot):
    await bot.add_cog(crosspostCog(bot=bot))

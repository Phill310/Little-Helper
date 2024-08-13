from discord import app_commands
from discord.ext import commands
import discord
import utils


class CrossPostCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @app_commands.command(description="Message advising not to crosspost")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def crosspost(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        msg = "Please do not crosspost"
        if reply_to is not None:
            msg = msg + " " + reply_to.mention
        msg += (". We have multiple channels to make sure that everyone's questions can be seen. Please pick one "
                "channel to ask your question in and then wait for someone to assist you.")
        await utils.send(
            interaction=interaction,
            content=msg
        )


async def setup(bot):
    await bot.add_cog(CrossPostCog(bot=bot))

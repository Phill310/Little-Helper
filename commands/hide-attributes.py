from discord import app_commands
from discord.ext import commands
import discord
import utils


class HideAttributesCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @app_commands.command(description="Explain that the attribute itemflag doesn't work on 1.20.5-1.21.4")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def hide_attributes(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            content="If you are playing on Minecraft 1.20.5-1.21.4 the hide attributes item flag will not work because "
                    "this behavior is now handled by the attributes themselves. You can use [this method]"
                    "(<https://github.com/ShaneBeee/SkBee/wiki/Tricks-Hide-Attribute-Modifiers>) to hide default "
                    "attributes on these versions. You can also update to 1.21.5+ to use the hide attributes flag",
            ping=reply_to
        )


async def setup(bot):
    await bot.add_cog(HideAttributesCog(bot=bot))

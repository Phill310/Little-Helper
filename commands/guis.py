from discord import app_commands
from discord.ext import commands
import discord

from utils import DeleteButton


class GuisCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="GUIs", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        embed.add_field(
            name="What are GUIs?",
            value="GUIs are custom inventories that you can use from all sorts of purposes including shops and server "
                  "selectors. There are two main ways to create them, using normal Skript and using the addon ["
                  "skript-gui](https://github.com/APickledWalrus/skript-gui)",
            inline=False
        )
        embed.add_field(
            name="Vanilla GUIs",
            value="You won't need to download any extra addons to start making vanilla GUIs! [Click Here]("
                  "https://docs.skunity.com/guides/tutorial/8939) to get started",
            inline=False
        )
        addon = """
Before you start making GUIs with skript-gui, you will have to download the addon [here](https://github.com/APickledWalrus/skript-gui/releases/latest)
Once you are ready to begin, [Click Here](https://https://github.com/APickledWalrus/skript-gui/wiki/1.-Creating-your-first-GUI) to get started!
This addon simplifies some of the steps of making GUIs such as listening for clicks
"""
        embed.add_field(
            name="skript-gui",
            value=addon,
            inline=False
        )
        embed.add_field(
            name="Tuske",
            value="Tuske is an old addon used for creating GUIs. It has become very outdated and will break all of "
                  "your code. If you still have this addon installed please switch to skript-gui",
            inline=False
        )
        self.embed = embed

    @app_commands.command(description="Informational embed about creating GUIs")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def guis(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
        await interaction.response.send_message(
            content=self.bot.default_message.format(
                ping="" if reply_to is None else reply_to.mention,
                user=interaction.user.display_name,
                message="this embed"
            ),
            embed=self.embed,
            view=DeleteButton(interaction.user.id)
        )


async def setup(bot):
    await bot.add_cog(GuisCog(bot=bot))

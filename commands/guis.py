from discord import app_commands
from discord.ext import commands
import discord


class GuisCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Guis", color=0x00ff00)
        embed.set_footer(
            text=bot.embedFooter,
            icon_url=bot.embedFooterUrl
        )
        embed.add_field(
            name="What are guis?",
            value="Guis are custom inventories that you can use from all sorts of purposes including shops and server "
                  "selectors. There are two main ways to create them, using normal Skript and using the addon ["
                  "Skript-Gui](https://github.com/APickledWalrus/skript-gui)",
            inline=False
        )
        embed.add_field(
            name="Vanilla Guis",
            value="You won't need to download any extra addons to start making vanilla guis! [Click Here]("
                  "https://docs.skunity.com/guides/tutorial/8939) to get started",
            inline=False
        )
        addon = """
Before you start making guis with Skript-Gui, you will have to download the addon [here](https://github.com/APickledWalrus/skript-gui/releases/latest)
Once you are ready to begin, [Click Here](https://https://github.com/APickledWalrus/skript-gui/wiki/1.-Creating-your-first-GUI) to get started!
This addon simplifies some of the steps of making guis such as listening for clicks
"""
        embed.add_field(
            name="Skript-Gui",
            value=addon,
            inline=False
        )
        embed.add_field(
            name="Tuske",
            value="Tuske is an old addon used for creating guis. Is has become very outdated and will break all of "
                  "your code. If you still have this addon installed please switch to Skript-Gui",
            inline=False
        )
        self.embed = embed

    @app_commands.command(description="Informational embed about creating guis")
    @app_commands.allowed_installs(guilds=False, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def guis(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(embed=self.embed)


async def setup(bot):
    await bot.add_cog(GuisCog(bot=bot))

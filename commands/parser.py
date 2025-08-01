from discord import app_commands
from discord.ext import commands
import discord
import utils

class ParserCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Parser", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url

        )
        skunityParser = """
[SkUnity Parser](https://parser.skunity.com) is the official parser for SkUnity to be used for Skript, but it is not recommended. The SkUnity Parser uses a very old version of Skript named `Skript-dev32`. 
This version is made in October 27th, 2017, making the version almost 8 years old. It is also known to crash a lot and break, making it hard to use, so usage of this is not recommended.
"""
        embed.add_field(
            name="SkUnity Parser",
            value=skunityParser
            inline=False
        )
        analyzerParser = """
The [Analyzer Parser](https://analyzer.notro.me) by the [SkEditor Team](https://github.com/SkEditorTeam) is an unofficial Skript Parser that uses modern versions of Skript. It only has SkBee right now as a detected addon. 
Though do note there is some issues with this as this is still in a very early prototype. This means that it is missing tons of features, like supporting more addons. They are working to add more features over time.
So do expect issues or missing features from this. If you want the best experience, use SkUnity Parser that does detect addons, or use Analyzer addon for the program called [SkEditor](https://github.com/SkEditorTeam/SkEditor)
to get the best parser experience possible. This is unofficial and not maintained by either SkriptLang or SkUnity. If there is any issues, report it in SkEditor's official discord.
"""
        embed.add_field(
            name"Analyzer Parser"
            value=analyzerParser
            inline=False
        )
        self.embed = embed

    @app_commands.command(description="Informational embed about Skript Website Parsers")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def parser(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            embed=self.embed,
            ping=reply_to
        )


async def setup(bot):
    await bot.add_cog(ParserCog(bot=bot))

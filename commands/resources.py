from discord import app_commands
from discord.ext import commands
import discord
import utils


class ResourcesCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Skript Resources Cheat Sheet", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        github = """
- https://github.com/SkriptLang/Skript/releases/latest: Download the latest Skript.
- https://github.com/SkriptLang/Skript/issues/new/choose: Report an issue or make a suggestion.
"""
        embed.add_field(
            name="SkriptLang Github",
            value=github,
            inline=False
        )

        docs = """
- https://docs.skriptlang.org/: Official SkriptLang docs, vanilla only.
- https://skripthub.net/docs/: SkriptHub docs, vanilla and addons.
- https://docs.skunity.com/: skUnity Docs, vanilla and addons.
"""
        embed.add_field(
            name="Docs",
            value=docs,
            inline=False
        )

        tutorials = """
- https://docs.skriptlang.org/tutorials.html: Official SkriptLang tutorials, coming soon.
- https://sovdee.gitbook.io/skript-tutorials: A set of general tutorials for learning Skript.
- https://skunity.com/tutorials: Community-made tutorials on skUnity.
- https://skripthub.net/tutorials/?search=&sort=score: Community-made tutorials on SkriptHub.
"""
        embed.add_field(
            name="Tutorials",
            value=tutorials,
            inline=False
        )

        other = """
- https://parser.skunity.com/: skUnity Parser, for parsing code in your browser.
- https://forums.skunity.com/: skUnity Forums, for asking for help and finding pre-made scripts.
"""
        embed.add_field(
            name="Other Resources",
            value=other,
            inline=False
        )
        self.embed = embed

    @app_commands.command(description="Embed full of useful resources")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def resources(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            embed=self.embed,
            ping=reply_to
        )


async def setup(bot):
    await bot.add_cog(ResourcesCog(bot=bot))

from discord import app_commands
from discord.ext import commands
import discord
import requests
import json
import datetime


class DownloadCog(commands.Cog):
    def __init__(self, bot):
        self.next_version_check = None
        self.embed = None
        self.bot = bot

    def update_embed(self):
        embed = discord.Embed(title="Skript Downloads", color=self.bot.embed_color, timestamp=datetime.datetime.now())
        embed.set_footer(
            text=self.bot.embed_footer,
            icon_url=self.bot.embed_footer_url
        )

        embed.add_field(
            name="Official SkriptLang Releases:",
            value="-# These are the recommended versions of Skript",
            inline=False
        )

        embed.add_field(
            name="Minecraft 1.9-1.12.2",
            value="Final Stable Release: [Skript 2.6.4](https://github.com/SkriptLang/Skript/releases/tag/2.6.4)",
            inline=False
        )

        latest_data = json.loads(requests.get("https://api.github.com/repos/SkriptLang/Skript/releases/latest").text)
        latest_version = latest_data["tag_name"]
        latest_unstable_data = json.loads(requests.get("https://api.github.com/repos/SkriptLang/Skript/releases").text)[0]
        latest_unstable_version = latest_unstable_data["tag_name"]
        latest = "Latest Stable Release: [Skript " + latest_version + "](" + latest_data["html_url"] + ")"
        if latest_unstable_version != latest_version:
            latest = latest + "\nLatest Experimental Release: [Skript " + latest_unstable_version + "](" + latest_unstable_data["html_url"] + ")"
        embed.add_field(
            name="Minecraft 1.13+",
            value=latest,
            inline=False
        )

        embed.add_field(
            name="\u200B",
            value="\u200B",
            inline=False
        )

        embed.add_field(
            name="Unofficial Releases:",
            value="-# These versions are not supported by SkriptLang",
            inline=False
        )

        mato_data = json.loads(requests.get("https://api.github.com/repos/Matocolotoe/Skript-1.8/releases/latest").text)
        mato_version = mato_data["tag_name"]
        embed.add_field(
            name="Minecraft 1.8.x",
            value="Recommended but **not supported**:\n[Matocolotoe fork, " + mato_version + "](" + mato_data["html_url"] + ")",
            inline=False
        )
        self.embed = embed
        self.next_version_check = datetime.datetime.now() + datetime.timedelta(hours=4)

    @app_commands.command(description="Informational embed on downloading Skript")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def download(self, interaction: discord.Interaction) -> None:
        if self.embed is None or self.next_version_check < datetime.datetime.now():
            self.update_embed()
        await interaction.response.send_message(embed=self.embed)


async def setup(bot):
    await bot.add_cog(DownloadCog(bot=bot))

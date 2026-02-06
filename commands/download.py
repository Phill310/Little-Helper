from discord import app_commands
from discord.ext import commands
import discord
import requests
import json
from datetime import datetime, timedelta
import utils


class DownloadCog(commands.Cog):
    def __init__(self, bot):
        self.next_version_check = None
        self.embed = None
        self.bot = bot

    def get_date_18_month_ago(self, date: datetime):
        month = date.month
        year = date.year
        if month <= 6:
            year -= 1
            month += 12
        month -= 6
        year -= 1

        return date.replace(month=month, year=year)

    def update_embed(self):
        embed = discord.Embed(title="", color=self.bot.embed_color, timestamp=datetime.now())
        embed.set_footer(
            text=self.bot.embed_footer,
            icon_url=self.bot.embed_footer_url
        )

        latest_data = json.loads(requests.get("https://api.github.com/repos/SkriptLang/Skript/releases/latest").text)
        latest_version = latest_data["tag_name"]
        latest_release_date = datetime.fromisoformat(latest_data["published_at"])
        latest_releases = json.loads(requests.get("https://api.github.com/repos/SkriptLang/Skript/releases").text)[:10]
        latest_unstable_data = None
        if "pre" in latest_releases[0]["tag_name"]:
            if datetime.fromisoformat(latest_releases[0]["published_at"]) > latest_release_date:
                latest_unstable_data = latest_releases[0]
        latest_feature = None
        if latest_version.split(".")[-1] == "0":
            latest_feature = latest_release_date

        for release in latest_releases:
            if not latest_feature and release["tag_name"].split(".")[-1] == "0":
                latest_feature = datetime.fromisoformat(release["published_at"])
                break

        minecraft_releases = [release for release in json.loads(requests.get("https://piston-meta.mojang.com/mc/game/version_manifest.json").text)["versions"] if release["type"] == "release"]
        supported_releases = []
        oldest_supported_date = self.get_date_18_month_ago(latest_feature)
        for release in minecraft_releases:
            release_date = datetime.fromisoformat(release["releaseTime"])
            if release_date > latest_release_date:
                continue
            if release_date >= oldest_supported_date:
                supported_releases.append(release["id"])
            else:
                supported_releases.append(release["id"])
                break

        latest = f"Minecraft **{supported_releases[-1]}** - **{supported_releases[0]}**: [Skript " + latest_version + "](" + latest_data["html_url"] + ")"
        if latest_unstable_data:
            latest += "\n### Latest Beta:\n> Not recommended for production servers: [Skript " + latest_unstable_data["tag_name"] + "](" + latest_unstable_data["html_url"] + ")"

        embed.description = f"""
# Download Skript
Skript supports minecraft versions that were released up to 18 months before the release of each Skript version. 
### Latest Release:
{latest}

If you would like to use an older version of Skript you can search through the [releases](https://github.com/SkriptLang/Skript/releases) section of the github.
"""
        self.embed = embed
        self.next_version_check = datetime.now() + timedelta(hours=4)

    @app_commands.command(description="Informational embed on downloading Skript")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def download(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        if self.embed is None or self.next_version_check < datetime.now():
            self.update_embed()
        await utils.send(
            interaction=interaction,
            embed=self.embed,
            ping=reply_to
        )


async def setup(bot):
    await bot.add_cog(DownloadCog(bot=bot))

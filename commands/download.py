from discord import app_commands
from discord.ext import commands
import discord
import requests
import json
import datetime
import utils


class DownloadCog(commands.Cog):
    def __init__(self, bot):
        self.next_version_check = None
        self.embed = None
        self.bot = bot

    def update_embed(self):
        embed = discord.Embed(title="", color=self.bot.embed_color, timestamp=datetime.datetime.now())
        embed.set_footer(
            text="Embed designed by jakegblp",
            icon_url=self.bot.embed_footer_url
        )

        latest_data = json.loads(requests.get("https://api.github.com/repos/SkriptLang/Skript/releases/latest").text)
        latest_version = latest_data["tag_name"]
        latest_releases = json.loads(requests.get("https://api.github.com/repos/SkriptLang/Skript/releases").text)[:10]
        latest_unstable_data = 0
        latest_unstable_version = 0
        highest_version_split = 0
        for release in latest_releases:
            if latest_unstable_data == 0:
                latest_unstable_data = release
                latest_unstable_version = release["tag_name"]
                highest_version_split = release["tag_name"].split("-")[0].split(".")
            else:
                current_version = release["tag_name"].split("-")[0].split(".")
                for i in range(3):
                    if int(current_version[i]) > int(highest_version_split[i]):
                        latest_unstable_data = release
                        latest_unstable_version = release["tag_name"]
                        highest_version_split = release["tag_name"].split("-")[0].split(".")
                        break
                    elif int(current_version[i]) < int(highest_version_split[i]):
                        break
        latest = "> Minecraft **1.19.4+**: [Skript " + latest_version + "](" + latest_data["html_url"] + ")"
        if latest_unstable_version != 0 and latest_unstable_version != latest_version:
            latest += "\n### Latest Beta:\n> Not recommended for production servers: [Skript " + latest_unstable_version + "](" + latest_unstable_data[
                "html_url"] + ")"

        mato_data = json.loads(requests.get("https://api.github.com/repos/Matocolotoe/Skript-1.8/releases/latest").text)
        mato_version = mato_data["tag_name"]

        embed.description = f"""
# Skript Downloads
These are the recommended versions of Skript:
### Latest Release:
{latest}
### Older Releases:
> Minecraft **1.9** - **1.12.2**: [Skript 2.6.4](https://github.com/SkriptLang/Skript/releases/tag/2.6.4)
> Minecraft **1.13** - **1.19.3**: [Skript 2.9.5](https://github.com/SkriptLang/Skript/releases/tag/2.9.5)

### Unofficial Releases:
> Minecraft **1.8.x**: [Matocolotoe fork {mato_version}]({mato_data["html_url"]})
-# These versions are not supported by SkriptLang
"""
        self.embed = embed
        self.next_version_check = datetime.datetime.now() + datetime.timedelta(hours=4)

    @app_commands.command(description="Informational embed on downloading Skript")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def download(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        if self.embed is None or self.next_version_check < datetime.datetime.now():
            self.update_embed()
        await utils.send(
            interaction=interaction,
            embed=self.embed,
            ping=reply_to
        )


async def setup(bot):
    await bot.add_cog(DownloadCog(bot=bot))

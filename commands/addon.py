from discord import app_commands
from discord.ext import commands
import discord
import requests
import os
import datetime
import utils


class AddonCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.token = os.getenv('SKUNITY_TOKEN')
        self.last_addon_check = None
        self.addon_list = {}
        self.addon_choices = []

    def update_addons(self):
        addons = requests.get(f"https://api.skunity.com/v1/{self.token}/resources/addons").json()
        self.addon_list = addons['result']
        for addon_id in self.addon_list:
            self.addon_choices.append(app_commands.Choice(name=addons['result'][addon_id]['addon_name'], value=addon_id))
        self.last_addon_check = datetime.datetime.now()

    @app_commands.command(description="Get info about an addon")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.describe(addon_id="The addon you want to search")
    @app_commands.rename(addon_id="addon")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def addon(self, interaction: discord.Interaction, addon_id: str, reply_to: discord.User = None) -> None:
        addon = self.addon_list[addon_id]
        embed = discord.Embed(title="Addon: " + addon['addon_name'], color=self.bot.embed_color, timestamp=self.last_addon_check)
        author_pfp = ""
        if addon['author_profile_picture'] is not None:
            author_id = int(addon['author_profile_picture'].split('=')[-1])
            author_pfp = f"https://forums.skunity.com/data/avatars/l/{int(author_id/1000)}/{author_id}.jpg"
        embed.set_author(
            name=addon['author_name'],
            icon_url=author_pfp,
            url=addon['author_profile']
        )
        embed.set_footer(
            text=self.bot.embed_footer,
            icon_url=self.bot.embed_footer_url
        )
        if addon['download'] is not None:
            embed.add_field(
                name="Download",
                value=f"[Click to download]({addon['download']})",
                inline=True
            )
        if addon['docs'] is not None:
            embed.add_field(
                name="Docs",
                value=f"[Click to read docs]({addon['docs']})",
                inline=True
            )
        if addon['forums'] is not None:
            embed.add_field(
                name="Forums",
                value=f"[Click for more info]({addon['forums']})",
                inline=True
            )
        await utils.send(
            interaction=interaction,
            ping=reply_to,
            embed=embed
        )

    @addon.autocomplete("addon_id")
    async def addon_autocomplete(self, interaction: discord.Interaction, current: str):
        if self.last_addon_check is None or self.last_addon_check + datetime.timedelta(hours=6) < datetime.datetime.now():
            self.update_addons()
        selected = []
        current = current.lower().replace(" ", "-")
        for addon in self.addon_choices:
            if addon.name.lower().startswith(current):
                selected.append(addon)
                continue
            for word in addon.name.lower().split("-"):
                if word.startswith(current):
                    selected.append(addon)
                    break
        return selected[:25]


async def setup(bot):
    await bot.add_cog(AddonCog(bot=bot))

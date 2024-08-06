from discord import app_commands
from discord.ext import commands
import discord
import requests
import datetime
import os

from utils import DeleteButton


class ShaneCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        bot.tree.add_command(Shane(bot))


@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
class Shane(app_commands.Group):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.auth = os.environ['GIT_TOKEN']
        self.next_snippet_check = None
        self.snippet_list = []
        self.next_wiki_check = None
        self.wiki_list = []
        self.bot = bot

    def update_snippets(self):
        headers = {'Authorization': "Bearer " + self.auth}
        snippet_data = requests.get("https://api.github.com/repos/ShaneBeee/SkriptSnippets/git/trees/master?recursive=1", headers=headers).json()
        snippets = []
        for file in snippet_data["tree"]:
            if file["path"].endswith(".sk"):
                snippets.append(app_commands.Choice(name=file["path"][9:-3], value=file["path"]))
        self.snippet_list = snippets
        self.next_snippet_check = datetime.datetime.now() + datetime.timedelta(hours=6)

    def update_wiki(self):
        headers = {'Authorization': "Bearer " + self.auth}
        wiki_data = requests.get("https://github.com/ShaneBeee/SkBee/wiki", headers=headers).text
        wikis = []
        for line in wiki_data.splitlines():
            # not an ideal way to check (no GitHub api for wikis) but we ball
            if "src=\"https://github.com/ShaneBeee/SkBee/wiki/" in line:
                link = line.split("src=\"")[-1][:-7]
                section = link.split("/")[-1]
                wikis.append(app_commands.Choice(name=section.replace("-", " ").replace("%E2%80%90", ""), value=section))
        self.wiki_list = wikis

    @app_commands.command(description="Lin to shane's repo of skript snippets")
    @app_commands.describe(snippet="A specific snippet to send")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def snippets(self, interaction: discord.Interaction, snippet: str = "", reply_to: discord.Member = None) -> None:
        snippet_name = ""
        if snippet != "":
            snippet_name = " (" + snippet[9:] + ")"
        await interaction.response.send_message(
            content=self.bot.default_message.format(
                ping="" if reply_to is None else reply_to.mention,
                user=interaction.user.display_name,
                message="[Shane's snippets" + snippet_name + "](https://github.com/ShaneBeee/SkriptSnippets/blob/master/" + snippet + ")"
            ),
            view=DeleteButton(interaction.user.id)
        )

    @snippets.autocomplete("snippet")
    async def snippets_autocomplete(self, interaction: discord.Interaction, current: str):
        if self.next_snippet_check is None or self.next_snippet_check < datetime.datetime.now():
            self.update_snippets()
        current = current.lower().replace(" ", "-")
        selected = []
        for snippet in self.snippet_list:
            if snippet.name.lower().startswith(current) or snippet.name.lower().split("/")[-1].startswith(current):
                selected.append(snippet)
        return selected[:25]

    @app_commands.command(description="Link to SkBee's wiki")
    @app_commands.describe(wiki="A specific wiki to send")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def wiki(self, interaction: discord.Interaction, wiki: str = "", reply_to: discord.Member = None) -> None:
        wiki_name = ""
        if wiki != "":
            wiki_name = " (" + wiki.replace("%E2%80%90", "") + ")"
        await interaction.response.send_message(
            content=self.bot.default_message.format(
                ping="" if reply_to is None else reply_to.mention,
                user=interaction.user.display_name,
                message="[SkBee's Wiki" + wiki_name + "](https://github.com/ShaneBeee/SkBee/wiki/" + wiki + ")"
            ),
            view=DeleteButton(interaction.user.id)
        )

    @wiki.autocomplete("wiki")
    async def wiki_autocomplete(self, interaction: discord.Interaction, current: str):
        if self.next_wiki_check is None or self.next_wiki_check < datetime.datetime.now():
            self.update_wiki()
        selected = []
        for wiki in self.wiki_list:
            if wiki.name.lower().startswith(current.lower().replace("-", " ")):
                selected.append(wiki)
        return selected[:25]


async def setup(bot):
    await bot.add_cog(ShaneCog(bot=bot))

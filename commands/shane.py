from discord import app_commands
from discord.ext import commands
import discord
import requests
import json
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
        self.bot = bot
        if 'DEV' not in os.environ:
            self.update_snippets()

    def update_snippets(self):
        headers = {'Authorization': "Bearer " + self.auth}
        snippet_data = json.loads(requests.get("https://api.github.com/repos/ShaneBeee/SkriptSnippets/git/trees/46ae166a31fc3a07512c3873f0adf9dcf5981eb6?recursive=1", headers=headers).text)
        snippets = []
        for file in snippet_data["tree"]:
            if file["path"].endswith(".sk"):
                snippets.append(app_commands.Choice(name=file["path"][:-3], value="snippets/" + file["path"]))
        self.snippet_list = snippets
        self.next_snippet_check = datetime.datetime.now() + datetime.timedelta(hours=6)

    @app_commands.command(description="Link to shane's repo of skript snippets")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.describe(snippet="A specific snippet to send")
    async def snippets(self, interaction: discord.Interaction, snippet: str = "", reply_to: discord.Member = None) -> None:
        snippet_name = ""
        if snippet != "":
            snippet_name = " (" + snippet[9:] + ")"
        if self.next_snippet_check is None or self.next_snippet_check < datetime.datetime.now():
            await interaction.response.defer(thinking=True)
            self.update_snippets()
            await interaction.edit_original_response(
                content=self.bot.default_message.format(
                    ping="" if reply_to is None else reply_to.mention,
                    user=interaction.user.display_name,
                    message="[Shane's snippets" + snippet_name + "](https://github.com/ShaneBeee/SkriptSnippets/blob/master/" + snippet + ")"
                ),
                view=DeleteButton(interaction.user.id)
            )
        else:
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
        selected = []
        for snippet in self.snippet_list:
            if snippet.name.lower().startswith(current.lower()) or snippet.name.lower().split("/")[-1].startswith(current.lower()):
                selected.append(snippet)
        return selected[:25]

    @app_commands.command(description="Link to SkBee's wiki")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def wiki(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
        await interaction.response.send_message(
            content=self.bot.default_message.format(
                ping="" if reply_to is None else reply_to.mention,
                user=interaction.user.display_name,
                message="[SkBee's wiki](https://github.com/ShaneBeee/SkBee/wiki)"
            ),
            view=DeleteButton(interaction.user.id)
        )

    @app_commands.command(description="Link to SkBee's nbt heads")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def heads(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
        await interaction.response.send_message(
            content=self.bot.default_message.format(
                ping="" if reply_to is None else reply_to.mention,
                user=interaction.user.display_name,
                message="[Custom NBT Heads](https://github.com/ShaneBeee/SkBee/wiki/NBT-Heads)"
            ),
            view=DeleteButton(interaction.user.id)
        )


async def setup(bot):
    await bot.add_cog(ShaneCog(bot=bot))

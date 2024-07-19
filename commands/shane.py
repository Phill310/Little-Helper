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
        bot.tree.add_command(Shane())


@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
class Shane(app_commands.Group):
    def __init__(self):
        super().__init__()
        self.auth = os.environ['GIT_TOKEN']
        self.next_snippet_check = None
        self.snippet_list = []
        if 'DEV' not in os.environ:
            self.update_snippets()

    def update_snippets(self):
        headers = {'Authorization': "Bearer " + self.auth}
        snippet_data = json.loads(requests.get("https://api.github.com/repos/ShaneBeee/SkriptSnippets/contents/snippets", headers=headers).text)
        snippets = []
        for file in snippet_data:
            if file["name"].endswith(".sk"):
                snippets.append(app_commands.Choice(name=file["name"][:-3], value=file["path"]))
            elif file["type"] == "dir":
                folder_data = json.loads(requests.get("https://api.github.com/repos/ShaneBeee/SkriptSnippets/contents/" + file["path"], headers=headers).text)
                for sub_file in folder_data:
                    if sub_file["name"].endswith(".sk"):
                        snippets.append(app_commands.Choice(name=sub_file["name"][:-3], value=sub_file["path"]))
        self.snippet_list = snippets
        self.next_snippet_check = datetime.datetime.now() + datetime.timedelta(hours=6)

    @app_commands.command(description="Link to shane's repo of skript snippets")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.describe(snippet="A specific snippet to send")
    async def snippets(self, interaction: discord.Interaction, snippet: str = "", reply_to: discord.Member = None) -> None:
        snippet_name = ""
        if snippet != "":
            snippet_name = " (" + snippet[9:] + ")"
        if self.next_snippet_check < datetime.datetime.now():
            await interaction.response.defer(thinking=True)
            self.update_snippets()
            await interaction.edit_original_response(
                content="Please read [Shane's snippets" + snippet_name + "](https://github.com/ShaneBeee/SkriptSnippets/blob/master/" + snippet + ") "
                        + (reply_to.mention if reply_to is not None else ""),
                view=DeleteButton(interaction.user.id)
            )
        else:
            await interaction.response.send_message(
                content="Please read [Shane's snippets" + snippet_name + "](https://github.com/ShaneBeee/SkriptSnippets/blob/master/" + snippet + ") "
                        + (reply_to.mention if reply_to is not None else ""),
                view=DeleteButton(interaction.user.id)
            )

    @snippets.autocomplete("snippet")
    async def snippets_autocomplete(self, interaction: discord.Interaction, current: str):
        return [snippet for snippet in self.snippet_list if snippet.name.lower().startswith(current.lower())][:25]

    @app_commands.command(description="Link to skbee's wiki")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def wiki(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
        await interaction.response.send_message(
            content="Please read [Skbee's wiki](https://github.com/ShaneBeee/SkBee/wiki) "
                    + (reply_to.mention if reply_to is not None else ""),
            view=DeleteButton(interaction.user.id)
        )

    @app_commands.command(description="Link to skbee's nbt heads")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def heads(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
        await interaction.response.send_message(
            content="Please read [Custom NBT Heads](https://github.com/ShaneBeee/SkBee/wiki/NBT-Heads) "
                    + (reply_to.mention if reply_to is not None else ""),
            view=DeleteButton(interaction.user.id)
        )


async def setup(bot):
    await bot.add_cog(ShaneCog(bot=bot))

from discord import app_commands
from discord.ext import commands
import discord
import requests
import json
import datetime


class ShaneCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        bot.tree.add_command(Shane())


@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
class Shane(app_commands.Group):
    def __init__(self):
        super().__init__()
        self.auth = open("tokens.txt", "r").readlines()[1]
        self.next_snippet_check = None
        self.snippet_list = []
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
    @app_commands.describe(snippet="A specific snippet to send")
    async def snippets(self, interaction: discord.Interaction, snippet: str = "") -> None:
        snippet_name = ""
        if snippet != "":
            snippet_name = " (" + snippet[9:] + ")"
        if self.next_snippet_check < datetime.datetime.now():
            await interaction.response.defer(thinking=True)
            self.update_snippets()
            await interaction.edit_original_response(content="[Shane's snippets" + snippet_name + "](https://github.com/ShaneBeee/SkriptSnippets/blob/master/" + snippet + ")")
        else:
            await interaction.response.send_message(content="[Shane's snippets" + snippet_name + "](https://github.com/ShaneBeee/SkriptSnippets/blob/master/" + snippet + ")")

    @snippets.autocomplete("snippet")
    async def snippets_autocomplete(self, interaction: discord.Interaction, current: str):
        return [snippet for snippet in self.snippet_list if snippet.name.lower().startswith(current.lower())][:25]

    @app_commands.command(description="Link to skbee's wiki")
    async def wiki(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Skbee's wiki](https://github.com/ShaneBeee/SkBee/wiki)")

    @app_commands.command(description="Link to skbee's nbt heads")
    async def heads(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Custom NBT Heads](https://github.com/ShaneBeee/SkBee/wiki/NBT-Heads)")


async def setup(bot):
    await bot.add_cog(ShaneCog(bot=bot))

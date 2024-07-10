from discord import app_commands
from discord.ext import commands
import discord


class ShaneCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        bot.tree.add_command(Shane())


@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
class Shane(app_commands.Group):
    @app_commands.command(description="Link to shane's repo of skript snippets")
    async def snippets(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Shane's snippets](https://github.com/ShaneBeee/SkriptSnippets/tree/master/snippets)")

    @app_commands.command(description="Link to skbee's wiki")
    async def wiki(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Skbee's wiki](https://github.com/ShaneBeee/SkBee/wiki)")

    @app_commands.command(description="Link to skbee's nbt heads")
    async def heads(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Custom NBT Heads](https://github.com/ShaneBeee/SkBee/wiki/NBT-Heads)")


async def setup(bot):
    await bot.add_cog(ShaneCog(bot=bot))

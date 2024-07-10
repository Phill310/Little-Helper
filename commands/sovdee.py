from discord import app_commands
from discord.ext import commands
import discord


class SovdeeCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        bot.tree.add_command(Sovdee())


@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
class Sovdee(app_commands.Group):
    @app_commands.command(name="global-local", description="Global vs Local variables tutorial")
    async def gvars(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovdee's Global vs Local Variable tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/variables/global-and-local)")

    @app_commands.command(name="variables", description="Variable tutorials")
    async def vars(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovdee's Variable Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/variables)")

    @app_commands.command(description="Home page of Sovdee's tutorials")
    async def home(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="https://sovdee.gitbook.io/skript-tutorials/")

    @app_commands.command(name="indentation", description="Indentation and Program Flow")
    async def indent(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovdee's Indentation Tutorial]("
                                                        "https://sovdee.gitbook.io/skript-tutorials/core-concepts/indentation)")

    @app_commands.command(name="commands", description="Custom Commands")
    async def commands(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovdee's Custom Command Tutorial]("
                                                        "https://sovdee.gitbook.io/skript-tutorials/core-concepts/commands)")

    @app_commands.command(name="vectors", description="Vector tutorials")
    async def vectors(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovdee's Vector tutorial]("
                                                        "https://sovdee.gitbook.io/skript-tutorials/core-concepts/vectors)")


async def setup(bot):
    await bot.add_cog(SovdeeCog(bot=bot))

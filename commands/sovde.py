from discord import app_commands
from discord.ext import commands
import discord

from utils import DeleteButton


class SovdeCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        bot.tree.add_command(Sovde())


@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
class Sovde(app_commands.Group):
    @app_commands.command(name="global-local", description="Global vs Local variables tutorial")
    async def gvars(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovde's Global vs Local Variable Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/variables/global-and-local)", view=DeleteButton(interaction.user.id))

    @app_commands.command(name="variables", description="Variable tutorials")
    async def vars(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovde's Variable Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/variables)", view=DeleteButton(interaction.user.id))

    @app_commands.command(description="Home page of Sovde's skript tutorials")
    async def home(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="https://sovdee.gitbook.io/skript-tutorials/", view=DeleteButton(interaction.user.id))

    @app_commands.command(name="indentation", description="Indentation and Program Flow")
    async def indent(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovde's Indentation Tutorial]("
                                                        "https://sovdee.gitbook.io/skript-tutorials/core-concepts/indentation)", view=DeleteButton(interaction.user.id))

    @app_commands.command(name="commands", description="Custom Commands")
    async def commands(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovde's Custom Command Tutorial]("
                                                        "https://sovdee.gitbook.io/skript-tutorials/core-concepts/commands)", view=DeleteButton(interaction.user.id))

    @app_commands.command(name="vectors", description="Vector tutorials")
    async def vectors(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovde's Vector Tutorial]("
                                                        "https://sovdee.gitbook.io/skript-tutorials/core-concepts/vectors)", view=DeleteButton(interaction.user.id))

    @app_commands.command(name="functions", description="Functions tutorial")
    async def functions(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovde's Function Tutorial]("
                                                        "https://sovdee.gitbook.io/skript-tutorials/core-concepts/indentation/functions)", view=DeleteButton(interaction.user.id))

    @app_commands.command(name="list-basics", description="Variable List Basics Tutorial")
    async def functions(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovde's List Variable Tutorial]("
                                                        "https://sovdee.gitbook.io/skript-tutorials/core-concepts/variables/list-basics)", view=DeleteButton(interaction.user.id))    


async def setup(bot):
    await bot.add_cog(SovdeCog(bot=bot))

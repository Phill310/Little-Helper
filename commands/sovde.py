from discord import app_commands
from discord.ext import commands
import discord
import utils


class SovdeCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        bot.tree.add_command(Sovde(bot))


@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
class Sovde(app_commands.Group):
    def __init__(self, bot):
        super().__init__()
        self.bot: commands.Bot = bot

    @app_commands.command(name="global-local", description="Global vs Local variables tutorial")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def gvars(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            message="[Sovde's Global vs Local Variable Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/variables/global-and-local)",
            ping=reply_to
        )

    @app_commands.command(name="variables", description="Variable tutorials")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def vars(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            message="[Sovde's Variable Tutorials](https://sovdee.gitbook.io/skript-tutorials/core-concepts/variables)",
            ping=reply_to
        )

    @app_commands.command(name="memory-variables", description="Memory variable tutorial")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def ram_vars(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            message="[Sovde's Memory Variable Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/variables/memory-variables-metadata-and-alternatives)",
            ping=reply_to
        )

    @app_commands.command(description="Home page of Sovde's skript tutorials")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def home(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            message="https://sovdee.gitbook.io/skript-tutorials/",
            ping=reply_to
        )

    @app_commands.command(name="indentation", description="Indentation and Program Flow")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def indent(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            message="[Sovde's Indentation Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/indentation)",
            ping=reply_to
        )

    @app_commands.command(name="commands", description="Custom Commands")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def commands(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            message="[Sovde's Custom Command Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/commands)",
            ping=reply_to
        )

    @app_commands.command(name="vectors", description="Vector tutorials")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def vectors(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            message="[Sovde's Vector Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/vectors)",
            ping=reply_to
        )

    @app_commands.command(name="functions", description="Functions tutorial")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def functions(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            message="[Sovde's Function Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/indentation/functions)",
            ping=reply_to
        )

    @app_commands.command(name="list-basics", description="Variable List Basics Tutorial")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def listvars(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            message="[Sovde's List Variable Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/variables/list-basics)",
            ping=reply_to
        )


async def setup(bot):
    await bot.add_cog(SovdeCog(bot=bot))

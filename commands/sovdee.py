from discord import app_commands
from discord.ext import commands
import discord

from utils import DeleteButton


class SovdeeCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        bot.tree.add_command(Sovdee())


@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
class Sovdee(app_commands.Group):
    @app_commands.command(name="global-local", description="Global vs Local variables tutorial")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def gvars(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
        await interaction.response.send_message(
            content="Please read [Sovdee's Global vs Local Variable Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/variables/global-and-local) "
                    + (reply_to.mention if reply_to is not None else ""),
            view=DeleteButton(interaction.user.id)
        )

    @app_commands.command(name="variables", description="Variable tutorials")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def vars(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
        await interaction.response.send_message(
            content="Please read [Sovdee's Variable Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/variables) "
                    + (reply_to.mention if reply_to is not None else ""),
            view=DeleteButton(interaction.user.id)
        )

    @app_commands.command(description="Home page of Sovdee's tutorials")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def home(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
        await interaction.response.send_message(
            content="Please read https://sovdee.gitbook.io/skript-tutorials/ "
                    + (reply_to.mention if reply_to is not None else ""),
            view=DeleteButton(interaction.user.id)
        )

    @app_commands.command(name="indentation", description="Indentation and Program Flow")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def indent(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
        await interaction.response.send_message(
            content="Please read [Sovdee's Indentation Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/indentation) "
                    + (reply_to.mention if reply_to is not None else ""),
            view=DeleteButton(interaction.user.id)
        )

    @app_commands.command(name="commands", description="Custom Commands")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def commands(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
        await interaction.response.send_message(
            content="Please read [Sovdee's Custom Command Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/commands) "
                    + (reply_to.mention if reply_to is not None else ""),
            view=DeleteButton(interaction.user.id)
        )

    @app_commands.command(name="vectors", description="Vector tutorials")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def vectors(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
        await interaction.response.send_message(
            content="Please read [Sovdee's Vector Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/vectors) "
                    + (reply_to.mention if reply_to is not None else ""),
            view=DeleteButton(interaction.user.id)
        )

    @app_commands.command(name="functions", description="Functions tutorial")
    @app_commands.describe(reply_to="The user you want to send this message to")
    async def functions(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
        await interaction.response.send_message(
            content="Please read [Sovdee's Function Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/indentation/functions) "
                    + (reply_to.mention if reply_to is not None else ""),
            view=DeleteButton(interaction.user.id)
        )


async def setup(bot):
    await bot.add_cog(SovdeeCog(bot=bot))

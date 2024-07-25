from discord import app_commands
from discord.ext import commands
import discord

from utils import DeleteButton


class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Percent signs (%)", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        embed.add_field(
            name="When should percent signs be used in Skript?",
            value="In Skript, the purpose of surrounding an expression in % signs is letting Skript know you want it "
                  "to be parsed as an expression and insert its value into the string or variable you've put it in.",
            inline=False
        )
        incorrect_example = """
```vb
give dirt to %player%
send "Hey there player" to %arg-1%
kill %{_entity}%```
Here, the % signs are not inside strings or variable names and should therefore be removed.
"""
        embed.add_field(
            name="Incorrect Usage",
            value=incorrect_example,
            inline=False
        )
        correct_example = """
```vb
broadcast "%player% has joined"
send "%{_variable::*}%" to player
set {variable::%uuid of player%} to 10```
Here, the % signs are being use properly, as a means to put expressions inside strings and variable names.
"""
        embed.add_field(
            name="Correct Usage",
            value=correct_example,
            inline=False
        )

        embed.add_field(
            name="Using % in a string",
            value="If you want to use the % character in a string such as sending the message `I am 50% done`, "
                  "you have to escape the character. To escape a character you must put 2 of them next to each other. "
                  "Our example would then be: ```vb\nsend \"I am 50%% done\"```",
            inline=False
        )
        self.embed = embed

    @app_commands.command(description="Informational embed about using %")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def percent(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
        await interaction.response.send_message(
            content=self.bot.default_message.format(
                ping="" if reply_to is None else reply_to.mention,
                user=interaction.user.display_name,
                message="this embed"
            ),
            embed=self.embed,
            view=DeleteButton(interaction.user.id)
        )


async def setup(bot):
    await bot.add_cog(Cog(bot=bot))

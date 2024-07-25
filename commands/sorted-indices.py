from discord import app_commands
from discord.ext import commands
import discord

from utils import DeleteButton


class SortedIndicesCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Sorted Indices", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        embed.description = ("The sorted indices expression returns a new list of indices sorted by the value of the "
                             "index. This can be very helpful for making all sorts of leaderboards. Lets say we have "
                             "the balances of our players saved in the variable `{balance::%player's uuid%}`. To "
                             "create our leaderboard we can use```vb\nset {_sorted::*} to sorted indices of "
                             "{balance::*} in descending order````{_sorted::*}` will be a list of uuids with `"
                             "{_sorted::1}` being the person with the most money. If we wanted to check how much money "
                             "they had we could plug the uuid back into the original variable: `{balance::%{_sorted::1}%}`")
        example = """
```vb
command /baltop:
    trigger:
        set {_sorted::*} to sorted indices of {balance::*} in descending order
        send "<aqua>Baltop"
        loop {_sorted::*}:
            send "<gold>%loop-iteration%. <white>%offlineplayer(loop-value)% <gray>- <green>$%{balance::%loop-value%}%"
            if loop-iteration = 10:
                stop```
"""
        embed.add_field(
            name="Leaderboard Example",
            value=example,
            inline=False
        )
        self.embed = embed

    @app_commands.command(name="sorted-indices", description="Informational embed sorted indices expression")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def sorted_indices(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
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
    await bot.add_cog(SortedIndicesCog(bot=bot))

from discord import app_commands
from discord.ext import commands
import discord


class ListsCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="List Variables", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        embed.add_field(
            name="Why?",
            value="List variables are a much cleaner way of storing multiple values, especially objects that are "
                  "unique to something (the money of a player, the warps of the server), as they can be looped, "
                  "added to, removed from, accessed, and deleted all at once, making variable organization a breeze. "
                  "A list basically maps objects to their corresponding unique indices.",
            inline=False
        )
        create_list = """
To make a list, we simply use the list variable separator `::` in the variable's name: `{money::%uuid of player%}`, `{warps::%{_warpName}%}`, `{luckyNumbers::*}`.
For example:
```
set {_list::*} to 1, 2, 3, and 4
set {_list::%uuid of player%} to player```
"""
        embed.add_field(
            name="How to create a list variable?",
            value=create_list,
            inline=False
        )
        embed.add_field(
            name="Indices and values",
            value="As already mentioned, lists have indices and values. For "
                  "instance, in `set {money::%uuid of player%} to 100` the "
                  "index is the uuid of the player and the value is 100. We "
                  "can also access all the values at once by using `::*`. This "
                  "last part means we can replace a lot of common loops with "
                  "simple lists, like `send \"You're on team red!\" to {"
                  "team-red::*}` instead of looping through all players and "
                  "checking if each one is on team red.",
            inline=False
        )
        common_situations = """
```
{%player%.money} -> {money::%player's uuid%}
{home.warps.%player%} -> {warps::%player's uuid%::home}
{%player%.cooldown} -> {cooldown::%player's uuid%}```
"""
        embed.add_field(
            name="Common situations which can use lists instead",
            value=common_situations,
            inline=False
        )
        self.embed = embed

    @app_commands.command(description="Informational embed about list variables")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def lists(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(embed=self.embed)


async def setup(bot):
    await bot.add_cog(ListsCog(bot=bot))

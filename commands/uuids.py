from discord import app_commands
from discord.ext import commands
import discord
from utils import DeleteButton


class UUIDsCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="UUIDs in variables", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        embed.add_field(
            name="Why?",
            value="UUIDs are the best way to store player info, as a player's UUID will never change, whereas their "
                  "name can. UUIDs can be used for any type of variable, in the same way as `%player%` is. Your "
                  "player's money/stats can be lost if they change their in game name when `%player%` is used.",
            inline=False
        )
        embed.add_field(
            name="How to use",
            value="You use this in the same was as using `%player%`, just with `'s uuid` on the end, so `player's "
                  "uuid`! You can also enable \"use player UUIDs in variable names\" in your config.sk file. This "
                  "causes all instances of `%player%` in variable names to actually use the player's UUID instead.",
            inline=False
        )
        example = """
```yaml
{stats::%player%::kills} -> {stats::%player's uuid%::kills}
{vanish::%player%} -> {vanish::%uuid of player%}
{generator::%player%::*} -> {generator::%player's uuid%::*}```
"""
        embed.add_field(
            name="Common situations which can use UUID's instead",
            value=example,
            inline=False
        )
        self.embed = embed

    @app_commands.command(description="Informational embed about using uuids instead of player")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def uuids(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
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
    await bot.add_cog(UUIDsCog(bot=bot))

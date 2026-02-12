from discord import app_commands
from discord.ext import commands
import discord
import utils


class PlaceholdersCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Using Placeholders", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        embed.description = \
            ("Skript does not support placeholders (from plugins such as PlaceholderAPI) on its own. This means that doing "
             "something like `send \"%luckperms_prefix%\"` will give you an error. You can either find syntax that "
             "Skript supports (`player's prefix` in this example) or you can use an addon such as ["
             "skript-placeholders](https://github.com/APickledWalrus/skript-placeholders).")

        example = """
```vb
command /getprefix:
    trigger:
        send (value of placeholder "luckperms_prefix" for player) to player```
You can see more examples in [the wiki](https://github.com/APickledWalrus/skript-placeholders/wiki)!"""

        embed.add_field(name="Skript-Placeholders Example", value=example)
        self.embed = embed

    @app_commands.command(description="Embed reminding people that skript does not natively support placeholders")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def placeholders(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            embed=self.embed,
            ping=reply_to,
        )


async def setup(bot):
    await bot.add_cog(PlaceholdersCog(bot=bot))

from discord import app_commands
from discord.ext import commands
import discord
import utils


class AliasesCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Moving from Aliases to Tags", color=bot.embed_color)
        embed.description = "For more info read [SkriptLang's statement](https://github.com/SkriptLang/Skript/discussions/7349)"
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        embed.add_field(
            name="What are Aliases",
            value="Aliases were a way to add new names for blocks and items within Minecraft. They were mainly added "
                  "for convenience back when items used numerical ids so that you could use `dirt` instead of `item "
                  "3`. This is no longer necessary so this system is being phased out starting with Skript 2.10",
            inline=False
        )
        embed.add_field(
            name="What is changing?",
            value="By default aliases will not be included meaning you will have to use the default minecraft names "
                  "for blocks and items. Additionally, categories like `any log` or `is a sword` and blockdata aliases "
                  "like `waterlogged oak slab` will no longer work. To fix these issues you can switch to using "
                  "blockdata and the minecraft tag system",
            inline=False
        )

        tags_example = """
To replace category aliases like `is a sword` you can use the new [is tagged](https://docs.skriptlang.org/conditions.html?search=#CondIsTagged) condition.
`if player's tool is a sword:` becomes `if player's tool is tagged as item tag "swords":`

This doesn't work in events yet so you can check the tag inside the event:
`on click with any pickaxe:` becomes ```vb
on click:
    player's tool is tagged as item tag "pickaxes"```
    
You can also create custom tags
```vb
on load:
    register an item tag named "my_favorite_blocks" using oak log, stone, and podzol```
    
You can see a full list of default tags on the [Minecraft Wiki](https://minecraft.wiki/w/Tag#Java_Edition_2)
"""

        embed.add_field(
            name="Using minecraft tags",
            value=tags_example,
            inline=False
        )
        self.embed = embed

    @app_commands.command(description="Explains that aliases are being replaced by the tag system")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def aliases(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            embed=self.embed,
            ping=reply_to,
        )


async def setup(bot):
    await bot.add_cog(AliasesCog(bot=bot))

from discord import app_commands
from discord.ext import commands
import discord
import utils


class PdcCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Persistent Data Tags (PDC)", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        embed.add_field(
            name="What are Persistent Data Tags?",
            value="Persistent data tags (PDC) store custom data directly on players, entities, items, blocks, chunks "
                  "and worlds. Think of one as a sticky note on the object itself: put a number on a sword and it "
                  "keeps that number when you drop it or move it between inventories. That makes them the best option "
                  "for item data, since items have no id you can use in a normal variable. They need Skript 2.15 or "
                  "newer.",
            inline=False
        )
        embed.add_field(
            name="How to use them",
            value="Every tag needs a key written as `namespace:key-name`, and then you can set it with `set data tag "
                  "\"myserver:level\" of player to 5` and read it back with `data tag \"myserver:level\" of player`. "
                  "[Click Here](https://beta-docs.skriptlang.org/scripting/pdc/) to get started",
            inline=False
        )
        embed.add_field(
            name="Not NBT, not metadata",
            value="PDC tags show up in an object's NBT, but reading and writing them skips the expensive rewrite that "
                  "editing NBT causes. They also fill the same role as metadata tags while surviving restarts, "
                  "and Paper is in the process of removing metadata, so please move any metadata you have over to PDC",
            inline=False
        )
        self.embed = embed

    @app_commands.command(description="Informational embed about persistent data tags")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def pdc(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            embed=self.embed,
            ping=reply_to
        )


async def setup(bot):
    await bot.add_cog(PdcCog(bot=bot))

from discord import app_commands
from discord.ext import commands
import discord
import utils


class BlocksCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Saving blocks", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        block_example = """
```vb
on break:
    set {_block} to event-block
    wait 5 seconds
    set event-block to {_block}
    # the block will still be air```
"""
        embed.add_field(
            name="Setting a variable to a block",
            value="When you do `set {_block} to event-block` you are saving a reference to the block at that "
                  "location. Since the variable is a reference to the block in the world, any changes to the block "
                  "will also affect the variable. That is why the following code will not set the block back to its "
                  "original state." +
                  block_example,
            inline=False
        )
        blockdata_example = """
```vb
on break:
    set {_block} to blockdata of event-block
    wait 5 seconds
    set event-block to {_block}
    # the block will be regenerated```
"""
        embed.add_field(
            name="Using blockdata",
            value="To avoid this issue we can store the blockdata! Blockdata will store all of the important "
                  "information about the block including its type and rotation. Unfortunately, blockdata does not "
                  "include the location of the block." + blockdata_example,
            inline=False
        )
        location_example = """
```vb
on right click with apple:
    loop blocks in radius 3 of player:
        set {_blockdata::%loop-iteration%} to blockdata of loop-block
        set {_locations::%loop-iteration%} to location of loop-block
        set loop-block to air
    wait 5 seconds
    loop {_locations::*}:
        set block at loop-value to {_blockdata::%loop-iteration%}```
"""
        embed.add_field(
            name="Saving locations",
            value="Sometimes we still need to save the locations of the blocks even if we want to use blockdata. In "
                  "this case we can use two variables: one with our location and one with the blockdata. "
                  "Alternatively you could store these in the same list under two different indices (`"
                  "{_blocks::%common index%::location}` and `{_blocks::%common index%::blockdata}`)" + location_example,
            inline=False
        )
        self.embed = embed

    @app_commands.command(description="Informational embed about saving blocks")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def blocks(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            ping=reply_to,
            embed=self.embed
        )


async def setup(bot):
    await bot.add_cog(BlocksCog(bot=bot))

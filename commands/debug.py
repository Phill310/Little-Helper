from discord import app_commands
from discord.ext import commands
import discord

from utils import DeleteButton


class DebugCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Debug", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        embed.add_field(
            name="What is debugging?",
            value="Debugging is the process of finding and fixing bugs/issues/errors within your code. For a more "
                  "detailed explanation on proper debugging check out [sovdee's page]("
                  "https://sovdee.gitbook.io/skript-tutorials/readme/debugging)",
            inline=False
        )
        variable_example = """
Since you don't see the value of variables it can be easy to assume that everything is working properly even though that might not be the case. Variables and arguments in functions and commands might change throughout your code in unexpected ways. It is a good idea to broadcast your variables at different points in your code to confirm that the value is what you expect it to be.
```vb
on chat:
    broadcast {chats::%player's uuid%}
    add 1 to {chats::%player's uuid%}
    broadcast {chats::%player's uuid%}```
In this example we broadcast the variable to check its value before and after we add to it to make sure the value goes up. If the variable was set to a string (`set {chats::%player's uuid%} to "3"`) then we would be able to see that the value did not go up, alerting us of the issue.
"""
        embed.add_field(
            name="Variables",
            value=variable_example,
            inline=False
        )
        condition_example = """
If your code does no seem to be doing anything it is a good idea to establish which parts of your code are being executed, especially when using conditions. To accomplish this, add a broadcast after each part of line of your code with a descriptive message.
```vb
on right click:
    broadcast "player clicked"
    if player's tool = iron sword:
        broadcast "player's tool was iron sword"
        set player's tool to diamond sword```
In this example, we would only see the `player clicked` message if the player was holding an apple, alerting us that the code stopped after the first condition.
"""
        embed.add_field(
            name="Conditions",
            value=condition_example,
            inline=False
        )
        self.embed = embed

    @app_commands.command(description="Informational embed about debugging")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def debug(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
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
    await bot.add_cog(DebugCog(bot=bot))

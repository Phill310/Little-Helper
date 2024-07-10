from discord import app_commands
from discord.ext import commands
import discord


class FormatCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Formatting Code In Discord", color=0x00ff00)
        embed.set_footer(
            text=bot.embedFooter,
            icon_url=bot.embedFooterUrl
        )
        embed.add_field(
            name="Why?",
            value="Code blocks make it easier for helpers to identify potential errors -- help them help you!",
            inline=False
        )
        format_demo = """
\`\`\`vb
on chat:
    broadcast "This is how you format code!"\`\`\`
"""
        embed.add_field(
            name="The Format",
            value=format_demo,
            inline=False
        )
        format_output = """
```vb
on chat:
    broadcast "This is how you format code!"```
"""
        embed.add_field(
            name="How It Looks",
            value=format_output,
            inline=False
        )
        embed.add_field(
            name="Extra Info",
            value="On US keyboards, the grave character (`) is located above the tab key on the top left of the "
                  "keyboard",
            inline=False
        )
        self.embed = embed

    @app_commands.command(description="Informational embed about code formatting")
    @app_commands.allowed_installs(guilds=False, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def format(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(embed=self.embed)


async def setup(bot):
    await bot.add_cog(FormatCog(bot=bot))

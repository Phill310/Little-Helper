from discord import app_commands
from discord.ext import commands
import discord

from utils import DeleteButton


class EscapeCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Escaping Characters", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        embed.add_field(
            name="Why do we need to escape characters?",
            value="Some characters such as `%` and `\"` have special purposes in Skript. If we want to send one of "
                  "these special characters normally, we need to tell Skript that we don't want the character to be "
                  "used for its special purpose.",
            inline=False
        )
        embed.add_field(
            name="How to escape characters",
            value="In order to escape a character we simply double it. If I wanted to share the quote `You miss 100% "
                  "of the shots you don't take`, I could do ```\nsend \"I like this quote: \"\"You miss 100%% of the "
                  "shots you don't take\"\" - Wayne Gretzky\"```"
        )
        self.embed = embed

    @app_commands.command(description="Informational embed about escaping characters")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def escape(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
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
    await bot.add_cog(EscapeCog(bot=bot))

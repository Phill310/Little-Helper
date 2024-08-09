from discord import app_commands
from discord.ext import commands
import discord
from utils import DeleteButton


class SpoonFeedCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Spoonfeeding", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        embed.add_field(
            name="What is spoonfeeding?",
            value="When a person trying to help someone sends the entire code/solution the other person needs without "
                  "letting them figure it out and learn it themselves it is considered spoonfeeding.",
            inline=False
        )
        embed.add_field(
            name="Why is this a bad thing?",
            value="This becomes an issue because the person seeking help does not learn anything. When they are "
                  "handed the code it is just a simple copy and paste to fix their issue rather than applying and "
                  "gaining knowledge so that they can fix the issue on their own. This also develops a reliance on "
                  "getting code from others leading to them wanting and needing to get spoonfed again",
            inline=False
        )
        embed.add_field(
            name="What can I do instead?",
            value="It is better to suggest ideas and make a plan on how to solve their issue, helping them walk "
                  "through the process of fixing their code. This can involve sending link to relevant documentation "
                  "or suggestion syntax",
            inline=False
        )
        self.embed = embed

    @app_commands.command(description="Informational embed about spoonfeeding")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def spoonfeed(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
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
    await bot.add_cog(SpoonFeedCog(bot=bot))

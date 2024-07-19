from discord import app_commands
from discord.ext import commands
import discord
from utils import DeleteButton


class GettingHelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="How to get help", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        embed.add_field(
            name="What to send",
            value="Once you are ready to ask your question make sure you also send some helpful information such "
                  "as:\n- your code\n- a picture of any errors\n- a picture of /sk info\nAdditionally, "
                  "it is important that you actually describe your issue rather than just stating that your code does "
                  "not work or just telling us to fix it",
            inline=False
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/138027100593455104/803204210291245075/image0.png")
        self.embed = embed

    @app_commands.command(name="getting-help", description="What to do when you want to ask for help")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def getting_help(self, interaction: discord.Interaction, reply_to: discord.Member = None) -> None:
        await interaction.response.send_message(
            content=(f"Please read this embed {reply_to.mention}" if reply_to is not None else ""),
            embed=self.embed,
            view=DeleteButton(interaction.user.id)
        )


async def setup(bot):
    await bot.add_cog(GettingHelpCog(bot=bot))

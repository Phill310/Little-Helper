from discord import app_commands
from discord.ext import commands
import discord


class SaladCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @app_commands.command(description="DO NOT DISTURB THE SALAD")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def salad(self, interaction: discord.Interaction) -> None:
        if interaction.channel_id == 171726362388725760:
            await interaction.response.send_message(content="DO NOT DISTURB THE SALAD")
            await interaction.channel.send(content="https://media1.tenor.com/m/A3z9MU9YTBQAAAAC/salad-mix.gif")
        else:
            await interaction.response.send_message(content="You can only use this in <#171726362388725760>", ephemeral=True)


async def setup(bot):
    await bot.add_cog(SaladCog(bot=bot))

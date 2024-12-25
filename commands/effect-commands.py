from discord import app_commands
from discord.ext import commands
import discord
import utils


class EffectCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Effect Commands", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        embed.add_field(
            name="What are Effect Commands?",
            value="Effect commands allow you to use Skript effects ingame through your chat. By default these "
                  "messages have to start with `!` but are not enabled. They can be very useful for debugging and "
                  "making simple changes without leaving your game.",
            inline=False
        )
        embed.add_field(
            name="How to enable Effect Commands",
            value="Start by locating the configuration file for Skript (`plugins -> Skript -> config.sk`). In the file "
                  "you can search for `enable effect commands`. It should be around line 60. Set this value to `true` "
                  "to enable effect commands. At this point only people with the `permission 'skript.effectcommands'` "
                  "will be able to use effect commands (OPs will not be able to). If you want to allows OPs to use "
                  "effect commands scroll down to the next paragraph and set `allow ops to use effect commands` to "
                  "`true`.",
            inline=False
        )
        embed.add_field(
            name="Be careful",
            value="Just like scripts, effect commands can be used to cause a lot of damage to your server and even "
                  "crash it. Only let people you trust use effect commands.",
            inline=False
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/1317215749739380897/1317215767233822720/image.png")
        self.embed = embed

    @app_commands.command(description="Informational embed about Effect Commands")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def effect_commands(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            embed=self.embed,
            ping=reply_to,
        )


async def setup(bot):
    await bot.add_cog(EffectCommandsCog(bot=bot))

import discord
from discord.ext import commands
import os


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            intents=discord.Intents.all(),
            command_prefix=".",
            help_command=None,
            owner_id=415356187161395201
        )

    async def setup_hook(self):
        print("Setting up commands:")
        for file in os.listdir("./commands"):
            if file.endswith(".py"):
                print(f" - Loading {file[:-3]}")
                await self.load_extension(f"commands.{file[:-3]}")

    async def on_ready(self):
        print('------')
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


bot = MyBot()
bot.embed_footer = "Send any suggestions to @the.phill"
bot.embed_footer_url = "https://cdn.discordapp.com/avatars/415356187161395201/569b991411c0d9096a208f58146320b8.webp"
bot.embed_color = 0x00ff00


@bot.command()
@commands.is_owner()
async def sync(ctx: commands.Context, guild: str = None) -> None:
    if guild is None:
        await bot.tree.sync()
        await ctx.send(content="Synced commands globally", delete_after=3)
    else:
        await bot.tree.sync(guild=ctx.guild)
        await ctx.send(content=f"Synced commands for `{ctx.guild.name}`", delete_after=3)
    await ctx.message.delete()


@sync.error
async def sync_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        print(f"{ctx.author} tried to use sync!")


@bot.command()
async def help(ctx) -> None:
    await ctx.reply("We have switched to slash commands! You can see all of the available commands and their descriptions by typing /")


bot.run(os.environ['DISCORD_TOKEN'])

import discord
from discord.ext import commands
import os
import sys
import traceback


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            intents=discord.Intents.all(),
            command_prefix=".",
            help_command=None,
            owner_id=415356187161395201
        )
        self.old_commands = dict.fromkeys(["download", "dl", "down", "downloads"], "</download:1261180973580685333>")
        self.old_commands.update(dict.fromkeys(["%", "percent", "percents"], "</percent:1260033213204791389>"))
        self.old_commands.update(dict.fromkeys(["format", "formatting"], "</format:1260036961910001674>"))
        self.old_commands.update(dict.fromkeys(["list", "lists"], "</lists:1260118293419786261>"))
        self.old_commands.update(dict.fromkeys(["uuid", "uuids"], "</uuids:1263654687022911655>"))

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

    async def on_command_error(self, ctx, exception) -> None:
        if isinstance(exception, commands.CommandNotFound):
            if ctx.message.content[1:] in self.old_commands:
                await ctx.reply(f"We have moved on to slash commands! Please use {self.old_commands[ctx.message.content[1:]]}")
                return
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(exception), exception, exception.__traceback__, file=sys.stderr)


bot = MyBot()
bot.embed_footer = "Send any suggestions to @the.phill"
bot.embed_footer_url = "https://cdn.discordapp.com/avatars/415356187161395201/569b991411c0d9096a208f58146320b8.webp"
bot.embed_color = 0x00ff00
bot.default_message = "{user} suggests that you read {message} {ping}"


@bot.command()
@commands.is_owner()
async def sync(ctx: commands.Context) -> None:
    await bot.tree.sync()
    await ctx.send(content="Synced commands globally", delete_after=3)
    await ctx.message.delete()


@sync.error
async def sync_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        print(f"{ctx.author} tried to use sync!")
    else:
        raise error


@bot.command(aliases=["r", "reset"])
@commands.is_owner()
async def reload(ctx: commands.Context, command: str = None) -> None:
    await ctx.message.delete()
    if command is None:
        await ctx.send("Please specify a command to reload:\n`" + "`, `".join(bot.extensions).replace("commands.", "") + "`", delete_after=10)
    else:
        try:
            await bot.reload_extension(f"commands.{command}")
        except Exception as e:
            await ctx.send(f"Ran into an error while reloading `{command}`: ```{e}```", delete_after=30)
        else:
            await ctx.send(content=f"Reloaded `{command}`", delete_after=3)


@bot.command()
async def help(ctx) -> None:
    await ctx.reply("We have switched to slash commands! You can see all of the available commands and their descriptions by typing /")


bot.run(os.environ['DISCORD_TOKEN'])

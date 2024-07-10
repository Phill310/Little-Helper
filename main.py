import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional
import os


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            intents=discord.Intents.none(),
            command_prefix="-"
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
bot.embedFooter = "Send any suggestions to @the.phill"
bot.embedFooterUrl = "https://cdn.discordapp.com/avatars/415356187161395201/569b991411c0d9096a208f58146320b8.webp"


@app_commands.command(name="sync", description="Sync app commands")
@app_commands.allowed_installs(guilds=False, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(guild='The guild you want to sync')
@commands.is_owner()
async def sync(interaction: discord.Interaction, guild: Optional[discord.TextChannel] = None) -> None:
    if guild is None:
        await bot.tree.sync()
        await interaction.response.send_message(ephemeral=True, content="Synced all")
    else:
        await bot.tree.sync(guild=guild.guild)
        await interaction.response.send_message(ephemeral=True, content=f"Synced for {guild.guild}")


@app_commands.command(name="reload", description="Reload a command")
@app_commands.describe(command="The command to reload")
@app_commands.allowed_installs(guilds=False, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@commands.is_owner()
async def reloadcommand(interaction: discord.Interaction, command: str) -> None:
    if command == "*":
        result = []
        for file in os.listdir("./commands"):
            if file.endswith(".py"):
                try:
                    await bot.reload_extension("commands." + file[:-3])
                except Exception as e:
                    result.append(f"Failed to reload `{file[:-3]}`: ```{e}```")
                else:
                    result.append(f"Reloaded `{file[:-3]}`")
        await interaction.response.send_message(ephemeral=True, content="\n".join(result))
    else:
        try:
            await bot.reload_extension("commands." + command)
        except Exception as e:
            await interaction.response.send_message(ephemeral=True, content=f"Failed to reload `{command}`: ```{e}```")
        else:
            await interaction.response.send_message(ephemeral=True, content=f"Reloaded `{command}`")


@reloadcommand.autocomplete("command")
async def autocomplete(interaction: discord.Interaction, current: str):
    cogs = [app_commands.Choice(name="*",value="*")]
    for file in os.listdir("./commands"):
        if file.endswith(".py") and file.startswith(current):
            cogs.append(app_commands.Choice(name=file[:-3], value=file[:-3]))
    return cogs


@app_commands.command(name="load", description="Load a command")
@app_commands.describe(command="The command to load")
@app_commands.allowed_installs(guilds=False, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@commands.is_owner()
async def loadcommand(interaction: discord.Interaction, command: str) -> None:
    try:
        await bot.reload_extension("commands." + command)
    except Exception as e:
        await interaction.response.send_message(ephemeral=True, content=f"Failed to load `{command}`: ```{e}```")
    else:
        await interaction.response.send_message(ephemeral=True, content=f"Loaded `{command}`")


bot.tree.add_command(loadcommand)
bot.tree.add_command(reloadcommand)
bot.tree.add_command(sync)


token = open("token.txt", "r")
bot.run(token.read())

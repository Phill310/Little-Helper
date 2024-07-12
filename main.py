import discord
from discord.ext import commands
from discord import app_commands
import os


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            intents=discord.Intents.none(),
            command_prefix="/",
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


@app_commands.command(name="sync", description="Sync app commands")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.describe(guild='Id of the guild')
async def sync(interaction: discord.Interaction, guild: str = None) -> None:
    if interaction.user.id != bot.owner_id:
        await interaction.response.send_message(ephemeral=True, content="You do not have permission to use this command.")
        return
    if guild is None:
        await bot.tree.sync()
        await interaction.response.send_message(ephemeral=True, content="Synced commands globally")
    else:
        id = int(guild)
        await bot.tree.sync(guild=discord.Object(id=id))
        await interaction.response.send_message(ephemeral=True, content=f"Synced commands for `{id}`")


@sync.autocomplete("guild")
async def sync_autocomplete(interaction: discord.Interaction, current: str):
    if interaction.user.id != bot.owner_id:
        return []
    return [app_commands.Choice(name="Phill's Bot Server", value="824851662102331423"), app_commands.Choice(name="skUnity", value="135877399391764480")]


@app_commands.command(name="reload", description="Reload a command")
@app_commands.describe(command="The command to reload")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def reloadcommand(interaction: discord.Interaction, command: str) -> None:
    if interaction.user.id != bot.owner_id:
        await interaction.response.send_message(ephemeral=True, content="You do not have permission to use this command.")
        return
    await interaction.response.defer(ephemeral=True, thinking=True)
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
        await interaction.edit_original_response(content="\n".join(result))
    else:
        try:
            await bot.reload_extension("commands." + command)
        except Exception as e:
            await interaction.edit_original_response(content=f"Failed to reload `{command}`: ```{e}```")
        else:
            await interaction.edit_original_response(content=f"Reloaded `{command}`")


@reloadcommand.autocomplete("command")
async def reload_autocomplete(interaction: discord.Interaction, current: str):
    if interaction.user.id != bot.owner_id:
        return []
    cogs = []
    if current == "":
        cogs.append(app_commands.Choice(name="*",value="*"))
    for file in os.listdir("./commands"):
        if file.endswith(".py") and file.startswith(current):
            cogs.append(app_commands.Choice(name=file[:-3], value=file[:-3]))
    return cogs


@app_commands.command(name="load", description="Load a command")
@app_commands.describe(command="The command to load")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def loadcommand(interaction: discord.Interaction, command: str) -> None:
    if interaction.user.id != bot.owner_id:
        await interaction.response.send_message(ephemeral=True, content="You do not have permission to use this command.")
        return
    try:
        await bot.load_extension("commands." + command)
    except Exception as e:
        await interaction.response.send_message(ephemeral=True, content=f"Failed to load `{command}`: ```{e}```")
    else:
        await interaction.response.send_message(ephemeral=True, content=f"Loaded `{command}`")


bot.tree.add_command(loadcommand)
bot.tree.add_command(reloadcommand)
bot.tree.add_command(sync)


token = open("tokens.txt", "r")
bot.run(token.readlines()[0])

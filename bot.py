from typing import Optional

import discord
from discord import app_commands

client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

@tree.command(description="Informational embed about debugging")
@app_commands.allowed_installs(guilds=False, users=True) # users only, no guilds for install
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True) # all allowed
async def debug(interaction: discord.Interaction) -> None:
    embed = discord.Embed(title="Debug", color=0x00ff00)
    embed.set_footer(text="Send any suggestions to @the.phill", icon_url="https://cdn.discordapp.com/avatars/415356187161395201/569b991411c0d9096a208f58146320b8.webp")
    embed.add_field(name="What is debugging?", value="Debugging is the process of finding and fixing bugs/issues/errors within your code. For a more detailed explanation on proper debugging check out [sovdee's page](https://sovdee.gitbook.io/skript-tutorials/readme/debugging)", inline=False)
    msg = """
Since you don't see the value of variables it can be easy to assume that everything is working properly even though that might not be the case. Variables and arguments in functions and commands might change throughout your code in unexpected ways. It is a good idea to broadcast your variables at different points in your code to confirm that the value is what you expect it to be.
```vb
on chat:
	broadcast {chats::%player's uuid%}
	add 1 to {chats::%player's uuid%}
	broadcast {chats::%player's uuid%}```
In this example we broadcast the variable to check its value before and after we add to it to make sure the value goes up. If the variable was set to a string (`set {chats::%player's uuid%} to "3"`) then we would be able to see that the value did not go up, alerting us of the issue.
"""
    embed.add_field(name="Variables", value=msg, inline=False)
    msg = """
If your code does no seem to be doing anything it is a good idea to establish which parts of your code are being executed, especially when using conditions. To accomplish this, add a broadcast after each part of line of your code with a descriptive message.
```vb
on right click:
	broadcast "player clicked"
	if player's tool = iron sword:
		broadcast "player's tool was iron sword"
		set player's tool to diamond sword```
In this example, we would only see the `player clicked` message if the player was holding an apple, alerting us that the code stopped after the first condition.
"""
    embed.add_field(name="Conditions", value=msg, inline=False)
    await interaction.response.send_message(embed=embed)

@tree.command(description="Informational embed about using %")
@app_commands.allowed_installs(guilds=False, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def percent(interaction: discord.Interaction) -> None:
    embed = discord.Embed(title="Percent signs (%)", color=0x00ff00)
    embed.add_field(name="When should percent signs be used in Skript?", value="In Skript, the purpose of surrounding an expression in % signs is letting Skript know you want it to be parsed as an expression and insert its value into the string or variable you've put it in.", inline=False)
    msg = """
```vb
give dirt to %player%
send "Hey there player" to %arg-1%
kill %{_entity}%```
Here, the % signs are not inside strings or variable names and should therefore be removed.
"""
    embed.add_field(name="Incorrect Usage", value=msg, inline=False)
    msg = """
```vb
broadcast "%player% has joined"
send "%{_variable::*}%" to player
set {_variable::%uuid of player%} to 10```
Here, the % signs are being use properly, as a means to put expressions inside strings and variable names.
"""
    embed.add_field(name="Correct Usage", value=msg, inline=False)
    await interaction.response.send_message(embed=embed)

@tree.command(description="Informational embed about code formatting")
@app_commands.allowed_installs(guilds=False, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def format(interaction: discord.Interaction) -> None:
    embed = discord.Embed(title="Formatting Code In Discord", color=0x00ff00)
    embed.add_field(name="Why?", value="Code blocks make it easier for helpers to identify potential errors -- help them help you!", inline=False)
    msg = """
\`\`\`vb
on chat:
	broadcast "This is how you format code!"\`\`\`
"""
    embed.add_field(name="The Format", value=msg, inline=False)
    msg = """
```vb
on chat:
	broadcast "This is how you format code!"```
"""
    embed.add_field(name="How It Looks", value=msg, inline=False)
    embed.add_field(name="Extra Info", value="On US keyboards, the grave character (`) is located above the tab key on the top left of the keyboard", inline=False)
    await interaction.response.send_message(embed=embed)

@tree.command(description="Informational embed about list variables")
@app_commands.allowed_installs(guilds=False, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def lists(interaction: discord.Interaction) -> None:
    embed = discord.Embed(title="List Variables", color=0x00ff00)
    embed.add_field(name="Why?", value="List variables are a much cleaner way of storing multiple values, especially objects that are unique to something (the money of a player, the warps of the server), as they can be looped, added to, removed from, accessed, and deleted all at once, making variable organization a breeze. A list basically maps objects to their corresponding unique indices.", inline=False)
    msg = """
To make a list, we simply use the list variable separator `::` in the variable's name: `{money::%uuid of player%}`, `{warps::%{_warpName}%}`, `{luckyNumbers::*}`.
For example:
```
set {_list::*} to 1, 2, 3, and 4
set {_list::%uuid of player%} to player```
"""
    embed.add_field(name="How to create a list variable?", value=msg, inline=False)
    embed.add_field(name="Indices and values", value="As already mentioned, lists have indices and values. For instance, in `set {money::%uuid of player%} to 100` the index is the uuid of the player and the value is 100. We can also access all the values at once by using `::*`. This last part means we can replace a lot of common loops with simple lists, like `send \"You're on team red!\" to {team-red::*}` instead of looping through all players and checking if each one is on team red.", inline=False)
    msg = """
```vb
{%player%.money} -> {money::%player's uuid%}
{home.warps.%player%} -> {warps::%player's uuid%::home}
{%player%.cooldown} -> {cooldown::%player's uuid%}```
"""
    embed.add_field(name="Common situations which can use lists instead", value=msg, inline=False)
    await interaction.response.send_message(embed=embed)

@tree.command(description="Links to cooldown tutorial")
@app_commands.allowed_installs(guilds=False, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def cooldowns(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(content="[Custom Cooldown Tutorial](https://docs.skunity.com/guides/tutorial/19354)")

@tree.command(name="try", description="Try it and see video")
@app_commands.describe(member='The member you want to ping')
@app_commands.allowed_installs(guilds=False, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def tryandsee(interaction: discord.Interaction, member: Optional[discord.Member] = None) -> None:
    msg = "why don't you [try it and see](https://tryitands.ee)"
    if member != None:
        msg = msg + " " + member.mention
    await interaction.response.send_message(content=msg)

@app_commands.allowed_installs(guilds=False, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
class Sovdee(app_commands.Group):
    @app_commands.command(name="global-local", description="Global vs Local variables tutorial")
    async def gvars(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovdee's Global vs Local Variable tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/variables/global-and-local)")

    @app_commands.command(name="variables", description="Variable tutorials")
    async def vars(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovdee's Variable Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/variables)")

    @app_commands.command(description="Home page of Sovdee's tutorials")
    async def home(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="https://sovdee.gitbook.io/skript-tutorials/")

    @app_commands.command(name="indentation", description="Indentation and Program Flow")
    async def indent(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovdee's Indentation Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/indentation)")

    @app_commands.command(name="commands", description="Custom Commands")
    async def commands(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovdee's Custom Command Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/commands)")

    @app_commands.command(name="vectors", description="Vector tutorials")
    async def vectors(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content="[Sovdee's Vector tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/vectors)")

tree.add_command(Sovdee())

@client.event
async def on_ready():
    print('------')
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.event
async def on_message(message):
    if message.author.id != 415356187161395201:
        return
    if message.content == ("!sync"):
        await tree.sync()
        await message.reply("Synced all")
    elif message.content == "!sync guild":
        await tree.sync(guild=message.guild)
        await message.reply("Synced this guild")

f = open("token.text", "r")
client.run(f.read())
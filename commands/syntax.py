from discord import app_commands
from discord.ext import commands
import discord


class SyntaxPages(discord.ui.View):
    def __init__(self, bot, user_ids: list[int], embeds):
        super().__init__(timeout=None)
        self.embeds = embeds
        self.user_ids = user_ids
        self.user_ids.append(bot.owner_id)
        self.bot = bot

    async def click(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id in self.user_ids:
            for child in self.children:
                if isinstance(child, discord.ui.Button) and child.disabled:
                    child.disabled = False
            button.disabled = True
            await interaction.message.edit(embed=self.embeds[button.label], view=self)
        await interaction.response.defer()

    @discord.ui.button(label="Structure", style=discord.ButtonStyle.blurple, disabled=True)
    async def structure_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.click(interaction, button)

    @discord.ui.button(label="Effect", style=discord.ButtonStyle.blurple)
    async def effect_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.click(interaction, button)

    @discord.ui.button(label="Expression", style=discord.ButtonStyle.blurple)
    async def expression_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.click(interaction, button)

    @discord.ui.button(label="Condition", style=discord.ButtonStyle.blurple)
    async def condition_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.click(interaction, button)

    @discord.ui.button(label="Section", style=discord.ButtonStyle.blurple)
    async def section_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.click(interaction, button)

    @discord.ui.button(label="", style=discord.ButtonStyle.grey, emoji="❌")
    async def delete_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id in self.user_ids:
            await interaction.message.delete()
        else:
            await interaction.response.defer()


class SyntaxCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.embeds = {}
        template = discord.Embed(
            title="Skript Syntaxes ",
            description="If you want a more in depth explanation or need to learn how to read syntax please read "
                        "[this article](https://sovdee.gitbook.io/skript-tutorials/readme/syntax-overview)",
            color=bot.embed_color
        )
        template.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )

        """ Structure Embed """
        structure_embed = template.copy()
        structure_embed.title += "(Structure)"
        structure_embed.description += ("\n\nStructures are the base of any code you write in Skript. All code you "
                                        "write will be inside a structure. Structures will never have indentation "
                                        "before them (they are the left most lines of code).")
        event_example = """
An event represents actions that occur in the game such as breaking and placing blocks
```vb
# called when a player breaks a block
on break:

# called when a player places stone
on place of stone:

# called when an entity dies
on death:```
"""
        structure_embed.add_field(
            name="Event",
            value=event_example,
            inline=False
        )

        command_example = """
The command structure allows you to make custom commands that you can run ingame. For more information read [Sovde's Custom Command Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/commands)
```vb
# says Hello to you
command /hello:
    trigger:
        send "Hello" to player```
"""
        structure_embed.add_field(
            name="Command",
            value=command_example,
            inline=False
        )

        function_example = """
Function structures allow you to create chunks of code that can be reused across all of your scripts. For more information read [Sovde's Function Tutorial](https://sovdee.gitbook.io/skript-tutorials/core-concepts/indentation/functions)
```vb
# says Hello World to everyone
function hello():
    broadcast "Hello World"```
"""
        structure_embed.add_field(
            name="Function",
            value=function_example,
            inline=False
        )
        self.embeds["Structure"] = structure_embed

        """ Effect Embed """
        effect_embed = template.copy()
        effect_embed.title += "(Effect)"
        effect_embed.add_field(
            name="What is an effect?",
            value="Effects cause changes to your game. They are often verbs (`teleport`, `send`) and usually have "
                  "missing parts (words surrounded in %) that you must fill in. You will only ever have 1 effect per "
                  "line of code.",
            inline=True
        )
        effect_example = """
```vb
# teleport syntax from the docs
[(force)] teleport %entities% (to|%direction%) %location%

# filled in version that teleports the player to spawn
teleport player to spawn of world "world"```
"""
        effect_embed.add_field(
            name="Example",
            value=effect_example,
            inline=False
        )
        self.embeds["Effect"] = effect_embed

        """ Expression Embed """
        expression_embed = template.copy()
        expression_embed.title += "(Expression)"
        expression_embed.add_field(
            name="What is an expression?",
            value="Expressions are used to fill in the blanks in effects. They can be nouns like `player` or "
                  "adjectives that describe another expression like `level of player`. ",
            inline=False
        )
        expression_example = """
```vb
# simple expressions
event-player # or just player
the drops
exploded blocks

# combined expressions
name of %item%
event-entity's location
player's tool```
"""
        expression_embed.add_field(
            name="Example",
            value=expression_example,
            inline=False
        )
        self.embeds["Expression"] = expression_embed

        """ Condition Embed """
        condition_embed = template.copy()
        condition_embed.title += "(Condition)"
        condition_embed.add_field(
            name="What is a condition?",
            value="Conditions (if statements) will almost always start with `if` and end with `:`. They are used to "
                  "compare two things (`if level of player > 5:`) or check a property of something (`if player is "
                  "alive:`). Conditions are used to control which code gets executed. You can follow an if with `else "
                  "if %condition%:` in order to use another condition only if the first one is false. If you only put "
                  "`else:` the following code will run if all the preceding conditions are met.",
            inline=False
        )
        condition_example = """
comparing two things
```vb
if player's tool is apple:
    broadcast "You are holding an apple"
else if player's tool is diamond:
    # this code only runs if the player is not holding an apple but is holding a diamond
    broadcast "You are holding an diamond"
else:
    # this code only runs if the player is holding neither an apple nor diamond
    broadcast "You were not holding an apple or a diamond"```
checking a property
```vb
if player is alive:
    broadcast "You survived!"
else:
    # this code only runs if the player is not alive
    broadcast "You didn't make it :("```
multi line conditions
```vb
if any:
    player's level > 10
    {rank::%player's uuid%} is "ranger"
    player has permission "bypass"
then:
    broadcast "You may enter"
else:
    broadcast "Thou shall not pass!"```
"""
        condition_embed.add_field(
            name="Example",
            value=condition_example,
            inline=False
        )
        self.embeds["Condition"] = condition_embed

        """ Section Embed """
        section_embed = template.copy()
        section_embed.title += "(Section)"
        section_embed.add_field(
            name="What is a section?",
            value="All sections (such as conditions) will end with a `:`. If lines after the section are indented one "
                  "level further than the section, they are considered to be a part of the section. These lines will "
                  "be affected by the section.",
            inline=True
        )
        section_example = """
```vb
if size of {zombies::*} < 10:
    spawn a zombie at {zombie_spawn}:
        set the zombie's helmet to an iron helmet
        set the zombie's display name to "Minion"
    broadcast "A new zombie has spawned!```
"""
        section_example += ("There are 2 levels of indentation meaning there are 2 sections. The first section is our "
                            "condition. If there are 10 or more zombies then all of the code inside the condition ("
                            "the spawn section and the broadcast) will be skipped. The spawn section allows you to "
                            "modify the entity you are about to spawn before it actually gets spawned. Once all of "
                            "the code inside the spawn section has ran we continue to the code outside of it (the "
                            "broadcast)")
        section_embed.add_field(
            name="Example",
            value=section_example,
            inline=False
        )
        self.embeds["Section"] = section_embed

    @app_commands.command(description="Informational embed about the syntax types")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def syntax(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        ids = [interaction.user.id]
        if reply_to is not None:
            ids.append(reply_to.id)
        await interaction.response.send_message(
            content=self.bot.default_message.format(
                ping="" if reply_to is None else reply_to.mention,
                user=interaction.user.display_name,
                message="this embed"
            ),
            embed=self.embeds["Structure"],
            view=SyntaxPages(self.bot, ids, self.embeds))


async def setup(bot):
    await bot.add_cog(SyntaxCog(bot=bot))

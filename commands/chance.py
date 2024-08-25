from discord import app_commands
from discord.ext import commands
import discord
import utils


class ChanceCog(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        embed = discord.Embed(title="Using Chance", color=bot.embed_color)
        embed.set_footer(
            text=bot.embed_footer,
            icon_url=bot.embed_footer_url
        )
        embed.add_field(
            name="Leaving things up to fate",
            value="There are two main ways of adding some randomness to your code. The simple way to achieve this is "
                  "by using the `chance of` condition. This condition will only pass a specified percent of the time. "
                  "The other option is to generate a random number and check if the generated number falls within a "
                  "certain range.",
            inline=False
        )
        chance_of_example = """
```vb
chance of 50%:
    give player diamond

if chance of 25%:
    send "you win!" to player
else:
    send "you lose!" to player```
"""
        embed.add_field(
            name="Chance of condition",
            value="This condition is great for making independent chances. You can combine it with an `else` to make "
                  "sure that something happens if the condition does not pass." + chance_of_example,
            inline=False
        )
        chance_problem_example = """
```vb
if chance of 20%:
    # This will happen 20% of the time
else if chance of 50%:
    # This will happen 40% of the time
else if chance of 10%:
    # This will happen 4% of the time
else if chance of 50%:
    # This will happen 18% of the time
else:
    # This will happen 18% of the time```
"""
        embed.add_field(
            name="Problems with chance of",
            value="While the chance of condition works well for simple conditions (mainly binomial probabilities), "
                  "the math becomes a lot more complicated as you try to add more outcomes." + chance_problem_example +
                  "See how confusing that can get?",
            inline=False
        )
        random_number_example = """
```vb
set {_rand} to random integer between 1 and 100
if {_rand} is between 1 and 10:
    # This will happen 10% of the time
else if {_rand} is between 11 and 60:
    # This will happen 50% of the time
else if {_rand} is 61:
    # This will happen 1% of the time
else:
    # This will happen 39% of the time```
"""
        embed.add_field(
            name="Random Integer",
            value="To avoid the confusion of calculating each individual probability we can generate one random "
                  "number and check if it falls within a certain range for each condition. If we generate and integer "
                  "between 1 and 100 each number you add to a range will make it 1% more likely to occur." +
                  random_number_example,
            inline=False
        )
        self.embed = embed

    @app_commands.command(name="chance", description="Informational embed about implementing chances")
    @app_commands.describe(reply_to="The user you want to send this message to")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def chance_embed(self, interaction: discord.Interaction, reply_to: discord.User = None) -> None:
        await utils.send(
            interaction=interaction,
            ping=reply_to,
            embed=self.embed
        )


async def setup(bot):
    await bot.add_cog(ChanceCog(bot=bot))

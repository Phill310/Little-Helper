import discord
import time


class DeleteButton(discord.ui.View):
    def __init__(self, user_id):
        super().__init__(timeout=None)
        self.user_id = user_id

    @discord.ui.button(label="", style=discord.ButtonStyle.grey, emoji="❌")
    async def delete_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id in [self.user_id, interaction.client.owner_id]:
            await interaction.message.delete()
        else:
            await interaction.response.defer()


last_used = {}


async def send(interaction: discord.Interaction, content: str = None, message: str = "this embed", embed: discord.Embed = None,
               ephemeral: bool = False, view: discord.ui.View = None, ping: discord.User = None, deferred: bool = False):
    """ Replies to an interaction (app command)

    :param interaction: The interation that is being replied to
    :param content: Set the content of the message (default message is used if this is not set)
    :param message: Set the message placeholder in the default message
    :param embed: The embed that is sent with the message
    :param ephemeral: Set the ephemeral flag
    :param view: Add a custom view to the response (defaults to delete button view)
    :param ping: Specify a user to ping
    :param deferred: Specify if this response has already been responded to
    """
    view = view or DeleteButton(interaction.user.id)
    ping = "" if ping is None else ping.mention
    if content is None:
        content = "{user} suggests that you read {message} {ping}".format(
            ping=ping,
            user=interaction.user.display_name,
            message=message
        )
    else:
        content = content + " " + ping
    if not ephemeral:
        if (interaction.channel.id in last_used) and (last_used[interaction.channel.id] + 10 > time.time()):
            ephemeral = True
            view = discord.ui.View()
            content = "**Your message was hidden because someone requested it recently**\n\n" + content
        else:
            last_used[interaction.channel.id] = round(time.time())
    if deferred:
        await interaction.followup.send(
            content=content,
            embed=embed,
            ephemeral=ephemeral,
            view=view
        )
    else:
        await interaction.response.send_message(
            content=content,
            embed=embed,
            ephemeral=ephemeral,
            view=view
        )
    if len(last_used) >= 50:
        last_used.clear()
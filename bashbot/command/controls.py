from discord import Message
from discord.ext import commands

from bashbot.command import session_exists, has_permission
from bashbot.terminal.sessions import sessions
from bashbot.terminal.terminal import Terminal


class ControlsCommand(commands.Cog):
    @commands.group(name='.controls')
    async def controls(self, ctx):
        if ctx.invoked_subcommand is None:
            pass

    @controls.command()
    @session_exists()
    @has_permission('input.controls.manage')
    async def add(self, ctx, emoji_id, content):
        terminal: Terminal = sessions().get_by_channel(ctx.channel)
        message: Message = sessions().get_message(terminal)

        terminal.add_control(emoji_id, content)
        await message.add_reaction(emoji_id)

    @controls.command()
    @session_exists()
    @has_permission('input.controls.manage')
    async def remove(self, ctx, emoji_id):
        terminal: Terminal = sessions().get_by_channel(ctx.channel)
        message: Message = sessions().get_message(terminal)

        terminal.remove_control(emoji_id)
        await message.remove_reaction(emoji_id, message.author)

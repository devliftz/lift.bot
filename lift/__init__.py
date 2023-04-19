import discord
from discord.ext import commands

from lift import gradient

bot = commands.Bot(command_prefix="?", help_command=None, self_bot=True)

def login(token):
    bot.run(token=f"{token}", log_handler=None)
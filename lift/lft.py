import discord
from discord.ext import commands

from lift.gradient import Colorate, Colors
import lift.status

bot = commands.Bot(command_prefix="?", help_command=None, intents=discord.Intents().all())
print(Colorate.Horizontal(Colors.red_to_yellow, f"""


                                      ██╗     ██╗███████╗████████╗
                                      ██║     ██║██╔════╝╚══██╔══╝
                                      ██║     ██║█████╗     ██║   
                                      ██║     ██║██╔══╝     ██║   
                                      ███████╗██║██║        ██║   
                                      ╚══════╝╚═╝╚═╝        ╚═╝   
                                                
                                        
     ┌────────────────────────────────────────────────────────────────────────────────────────┐
                      Current Version: 14.1.3 | You`re using the latest version
     └────────────────────────────────────────────────────────────────────────────────────────┘
     
     """))

@bot.event
async def on_command(ctx):
    print(Colorate.Horizontal(Colors.red_to_yellow, f"""
    ┌────────────────────────────────────────────────────┐
      Command: {ctx.command.name}
      Server: {ctx.author.guild.name} ID: {ctx.author.guild.id}
      User: {ctx.author.name}
    └────────────────────────────────────────────────────┘
    """))


def login(token):
    bot.run(token=f"{token}", log_handler=None)
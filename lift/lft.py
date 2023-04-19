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
                      Current Version: 14.0.1 | You`re using the latest version
     └────────────────────────────────────────────────────────────────────────────────────────┘
     
     """))

@bot.event
async def on_command(ctx):
    print(Colorate.Horizontal(Colors.red_to_yellow, f"     Command {ctx.command.name} was used by {ctx.author.name}#{ctx.author.discriminator}"))


def login(token):
    bot.run(token=f"{token}", log_handler=None)
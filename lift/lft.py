import discord
from discord.ext import commands

from lift.gradient import Colorate, Colors

bot = commands.Bot(command_prefix="?", help_command=None, intents=discord.Intents().all())
print(Colorate.Horizontal(Colors.red_to_yellow, f"""


                                      ██╗     ██╗███████╗████████╗
                                      ██║     ██║██╔════╝╚══██╔══╝
                                      ██║     ██║█████╗     ██║   
                                      ██║     ██║██╔══╝     ██║   
                                      ███████╗██║██║        ██║   
                                      ╚══════╝╚═╝╚═╝        ╚═╝   
                                                
                                        
     ┌────────────────────────────────────────────────────────────────────────────────────────┐
                      Current Version: 13.9.7 | You`re using the latest version
     └────────────────────────────────────────────────────────────────────────────────────────┘
     
     """))

@bot.event
async def on_command(ctx):
    print(Colorate.Horizontal(Colors.red_to_yellow, f"       Command {ctx.command.name} was used by {ctx.author.name}#{ctx.author.discriminator}"))


def login(token):
    bot.run(token=f"{token}", log_handler=None)
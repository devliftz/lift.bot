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
                      Current Version: 13.7.5 | You`re using the latest version
     └────────────────────────────────────────────────────────────────────────────────────────┘"""))



def login(token):
    bot.run(token=f"{token}", log_handler=None)
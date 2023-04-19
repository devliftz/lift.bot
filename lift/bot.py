import discord
from discord.ext import commands

from lift.gradient import Colorate, Colors

bot = commands.Bot(command_prefix="?", help_command=None, self_bot=True, intents=discord.Intents().all())
print(Colorate.Vertical(Colors.red_to_yellow, f"""


                                      ██╗     ██╗███████╗████████╗
                                      ██║     ██║██╔════╝╚══██╔══╝
                                      ██║     ██║█████╗     ██║   
                                      ██║     ██║██╔══╝     ██║   
                                      ███████╗██║██║        ██║   
                                      ╚══════╝╚═╝╚═╝        ╚═╝   
                                                
                                        
     ┌────────────────────────────────────────────────────────────────────────────────────────┐
                      Current Version: 13.2.8 | You`re using the latest version
     └────────────────────────────────────────────────────────────────────────────────────────┘"""))



def login(token):
    bot.run(token=f"{token}", log_handler=None)
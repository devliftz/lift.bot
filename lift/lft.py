import discord
from discord.ext import commands

from lift.gradient import Colorate, Colors
import lift.status
from urllib.request import urlopen

file_url = 'https://raw.githubusercontent.com/devliftz/lift.bot/main/version.txt'
dataver = urlopen(file_url).read(203).decode('utf-8')

bot = commands.AutoShardedBot(command_prefix="?", help_command=None, intents=discord.Intents().all(), shard_count=5)
print(Colorate.Horizontal(Colors.red_to_yellow, f"""


                                      ██╗     ██╗███████╗████████╗
                                      ██║     ██║██╔════╝╚══██╔══╝
                                      ██║     ██║█████╗     ██║   
                                      ██║     ██║██╔══╝     ██║   
                                      ███████╗██║██║        ██║   
                                      ╚══════╝╚═╝╚═╝        ╚═╝   
                                                
                                        
     ┌────────────────────────────────────────────────────────────────────────────────────────┐
                      Current Version: {dataver} | You`re using the latest version
     └────────────────────────────────────────────────────────────────────────────────────────┘
     
     """))

@bot.event
async def on_command(ctx):
    print(Colorate.Horizontal(Colors.red_to_yellow, f"""
    ┌────────────────────────────────────────────────────┐
      Command: {ctx.command.name}
      Input: {ctx.message.content}
      Server: {ctx.author.guild.name} ID: {ctx.author.guild.id}
      User: {ctx.author.name}
    └────────────────────────────────────────────────────┘
    """))

@bot.event
async def on_shard_ready(shard_id):
    print(Colorate.Horizontal(Colors.red_to_yellow, f"""Shard {shard_id} is ready"""))

def login(token):
    bot.run(token=f"{token}", log_handler=None)
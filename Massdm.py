import discord
from discord.ext import commands
import colorama
import os
from colorama import Fore
client = commands.Bot(command_prefix = 'MD', help_command = None)

colorama.init()
token = 'TOKEN_HERE'
@client.event
async def on_ready():
 os.system('cls')
 print(f'''
{Fore.RED} 
██╗   ███╗ █████╗ ███████╗███████╗    ██████╗ ███╗   ███╗
████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔══██╗████╗ ████║
██╔████╔██║███████║███████╗███████╗    ██║  ██║██╔████╔██║
██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██║  ██║██║╚██╔╝██║
██║ ╚═╝ ██║██║  ██║███████║███████║    ██████╔╝██║ ╚═╝ ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═╝     ╚═╝
{Fore.BLUE}                              
{Fore.BLUE}                      [1] Mass Dm 
{Fore.YELLOW}                                                                    
''')
 fuck = input(f"{Fore.GREEN}Select>>")
 if fuck == '1':
  input2 = input(f"{Fore.GREEN}What Should I Send?>>")
  for user in client.user.friends:
   await user.send(f"{input2}")
   print(f"{Fore.GREEN}[+] Send {Fore.GREEN} {input2} To {user}")

client.run(token, bot = False)

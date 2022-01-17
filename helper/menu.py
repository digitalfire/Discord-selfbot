from colorama import init
init()
from colorama import Fore, Style, Back
import os
import asyncio
import json
import sys
from helper import spammer
from cfg.cfg import get_value, set_value
import helper
from helper import security
from aioconsole import ainput
from helper import nuker
from helper import farm

# CLEAR ALL
os.system('clear')


async def giveaway_sniper(client):
    os.system('clear')
    print((Fore.RED + Style.BRIGHT) + '< CONTROL PANEL >')
    print((Fore.BLUE + Style.BRIGHT) + "\nGIVEAWAY SNIPER SETTINGS")
    option = str(await ainput('\nEnter Enable/Disable To Change The Settings: '))
    if option.lower() == 'enable':
        val = 'True'
    elif option.lower() == 'disable':
        val = 'False'
    else:
        print((Fore.RED + Style.BRIGHT) + "Invalid Option Entered! Resetting In 5 Seconds...")
        await asyncio.sleep(5.0)
        await giveaway_sniper(client)
    await set_value('giveaway_sniper', val)
    print((Fore.GREEN + Style.BRIGHT) + "Successfully " +option.title()+ "d Option! Returning To Main Menu In 5 Seconds...")
    await asyncio.sleep(5.0)
    await show_menu(client) 

async def nitro_sniper(client):
    os.system('clear')
    print((Fore.RED + Style.BRIGHT) + '< CONTROL PANEL >')
    print((Fore.BLUE + Style.BRIGHT) + "\nNITRO SNIPER SETTINGS")
    option = str(await ainput('\nEnter Enable/Disable To Change The Settings: '))
    if option.lower() == 'enable':
        val = 'True'
    elif option.lower() == 'disable':
        val = 'False'
    else:
        print((Fore.RED + Style.BRIGHT) + "Invalid Option Entered! Resetting In 5 Seconds...")
        await asyncio.sleep(5.0)
        await nitro_sniper(client)
    await set_value('nitro_sniper', val)
    print((Fore.GREEN + Style.BRIGHT) + "Successfully " +option.title()+ "d Option! Returning To Main Menu In 5 Seconds...")
    await asyncio.sleep(5.0)
    await show_menu(client)    


async def global_usage(client):
    os.system('clear')
    print((Fore.RED + Style.BRIGHT) + '< CONTROL PANEL >')
    print((Fore.BLUE + Style.BRIGHT) + "\nGLOBAL USAGE SETTINGS")
    option = str(await ainput('\nEnter Enable/Disable To Change The Settings: '))
    if option.lower() == 'enable':
        val = 'True'
    elif option.lower() == 'disable':
        val = 'False'
    else:
        print((Fore.RED + Style.BRIGHT) + "Invalid Option Entered! Resetting In 5 Seconds...")
        await asyncio.sleep(5.0)
        await global_usage(client)
    await set_value('global_usage', val)
    print((Fore.GREEN + Style.BRIGHT) + "Successfully " +option.title()+ "d Option! Returning To Main Menu In 5 Seconds...")
    await asyncio.sleep(5.0)
    await show_menu(client) 

async def logging_manager(client):
    os.system('clear')
    print((Fore.RED + Style.BRIGHT) + '< CONTROL PANEL >')
    print((Fore.BLUE + Style.BRIGHT) + "\nERROR LOGS SETTINGS")
    option = str(await ainput('\nEnter Enable/Disable To Change Error Logs Settings: '))
    if option.lower() == 'enable':
        val = 'True'
    elif option.lower() == 'disable':
        val = 'False'
    else:
        print((Fore.RED + Style.BRIGHT) + "Invalid Option Entered! Resetting In 5 Seconds...")
        await asyncio.sleep(5.0)
        await logging_manager(client)
    await set_value('logging', val)
    print((Fore.GREEN + Style.BRIGHT) + "Successfully " +option.title()+ "d Option! Returning To Main Menu In 5 Seconds...")
    await asyncio.sleep(5.0)
    await show_menu(client) 

async def show_menu(client):
    show_logo()
    print((Fore.RED + Style.BRIGHT) + '< CONTROL PANEL >')
    print((Fore.CYAN + Style.BRIGHT) + "\n1. DM Channel")
    print("2. Direct DM")
    print((Fore.YELLOW + Style.BRIGHT))
    ch = int(await ainput("Input Option Number: "))
    if ch == 1:
        await spammer.dm_advertise(client)   
    elif ch == 2:
        await spammer.dm_spammer(client)

def show_logo():
    os.system('clear')
    print((Fore.RED + Style.BRIGHT)) # Add bg color
    print(
"""
█▀▄ █ █▀▀ █ ▀█▀ ▄▀█ █░░ █▀▀ █ █▀█ █▀▀
█▄▀ █ █▄█ █ ░█░ █▀█ █▄▄ █▀░ █ █▀▄ ██▄
"""
    )
    print(Style.RESET_ALL)


def show_console_logo():
    os.system('clear')
    print((Fore.CYAN + Back.BLACK + Style.BRIGHT)) # Add bg color
    print(
"""
░█▀▄▀█ █▀▀█ █▀▀▄ █▀▀ █──█ ░█▀▀█ █▀▀█ ─▀─ █▀▀▄ ▀▀█▀▀ █▀▀ █▀▀█ 
░█░█░█ █──█ █──█ █▀▀ █▄▄█ ░█▄▄█ █▄▄▀ ▀█▀ █──█ ──█── █▀▀ █▄▄▀ 
░█──░█ ▀▀▀▀ ▀──▀ ▀▀▀ ▄▄▄█ ░█─── ▀─▀▀ ▀▀▀ ▀──▀ ──▀── ▀▀▀ ▀─▀▀
"""
    )
    print(Style.RESET_ALL)
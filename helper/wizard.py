from cli import run
import os
import asyncio
from colorama import init

from helper.menu import show_logo
init()
from colorama import Fore, Style
import json
from cfg.cfg import set_value
from aioconsole import ainput


async def setup_bot():
    try:
        os.system('clear')
        show_logo()
        print((Fore.RED + Style.BRIGHT) + '-----[ WELCOME TO SETUP WIZARD ]')
        print((Fore.CYAN + Style.BRIGHT) + '\nThis Setup Wizard Will Easily Configure Your Bot Settings.')
        token = str(await ainput('Enter Your Account Token: '))
        await set_value('token', token)
        usage = str(await ainput('Do You Want To Enable Global Command Usage (Yes/No): ')).lower()
        if usage == 'yes':
            global_usage = "True"
        else:
            global_usage = "False"
        await set_value('global_usage', global_usage)
        logs = str(await ainput('Do You Want To Enable Error Logging (Yes/No): ')).lower()
        if logs == 'yes':
            log_error = "True"
        else:
            log_error = "False"
        await set_value('logging', log_error)
        prefix = str(await ainput('What Should Be The Prefix For Your Selfbot: '))
        await set_value('prefix', prefix)
        owner = int(await ainput('Enter Owner ID Of The Bot: '))
        await set_value('owner', owner)
        print((Fore.GREEN + Style.BRIGHT) + "\nSETUP COMPLETED RESTART THE PROGRAM TO RUN YOUR BOT!")
        await ainput('PRESS ENTER TO CLOSE...')
    except Exception as e:
        print((Fore.RED + Style.BRIGHT) + "[ERROR] "+str(e))
        await ainput("PRESS ENTER TO RESTART TO SETUP WIZARD...")
        await setup_bot()
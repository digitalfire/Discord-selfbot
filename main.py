from colorama import init
from helper.menu import show_logo
init()
import selfcord as discord
from cli.auth import client
from cli import run
from cfg.cfg import get_value
from colorama import Fore, Style
import sys
import platform
import asyncio
from helper import security
import helper
import json


@client.event
async def on_ready():
    print((Fore.GREEN + Style.BRIGHT) + get_value('botname') + ' bot successfully connected to the server.')
    await helper.console(client)

@client.command(name='shutdown', help='Shutdown the bot remotely', usage='shutdown')
async def _shutdown(ctx):
    owner = get_value('owner')
    if ctx.author.id == int(owner):
        msg = await ctx.send("Shutting down...")
        await helper.shutdown(client)


if __name__ == '__main__':
    extensions = get_value('modules')
    default_extensions = ["handler.errorHandler"]
    show_logo()
    print((Fore.RED + Style.BRIGHT) + "---------------[ LOADING COMMANDS ]")
    try:
        for extension in extensions:
            client.load_extension(extension)
            print(Fore.CYAN + 'Command Loaded: {}'.format(extension))
        print('\n')
    except Exception as error:
        print((Fore.RED + Style.BRIGHT) + 'Command {} cannot be loaded. [{}]'.format(extension, error))
        pass
    print((Fore.RED + Style.BRIGHT) + "---------------[ LOADING MODULES ]")
    try:
        for default_extension in default_extensions:
            client.load_extension(default_extension)
            print(Fore.CYAN + 'Module Loaded: {}'.format(default_extension))
        print('\n')
    except Exception as error:
        print((Fore.RED + Style.BRIGHT) + 'Module {} cannot be loaded. [{}]'.format(default_extension, error))
        pass
    print((Fore.RED + Style.BRIGHT) + "---------------[ CHECKING VERSION DEPENDENCIES ]")
    print(Fore.CYAN + 'Bot Version: ' + get_value('version'))
    print(Fore.CYAN + 'Discord Version: ' + discord.__version__)
    print(Fore.CYAN + 'Python Version: ' + sys.version)
    print(Fore.CYAN + 'OS Information: ' + str(platform.platform()))
    print('\n')
    print((Fore.RED + Style.BRIGHT) + "---------------[ INITIALIZING AUTOMATION SEQUENCE ]")
    print((Fore.YELLOW + Style.BRIGHT) + 'Please wait...')
    run.start()
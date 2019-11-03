from Util.LoggingHelper import log_info_message
import threading
from Cli.Commands import ping
import asyncio

COMMANDS = {'help': -1, 'ping': 1}
TRANSMIT_COMMANDS = {1: ping.ping}

class CommandLine:
    def __init__(self, rf_controller):
        self.rf_controller = rf_controller

    async def run_cli(self):
        while True:
            await self.run_command(input('Enter Command: '))
            await asyncio.sleep(0.01)

    async def run_command(self, command):
        if command == 'help':
            print('-Commands-')
            print(COMMANDS.keys())
            return
        try:
            await TRANSMIT_COMMANDS[COMMANDS[command]](self.rf_controller)
        except Exception as e:
            print('Invalid Command')
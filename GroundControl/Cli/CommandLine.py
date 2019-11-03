from Util.LoggingHelper import log_info_message
import threading
from Cli.Commands import ping, start_reaction_wheels, stop_reaction_wheels, get_reaction_wheel_status
import asyncio

COMMANDS = {'help': -1, 'ping': 1, 'startReactionWheels': 5, 'stopReactionWheels': 6, 'getReactionWheelStatus': 7}
TRANSMIT_COMMANDS = {1: ping.ping, 5: start_reaction_wheels.start_reaction_wheels, 6: stop_reaction_wheels.stop_reaction_wheels, 7: get_reaction_wheel_status.get_reaction_wheel_status}

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
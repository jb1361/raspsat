import RfCommunications.RfController as rfController
import asyncio
import sys
import os


async def execute_command(rf_controller):
    while True:
        receive = await rf_controller.get_response()
        print(receive)
        if receive == 1:
            print('Responding to Ping Command')
            rf_controller.rfTransmitter.tx_repeat = 50
            await rf_controller.send(123)
            return

async def main():
    global rf_controller
    try:
        print('Starting RaspSat')

        print('Starting Rf Controller')
        rf_controller = rfController.RfController()

        while True:
            print('Waiting for command...')
            await execute_command(rf_controller)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        rf_controller.exit()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

asyncio.run(main())

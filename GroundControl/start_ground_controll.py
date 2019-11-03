from Util.LoggingHelper import log_info_message
import RfCommunications.RfController as rfController
import Cli.CommandLine as Cli
import threading
import asyncio
import sys
import os

async def main():
    global rf_controller
    try:
        log_info_message('Starting Ground Control')

        log_info_message('Starting Rf Controller')
        rf_controller = rfController.RfController()

        log_info_message('Starting Cli')
        cli = Cli.CommandLine(rf_controller)
        cli_task = asyncio.create_task(cli.run_cli())

        await cli_task
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        rf_controller.exit()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

asyncio.run(main())
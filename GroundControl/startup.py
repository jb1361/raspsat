from Util.LoggingHelper import log_info_message
import RfCommunications.RfController as rfController
import Cli.CommandLine as Cli
import threading
import asyncio

async def main():
    log_info_message('Starting Ground Control')

    log_info_message('Starting Rf Controller')
    rf_controller = rfController.RfController()
    rf_controller_task = asyncio.create_task(rf_controller.receive())

    log_info_message('Starting Cli')
    cli = Cli.CommandLine(rf_controller)
    cli_task = asyncio.create_task(cli.run_cli())

    await rf_controller_task
    await cli_task

asyncio.run(main())
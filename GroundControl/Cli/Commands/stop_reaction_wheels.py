from Util.LoggingHelper import log_info_message
from datetime import datetime

async def stop_reaction_wheels(rf_controller):
    try:
        log_info_message('Sending Start Reaction Wheel Command')
        await rf_controller.send(6)
        rf_controller.disable_receiver()
    except Exception as e:
        print('Error: ' + str(e))
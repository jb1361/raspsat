from Util.LoggingHelper import log_info_message
from datetime import datetime

async def start_reaction_wheels(rf_controller):
    try:
        log_info_message('Sending Start Reaction Wheel Command')
        await rf_controller.send(5)
    except Exception as e:
        print('Error: ' + str(e))
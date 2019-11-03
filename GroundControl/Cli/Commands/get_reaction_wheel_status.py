from Util.LoggingHelper import log_info_message
from datetime import datetime

async def get_reaction_wheel_status(rf_controller):
    try:
        log_info_message('Sending Get Reaction Wheel Command')
        await rf_controller.send(7)
        while True:
            print('Waiting for response...')
            receive = await rf_controller.get_response(10)
            if receive == 71:
                print('Reaction Wheels are Running')
                break
            elif receive == 70:
                print('Reaction Wheels are not running')
                break
            else:
                print('Timed out - Retrying')
                await rf_controller.send(5200)
    except Exception as e:
        print('Error: ' + str(e))
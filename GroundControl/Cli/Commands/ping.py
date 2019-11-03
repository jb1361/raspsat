from Util.LoggingHelper import log_info_message
from datetime import datetime

async def ping(rf_controller):
    try:
        log_info_message('Sending Ping Command')
        timestamp = datetime.now()
        await rf_controller.send(1)
        while True:
            print('Waiting for response...')
            receive = await rf_controller.get_response(10, 1200)
            if receive == 1200:
                break
            else:
                print('Timed out - Retrying')
                await rf_controller.send(1)
        diff = (datetime.now() - timestamp).seconds
        print('Got response in {} seconds.'.format(str(diff)))
    except Exception as e:
        print('Error: ' + e)
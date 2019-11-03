from Util.LoggingHelper import log_info_message

async def ping(rf_controller):
    log_info_message('Sending Ping Command')
    await rf_controller.send(1)
    receive = await rf_controller.get_response(1)
    print('Response: ' + str(receive))
from Util.LoggingHelper import log_info_message
import RfCommunications.RfController as rfController
import threading

log_info_message('Starting Ground Control')

threadLock = threading.Lock()
threads = []
RfControllerThread = rfController.RfController(1, 'RfControllerThread')
RfControllerThread.start()



RfControllerThread.send(123)
RfControllerThread.receive()
threads.append(RfControllerThread)
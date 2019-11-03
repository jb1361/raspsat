from Util.LoggingHelper import log_info_message
import threading
from rpi_rf import RFDevice
import signal
import sys
import time
import logging


class RfController (threading.Thread):

    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self.rfReceiver = RFDevice(27)
        self.rfTransmitter = RFDevice(17)
        self.rfTransmitter.tx_repeat = 10
        self.timestamp = None
        log_info_message('Starting ' + self.name)


    def exithandler(self, signal, frame):
        self.rfReceiver.cleanup()
        self.rfTransmitter.cleanup()
        sys.exit(0)

    def receive(self):
        log_info_message('Enabling Receiver')
        self.rfTransmitter.disable_tx()
        self.rfReceiver.enable_rx()
        while True:
            if self.rfReceiver.rx_code_timestamp != self.timestamp:
                self.timestamp = self.rfReceiver.rx_code_timestamp
                logging.info(str(self.rfReceiver.rx_code) +
                             " [pulselength " + str(self.rfReceiver.rx_pulselength) +
                             ", protocol " + str(self.rfReceiver.rx_proto) + "]")
            time.sleep(0.01)

    def send(self, data):
        log_info_message('Sending ' + str(data))
        self.rfReceiver.disable_rx()
        self.rfTransmitter.enable_tx()
        self.rfTransmitter.tx_code(data, 1)
        self.rfTransmitter.disable_tx()
        log_info_message('Sent Data')
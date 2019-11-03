from Util.LoggingHelper import log_info_message
import threading
from rpi_rf import RFDevice
import signal
import sys
import time
import logging
import asyncio

class RfController:

    def __init__(self):
        self.rfReceiver = RFDevice(27)
        self.rfReceiver.enable_rx()
        self.rfTransmitter = RFDevice(17)
        self.rfTransmitter.enable_tx()
        self.rfTransmitter.tx_repeat = 10
        self.timestamp = None
        self.rx = None

    def exithandler(self, signal, frame):
        self.rfReceiver.cleanup()
        self.rfTransmitter.cleanup()
        sys.exit(0)

    async def receive(self):
        while True:
            if self.rfReceiver.rx_code_timestamp != self.timestamp:
                if self.valid_rx(self.rfReceiver.rx_pulselength, self.rfReceiver.rx_proto):
                    self.timestamp = self.rfReceiver.rx_code_timestamp
                    logging.info(str(self.rfReceiver.rx_code) +
                                 " [pulselength " + str(self.rfReceiver.rx_pulselength) +
                                 ", protocol " + str(self.rfReceiver.rx_proto) + "]")
            await asyncio.sleep(0.01)

    def valid_rx(self, pulse_length, protocol):
        if 349 <= pulse_length <= 354 and protocol == 1:
            return True
        else:
            return False

    async def get_response(self, expected_response):
        if self.rfReceiver.rx_code == expected_response:
            return self.rfReceiver.rx_code

    async def send(self, data):
        log_info_message('Sending ' + str(data))
        self.rfTransmitter.tx_code(data, 1)
        log_info_message('Sent Data')
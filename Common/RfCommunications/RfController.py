from Util.LoggingHelper import log_info_message
import threading
from rpi_rf import RFDevice
import signal
import sys
import time
import logging
import asyncio
from datetime import datetime

class RfController:

    def __init__(self):
        self.rfReceiver = RFDevice(27)
        self.rfReceiver.enable_rx()
        self.rfTransmitter = RFDevice(17)
        self.rfTransmitter.tx_repeat = 10
        self.timestamp = None

    def exithandler(self, signal, frame):
        self.rfReceiver.cleanup()
        self.rfTransmitter.cleanup()
        sys.exit(0)

    async def receive(self, timeout = None):
        start = datetime.now()
        while True:
            if self.rfReceiver.rx_code_timestamp != self.timestamp:
                if self.valid_rx(self.rfReceiver.rx_pulselength, self.rfReceiver.rx_proto):
                    self.timestamp = self.rfReceiver.rx_code_timestamp
                    break
            if timeout:
                diff = (datetime.now() - start).seconds
                if diff > timeout:
                    break

            await asyncio.sleep(0.01)
        return self.rfReceiver.rx_code

    def valid_rx(self, pulse_length, protocol):
        if 349 <= pulse_length <= 354 and protocol == 1:
            return True
        else:
            return False

    async def get_response(self, timeout = None):
        return await self.receive(timeout)

    async def send(self, data):
        log_info_message('Sending ' + str(data))
        self.rfReceiver.disable_rx()
        await asyncio.sleep(0.01)
        self.rfTransmitter.enable_tx()
        await asyncio.sleep(0.01)
        self.rfTransmitter.tx_code(data, 1)
        await asyncio.sleep(0.01)
        self.rfTransmitter.disable_tx()
        await asyncio.sleep(0.01)
        self.rfReceiver.enable_rx()
        log_info_message('Sent Data')
        await asyncio.sleep(1)

    def exit(self):
        self.rfTransmitter.cleanup()
        self.rfReceiver.cleanup()
        return

    def disable_receiver(self):
        self.rfReceiver.disable_rx()
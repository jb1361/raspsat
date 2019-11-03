import RfCommunications.RfController as rfController
import asyncio
import sys
import os
from RPi import GPIO


class RaspSat:
    def __init__(self):
        self.reaction_wheels_enabled = False
        self.reaction_wheels_pin = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.reaction_wheels_pin, GPIO.OUT)
        self.rf_controller = None

    def start_reaction_wheels(self):
        GPIO.output(self.reaction_wheels_pin, 1)
        self.reaction_wheels_enabled = True

    def stop_reaction_wheels(self):
        GPIO.output(self.reaction_wheels_pin, 0)
        self.reaction_wheels_enabled = False

    def get_reaction_wheels_status(self):
        return self.reaction_wheels_enabled

    async def execute_command(self, rf_controller):
        while True:
            receive = await rf_controller.get_response()
            print('Received: ' + str(receive))
            if receive == 1:
                print('Responding to Ping Command')
                await rf_controller.send(1200)
                return
            if receive == 5:
                self.start_reaction_wheels()
                print('Responding to Start Reaction Wheel Command')
                # await rf_controller.send(5200)
                return
            if receive == 6:
                self.stop_reaction_wheels()
                print('Responding to Stop Reaction Wheel Command')
                # await rf_controller.send(6200)
                return

            if receive == 7:
                self.get_reaction_wheels_status()
                print('Responding to Get Reaction Wheel Status')
                if self.get_reaction_wheels_status():
                    await rf_controller.send(71)
                else:
                    await rf_controller.send(70)
                return

    async def main(self):
        try:
            print('Starting RaspSat')

            print('Starting Rf Controller')
            self.rf_controller = rfController.RfController()
            self.rf_controller.rfTransmitter.tx_repeat = 50
            while True:
                print('Waiting for command...')
                await self.execute_command(self.rf_controller)
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            self.rf_controller.exit()
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)

# def trace(frame, event, arg):
#     print("%s, %s:%d" % (event, frame.f_code.co_filename, frame.f_lineno))
#     return trace
#
# sys.settrace(trace)
asyncio.run(RaspSat().main())

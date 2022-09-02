'''
'''

import time
from math import ceil

from commands import commands
from coordinate import Coordinate, coordinates
from upper_gantry_velocity import UpperGantryVelocity

from utils import check_type, check_if_dir_valid, replace_address, replace_word

class Motor():
    # Public variables.
    controller = None

    # Private variables.
    __request_ID = None
    __address = None        # uint
    __steps = None
    __limit = None
    __IO = None
    __velocity = None
    __commands = commands['motor']

    # Private constants (homing velocity)
    __HVEL = {
        0x01 : 20000, # ustep / sec
        0x02 : 150000,
        0x03 : 80000,
        0x04 : 150000
        }

    # Private constants (Move Time Scaling Factors).
    __MOVE_TIME_SCALE_FACTOR = {
        0x01 : 2.13,
        0x02 : 67.20,
        0x03 : 2.03,
        0x04 : 6.25
        }

    def __init__(self, controller):
        self.controller = controller

    def home(self, address, block=True):
        # Check the address type.
        check_type(address, int)
        # Get the home command.
        command = self.__commands['home']
        # Replace 'address' with the desired address. 
        command = replace_address(command, address)
        # Get the current location from home (0).
        steps = self.get_position_from_response(address)
        # Send the command.
        self.controller.write(command)
        if block:
            # Compute the timeout for the move.
            timeout = self.compute_move_timeout(address, steps, self.__HVEL[address])
            # Check the position was reached.
            self.check_position_response(address, 0, timeout)

    def mrel(self, address, steps, velocity):
        # Check the input types.
        check_type(address, int)
        check_type(steps, int)
        check_type(velocity, int)
        # Get the mrel command.
        command = self.__commands['mrel']
        # Replace 'address' with the desired address.
        command = replace_address(command, address)
        # Replace 'steps' with the desired steps.
        command = replace_word(command, 'steps', steps)
        # Replace 'velocity' with the desired velocity.
        command = replace_word(command, 'velocity', velocity)
        # Send the command.
        self.controller.write(command)

    def mabs(self, address, steps, velocity, block=True):
        # Check the input types.
        check_type(address, int)
        check_type(steps, int)
        check_type(velocity, int)
        check_type(block, bool)
        # Get the mabs command.
        command = self.__commands['mabs']
        # Replace 'address' with the desired address.
        command = replace_address(command, address)
        # Replace 'steps' with the desired steps.
        command = replace_word(command, 'steps', steps)
        # Replace 'velocity' with the desired velocity.
        command = replace_word(command, 'velocity', velocity)
        # Send the command.
        self.controller.write(command)
        time.sleep(0.2)
        if block:
            # Compute the timeout for the move.
            timeout =  self.compute_move_timeout(address, steps, velocity)
            # Check the position was reached.
            self.check_position_response(address, steps, timeout)

    def mlim(self, address, limit, velocity):
        # Check the input types.
        check_type(address, int)
        check_type(limit, int)
        check_type(velocity, int)
        # Get the mlim command.
        command = self.__commands['mlim']
        # Replace 'address' with the desired address.
        command = replace_address(command, address)
        # Replace 'steps' with the desired steps.
        command = replace_word(command, 'limit', limit)
        # Replace 'velocity' with the desired velocity.
        command = replace_word(command, 'velocity', velocity)
        # Send the command.
        self.controller.write(command)

    def mgp(self, address, IO, velocity):
        # Check the input types.
        check_type(address, int)
        check_type(IO, int)
        check_type(velocity, int)
        # Get the mgp command.
        command = self.__commands['mgp']
        # Replace 'address' with the desired address.
        command = replace_address(command, address)
        # Replace 'steps' with the desired steps.
        command = replace_word(command, 'IO', IO)
        # Replace 'velocity' with the desired velocity.
        command = replace_word(command, 'velocity', velocity)
        # Send the command.
        self.controller.write(command)

    def qpos(self, address):
        # Check the input types.
        check_type(address, int)
        # Get the ?pos command.
        command = self.__commands['?pos']
        # Replace 'address' with the desired address.
        command = replace_address(command, address)
        # Send the command.
        self.controller.write(command)

    def qmv(self, address):
        # Check the input types.
        check_type(address, int)
        # Get the ?mv command.
        command = self.__commands['?mv']
        # Replace 'address' with the desired address.
        command = replace_address(command, address)
        # Send the command.
        self.controller.write(command)

    def hdir(self, address, direction):
        # Check the direction if valid.
        check_type(address, int)
        check_type(direction, int)
        check_if_dir_valid(direction)
        # Get the command.
        command = replace_address(self.__commands['hdir'], address)
        command = replace_word(command, 'direction', direction)
        # Send the command.
        self.controller.write(command)
    
    def hvel(self, address, velocity):
        # Check validity.
        check_type(address, int)
        check_type(velocity, int)
        # Get the command.
        command = replace_address(self.__commands['hvel'], address)
        command = replace_word(command, 'velocity', velocity)
        # Send the command.
        self.controller.write(command)

    def hpol(self, address, polarity):
        # Check validity.
        check_type(address, int)
        check_type(polarity, int)
        # Get the command.
        command = replace_word(self.__commands['hpol'], 'polarity', polarity)
        # Send the command.
        self.controller.write(command)

    def tout(Self, address, milliseconds):
        return None

    def gppol(self, address, polarity):
        return None

    def stop(self, address):
        # Check validity.
        check_type(address, int)
        # Get the command.
        command = replace_address(self.__commands['stop'], address)
        # Send the command.
        self.controller.write(command)

    def compute_move_timeout(self, address, steps, velocity):
        # Check the types.
        check_type(address, int)
        check_type(steps, int)
        check_type(velocity, int)
        # Get the scale factor.
        time_scale_factor = self.__MOVE_TIME_SCALE_FACTOR[address]
        # Return the timeout
        return ceil(time_scale_factor * abs(steps) / velocity)

    def check_position_response(self, address, steps, timeout):
        # Check types
        check_type(address, int)
        check_type(steps, int)
        check_type(timeout, int)
        # Wait the specified time for the ?pos response
        time_start = time.time()
        while time.time() - time_start < timeout:
            self.qpos(address)
            # Get the ?pos response after waiting
            position_response = self.controller.readline().decode()
            if position_response != '':
                position = self.get_position_from_response(address)
                if position == steps:
                    return
            time.sleep(0.5)
        # Send the ?pos command
        self.qpos(address)
        # Get the position
        position = self.get_position_from_response(address)
        # Check if the desired position was reached after the timeout period
        if position != steps:
            print(f"Position ({position}) != desired ({steps}) in {timeout} seconds!")

    def get_position_from_response(self, address):
        # Check types
        check_type(address, int)
        # Send out the ?pos 
        self.qpos(address)
        # Get the ?pos response
        position_response = self.controller.readline().decode()
        # Return the position
        while position_response == '':
            self.qpos(address)
            position_response = self.controller.readline().decode()
            if position_response != '':
                return int(position_response.split(',')[-1])
        return int(position_response.split(',')[-1])



    def wait(self):
        return None
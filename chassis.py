'''
DESCRIPTION:
This module contains the Chassis object for controlling relay valves.

AUTHOR:
G.LC

AFFILIATION:
Bio-Rad, CDG, Advanced-Tech Team

# CREATED ON:
9/1/2022
'''

from commands import commands

from utils import replace_address, replace_word

class Chassis():
    # Public variables.
    controller = None

    # Private variables.
    __id = None
    __relay_state = None # [0;OFF,1-ON] Following IEC 60417-5008 and IEC 60417-5007, respectively 
    __commands = commands['chassis']
    __address = None

    # Constructor.
    def __init__(self, controller, id=None, address=None):
        self.controller = controller
        self.__id = id
        self.__address = address

        # Set the default settings.
        self.__relay_state = 0 # OFF (IEC 60417-5008)

    # Getter Methods
    def get_id(self):
        return self.__id
    def get_relay_state(self):
        return self.__relay_state

    # Relayon Method
    def relayon(self, channel):
        # Get the relayon command.
        command = self.__commands['relayon']
        # Repalce the address.
        command = replace_address(command, self.__address)
        # Replace the channel.
        command = replace_word(command, 'channel', channel)
        # Send the command.
        self.controller.write(command)
        self.__relay_state = 1 # ON (IEC 60417-5007)

    # Relayoff Method
    def relayoff(self, channel):
        # Get the relayoff command.
        command = self.__commands['relayoff']
        # Replace the address.
        command = replace_address(command, self.__address)
        # Replace the channel.
        command = replace_word(command, 'channel', channel)
        # Send the command.
        self.__relay_state = 0 # OFF (IEC 60417-5008)
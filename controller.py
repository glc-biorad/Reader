'''
DESCRIPTION:
'''

import clr

clr.AddReference('System.IO')

from System.IO import Ports

class Controller():
    # Public variables.

    # Private variables.

    # Private constants
    __SERIAL_PORT = None
    __COM_PORT = 'COM8'
    __BAUD_RATE = 115200
    __TIMEOUT_READLINE = 1000
    __TIMEOUT_WRITELINE = 1000
    __PARITY = None
    __HANDSHAKE = None
    __DATABITS = 8
    __STOPBITS = 'One'
    __NEWLINE = '\r'

    # Constructor.
    def __init__(self):
        self.__SERIAL_PORT = Ports.SerialPort(PortName=self.__COM_PORT, BaudRate=self.__BAUD_RATE)
        self.__SERIAL_PORT.ReadTimeout = self.__TIMEOUT_READLINE
        self.__SERIAL_PORT.WriteTimeout = self.__TIMEOUT_WRITELINE
        self.__SERIAL_PORT.NewLine = self.__NEWLINE
        self.__SERIAL_PORT.Open()

    def write(self, command):
        self.__SERIAL_PORT.WriteLine(command.decode())

    def readline(self):
        response = self.__SERIAL_PORT.ReadLine()
        return response

    def close(self):
        self.__SERIAL_PORT.Close()

    def test(self):
        print("HERE")

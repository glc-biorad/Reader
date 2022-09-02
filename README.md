# Reader

# Required Modules:
- commands.py
- utils.py
- reader_coordinate.py
- reader_velocity.py
- motor.py
- led.py

# Reader Class
- Public Variables:
  - controller (Controller(serial.Serial)): serial.Serial inherited class for reading/writing data on a COM port.
  - led (led.LED()): LED object for controlling the Reader LEDs.
- Private Variables:
  - __commands (dict): dictionary of explicit Reader commands.
  - __coordinate (reader_coordinate.ReaderCoordinate): Reader coordinate (.x, .y, .z, .filter_wheel) for keeping track of the Reader.
  - __velocity (reader_velocity.ReaderVelocity): Reader velocity (.x, .y, .z, .filter_wheel) for keeping track of the Reader velocity.
- Private Constants:
  - __ADDRESS_X_AXIS (uint): 0x06
  - __ADDRESS_Y_AXIS (uint): 0x07
  - __ADDRESS_Z_AXIS (uint): 0x08
  - __ADDRESS_FILTER_WHEEL_AXIS (uint): 0x09
  - __ADDRESS_LED (uint): 0xA
  - __ADDRESS_FRONT_TRAY (uint): 0xB
  - __ADDRESS_READ_TRAY (uint): 0xC
- Constructor:
- Public Methods:
- Private Methods:

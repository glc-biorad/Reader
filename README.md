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
  - controller (controller.Controller(serial.Serial)): serial.Serial inherited class for reading/writing data on a COM port.
  - led (led.LED): LED object for controlling the Reader LEDs.
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
  - __ADDRESS_HEATER_FRONT_1 (uint): 0xD
  - __ADDRESS_HEATER_FRONT_2 (uint): 0xE
  - __ADDRESS_HEATER_REAR_1 (uint): 0xF
  - __ADDRESS_HEATER_REAR_2 (uint): 0x10
  - __LIMIT_MAX_STEPS_FROM_HOME_X (int): maximum steps along the Reader X-axis.
  - __LIMIT_MAX_STEPS_FROM_HOME_Y (int): maximum steps along the Reader Y-axis.
  - __LIMIT_MAX_STEPS_FROM_HOME_Z (int): maximum steps along the Reader Z-axis.
  - __LIMIT_MAX_STEPS_FROM_HOME_FILTER_WHEEL (int): maximum steps along the Reader Filter Wheel.
  - __LIMIT_MAX_VELOCITY_X (int): maximum velocity of the Reader X-axis motion.
  - __LIMIT_MAX_VELOCITY_Y (int): maximum velocity of the Reader Y-axis motion.
  - __LIMIT_MAX_VELOCITY_Z (int): maximum velocity of the Reader Z-axis motion.
  - __LIMIT_MAX_VELOCITY_FILTER_WHEEL (int): maximum velocity of the Reader Filter Wheel motion.
  - __HVEL_X (int): homing velocity of the Reader X-axis.
  - __HVEL_Y (int): homing velocity of the Reader Y-axis.
  - __HVEL_Z (int): homing velocity of the Reader Z-axis.
  - __HVEL_FILTER_WHEEL (int): homing velocity of the Reader Filter Wheel.
- Constructor:
  - Input:
    - controller (controller.Controller(serial.Serial): serial.Serial inherited class for reading/writing data on a COM port.
    - led (led.LED): LED object for controlling the Reader LEDs.
- Public Methods:
  - home_reader:
    - Description: Homes the Reader
- Private Methods:

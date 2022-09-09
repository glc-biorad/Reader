
'''
'''

from commands import commands

from utils import check_type

from reader_coordinate import ReaderCoordinate, target_to_reader_coordinate
from reader_velocity import ReaderVelocity

import motor

from led import LED
# this import requires numpy, check for compatability (iron python)
try:
    import camera
    ignore_camera = 0
except (ModuleNotFoundError, ImportError) as e:
    ignore_camera = 1
    print('Unable to import modules. Continuing without camera')

class Reader(motor.Motor):
    # Public variables.
    controller = None
    led = None

    # Private variables.
    __commands = commands['Reader']
    __coordinate = ReaderCoordinate()
    __velocity = ReaderVelocity()

    # Private constants (Addresses).
    __ADDRESS_X_AXIS = 0x06
    __ADDRESS_Y_AXIS = 0x07
    __ADDRESS_Z_AXIS = 0x08
    __ADDRESS_FILTER_WHEEL = 0x09
    __ADDRESS_LED = 0xA
    __ADDRESS_FRONT_TRAY = 0xB
    __ADDRESS_REAR_TRAY = 0xC
    __ADDRESS_HEATER_FRONT_1 = 0xD
    __ADDRESS_HEATER_FRONT_2 = 0xE
    __ADDRESS_HEATER_REAR_1 = 0xF
    __ADDRESS_HEATER_REAR_2 = 0x10

    # Private constants (Limits).
    __LIMIT_MAX_STEPS_FROM_HOME_X, __LIMIT_MAX_STEPS_FROM_HOME_Y, __LIMIT_MAX_STEPS_FROM_HOME_Z, __LIMIT_MAX_STEPS_FROM_HOME_FILTER_WHEEL = __coordinate.get_limit_max() # usteps
    __LIMIT_MAX_VELOCITY_X, __LIMIT_MAX_VELOCITY_Y, __LIMIT_MAX_VELOCITY_Z, __LIMIT_MAX_VELOCITY_FILTER_WHEEL = __velocity.get_limit_max() # usteps/sec

    # Private constants (Homing velocity -- hvel).
    __HVEL_X = 1  # usteps
    __HVEL_Y = 1
    __HVEL_Z = 1
    __HVEL_FILTER_WHEEL = 1

    # Constructor.
    def __init__(self, controller):
        super().__init__(self)
        self.controller = controller
        self.led = LED(controller, self.__ADDRESS_LED)
        self.illumination_off() # turn off leds incase of previous error
        if ignore_camera == 0:
            self.imager = camera.ImagerController()

    # Home Reader Method.
    def home_reader(self):
        # Home along Z, Y, and X.
        self.home(self.__ADDRESS_Z_AXIS, block=False)
        self.home(self.__ADDRESS_Y_AXIS, block=False)
        self.home(self.__ADDRESS_X_AXIS, block=False)
        # Home heater 1, 2, 3, 4.
        self.home(self.__ADDRESS_HEATER_FRONT_1, block=False)
        self.home(self.__ADDRESS_HEATER_FRONT_2, block=False)
        self.home(self.__ADDRESS_HEATER_REAR_1, block=False)
        self.home(self.__ADDRESS_HEATER_REAR_2, block=False)
        # Home reader tray 1 and 2.
        self.home(self.__ADDRESS_FRONT_TRAY, block=False)
        self.home(self.__ADDRESS_REAR_TRAY, block=True)

    # Move Reader Method.
    def move_reader(self, target):
        # Convert the target to a ReaderCoordinate object.
        target_rc = target_to_reader_coordinate(target)
        # Move along Y and X to the target location.
        self.mabs(self.__ADDRESS_Y_AXIS, target_rc.y, self.__LIMIT_MAX_VELOCITY_Y, block=False)
        self.mabs(self.__ADDRESS_X_AXIS, target_rc.x, self.__LIMIT_MAX_VELOCITY_X, block=True)

    # Illumination On Method.
    def illumination_on(self, color):
        # Check type.
        check_type(color, int)
        # Rotate the filter wheel to the desired color.
        self.rotate_filter_wheel(color)
        # Set the given LED color to its on intensity level.
        self.led.set(self.__ADDRESS_LED, color, self.led.get_limit_max_level())

    # Illumination Off Method.
    def illumination_off(self):
        # Turn all LEDs off.
        self.led.offmult(self.__ADDRESS_LED, [i for i in range(self.led.get_number_of_channels())])

    # Lower Heater Method.
    def lower_heater(self, number):
        return None

    # Raise Heater Method.
    def raise_heater(self, number):
        return None

    # Focus Reader Method.
    def focus_reader(self):
        return None

    # Capture Image Method.
    def capture_image(self):
        # this method requires numpy, will not work with IronPython
        image = self.imager.snap_single()
        return image

    # Set Cartridge Temp Method.
    def set_cartridge_temp(self, number, temp):
        return None

    # Set Exposure Time Method.
    def set_exposure(self, exposuretime_microseconds):
        self.imager.setExposureTimeMicroseconds(exp_time_microseconds=exposuretime_microseconds)

    # Get Exposure Time Method
    def get_exposure(self):
        return self.imager.getExposureTime()

    # Start Camera Streaming Method.
    def start_camera_streaming(self):
        return None

    # Stop Camera Streaming Method.
    def stop_camera_streaming(self):
        return None

    # Rotate Filter Wheel Method.
    def rotate_filter_wheel(self, color):
        return None

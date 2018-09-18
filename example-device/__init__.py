"""This module provides an example Cayenne plugin containing a sensor and an actuator"""

import random
import time
from threading import Thread
from myDevices.utils.logger import info

class ExampleSensor():
    """An example sensor that reads random or incremental values."""

    def __init__(self, max=100, min=0, random=True):
        """Initializes the example sensor.

        Arguments:
        max: Maximum value the sensor functions return
        min: Minimum value the sensor functions return
        random: True if sensor values should be random, False if they should be incremental
        """
        self.max = max
        self.min = min
        self.random = random
        self.current_value = self.min

    def get_value(self):
        """Get an example value."""
        if self.random:
            value = random.uniform(self.min, self.max) 
        else:
            value = self.current_value
            self.current_value += 1
            if self.current_value > self.max:
                self.current_value = self.min          
        return value

    def get_celsius(self):
        """Get an example Celsius value."""
        return (self.get_value(), 'temp', 'c')

    def get_humidity(self):
        """Get an example humidity value."""
        return (self.get_value(), 'rel_hum', 'p')

    def get_pressure(self):
        """Get an example pressure value."""
        return (self.get_value(), 'bp', 'pa')


class ExampleActuator():
    """An example actuator that prints values."""
    
    def __init__(self, value=0, digital=True):
        """Initializes the example sensor.

        Arguments:
        value: The initial value for the actuator
        digital: True if this is a digital actuator, False if it is analog
        """
        self.value = value
        self.digital = digital

    def read(self):
        """Get the example actuator value."""
        if self.digital:
            return (self.value, 'digital_actuator')
        else:
            return (self.value, 'analog_actuator')

    def write(self, value):
        """Logs the specified value."""
        self.value = value
        if self.digital:
            info('Example actuator digital value: {}'.format(self.value))
        else:
            info('Example actuator analog value: {}'.format(self.value))


class ExampleCallbackSensor():
    """An example sensor that sends data changes via a callback."""

    def __init__(self, interval=10):
        """Initializes the example sensor.

        Arguments:
        interval: Interval in seconds that the sensor value should be changed
        """
        self.interval = interval
        self.current_value = 0
        self.callback = None
        self.change_data_thread = Thread(target=self.change_data, daemon=True)
        self.change_data_thread.start()

    def change_data(self):
        """Change example data at intervals."""
        while True:
            self.current_value = 1 - self.current_value
            if self.callback:
                self.callback(self.read())
            time.sleep(self.interval)

    def read(self):
        """Get an example value."""
        return (self.current_value, 'digital_sensor')

    def register_callback(self, callback):
        """Register a callback for data changes."""
        self.callback = callback

    def unregister_callback(self):
        """Register a callback for data changes."""
        self.callback = None
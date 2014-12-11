#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "192.168.1.60"
PORT = 4223
UID = "ngP" # Change to your UID

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_temperature import Temperature

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    t = Temperature(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current temperature (unit is °C/100)
    temperature = t.get_temperature()/100.0

    print('Temperature: ' + str(temperature) + ' °C')

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.disconnect()
#!/usr/bin/env python

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_motion_detector import MotionDetector
from datetime import datetime
import picamera

HOST = "192.168.1.60"
PORT = 4223
UID = "m63"


# Callback function for end of detection cycle
def cb_detection_cycle_ended():
    print('Detection Cycle Ended (next detection possible in ~3 seconds)')


# Callback function for detected motion
def cb_motion_detected():
    take_picture(3)


def take_picture(count):
    for x in range(0, count):
        with picamera.PiCamera() as camera:
            timestamp = datetime.now().strftime("%Y-%m-%d--%H-%M-%S.%f")
            filename = 'pictures/img.'+timestamp+'.jpg'
            camera.capture(filename)
            print("saved image: " + filename)


if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    md = MotionDetector(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register detected callback to function cb_motion_detected
    md.register_callback(md.CALLBACK_MOTION_DETECTED, cb_motion_detected)

    # Register detection cycle ended callback to function cb_detection_cycle_ended
    md.register_callback(md.CALLBACK_DETECTION_CYCLE_ENDED, cb_detection_cycle_ended)

    raw_input('Press key to exit\n') # Use input() in Python 3
    ipcon.disconnect()
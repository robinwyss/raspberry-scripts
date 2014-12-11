#!/usr/bin/env python

import web
import picamera
import datetime

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_temperature import Temperature

urls = (
    '/picture', 'Picture'
    '/temperature', 'Temp'
)
app = web.application(urls, globals())


class Picture:
    def POST(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S.%f")
        camera.capture('pictures/img.'+timestamp+'.jpg')


class Temp:
    HOST = "192.168.1.60"
    PORT = 4223
    UID = "ngP"

    def __init__(self):
        ipcon = IPConnection()
        ipcon.connect(self.HOST, self.PORT)
        self.t = Temperature(self.UID, ipcon)

    def GET(self):
        temperature = self.t.get_temperature()/100.0
        return str('Temperature: ' + str(temperature) + ' C')


if __name__ == "__main__":
    app.run()
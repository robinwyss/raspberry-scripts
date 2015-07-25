#!/usr/bin/env python

import web
import camera
import temperature


urls = (
    '/picture', 'Picture',
    '/temperature', 'Temp'
)
app = web.application(urls, globals())


class Picture:
    def POST(self):
        camera.capture()


class Temp:
    def GET(self):
        return str('Temperature: ' + str(temperature.read()) + ' C')


if __name__ == "__main__":
    app.run()
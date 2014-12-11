import picamera
import datetime

with picamera.PiCamera() as camera:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S.%f")
    camera.capture('pictures/img.'+timestamp+'.jpg')
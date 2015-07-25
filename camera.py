
import picamera
import datetime

filenamePattern = 'pictures/img.%s.jpg'
datePattern = '%Y-%m-%d--%H-%M-%S.%f'


def get_filename():
    timestamp = datetime.now().strftime(datePattern)
    return filenamePattern % timestamp


def capture():
    with picamera.PiCamera() as camera:
        filename = get_filename()
        camera.capture(filename)
        print("saved image: " + filename)
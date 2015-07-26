import picamera
from datetime import datetime
import config
from os.path import join, exists
from os import makedirs

cameraConfig = config.getCameraConfig()
folder = cameraConfig["folder"]
filenamePattern = cameraConfig["filenamepattern"]
datePattern = cameraConfig["datepattern"]

def get_filename():
    timestamp = datetime.now().strftime(datePattern)
    return filenamePattern % timestamp

def capture():
    with picamera.PiCamera() as camera:
        filename = get_filename()
        if not exists(folder):
            makedirs(folder)
        filePath = join(folder, filename)
        camera.capture(filePath)
        print("saved image: " + filePath)
        return filename
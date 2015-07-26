from PIL import Image
from os.path import basename, join, exists, dirname
from os import makedirs
import config

cameraConfig = config.getCameraConfig()

size = int(cameraConfig["imgwidth"]), int(cameraConfig["imgheight"])
folderSmall = cameraConfig["foldersmall"]

def resizeImg(path):
    imgName = basename(path)
    img = Image.open(path)
    img2 = img.resize(size, Image.ANTIALIAS)
    if not exists(folderSmall):
        makedirs(folderSmall)
    filePath = join(folderSmall, imgName)
    img2.save(filePath)
    return filePath
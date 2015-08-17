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
    img = img.resize(size, Image.ANTIALIAS)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    if not exists(folderSmall):
        makedirs(folderSmall)
    filePath = join(folderSmall, imgName)
    img.save(filePath)
    return filePath

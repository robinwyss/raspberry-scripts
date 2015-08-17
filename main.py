#!/usr/bin/env python

import camera
import resize
import ftpupload
import time

# wait 10s to not interfer with the timelaps script
time.sleep(10)
print("taking a picture")
imagePath = camera.capture()
print("captured %s" % imagePath)
smallImagePath = resize.resizeImg(imagePath)
print("resized image")
print("uploading....")
ftpupload.uploadFile(smallImagePath)
print("upload completed")

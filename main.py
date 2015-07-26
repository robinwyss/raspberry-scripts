#!/usr/bin/env python

import camera
import resize
import ftpupload

imagePath = camera.capture()
smallImagePath = resize.resizeImg(imagePath)
ftpupload.uploadFile(smallImagePath)
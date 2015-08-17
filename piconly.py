#!/usr/bin/env python

import camera

print("taking a picture")
imagePath = camera.capture()
print("captured %s" % imagePath)

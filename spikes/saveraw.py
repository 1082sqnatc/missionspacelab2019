import time
import picamera
import numpy as np
import cv2
with picamera.PiCamera() as camera:
    camera.resolution = (3280, 2464)
    camera. start_preview()
    time. sleep(2)
    camera.capture('image.data', 'yuv')
fd = open('image.data', 'rb')
f=np.fromfile(fd, dtype=np.uint8, count=3280*2464)
im = f.reshape((3280, 2464))
fd.close()
cv2.imwrite('rawconverted.jpg', im)
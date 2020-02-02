from picamera import PiCamera
from time import sleep
import ephem
import os

name = "ISS (ZARYA)"
l1 = "1 25544U 98067A   20033.25120128  .00002314  00000-0  49941-4 0  9990"
l2 = "2 25544  51.6428 301.0629 0005407 220.6572 248.5738 15.49135306210949"
iss = ephem.readtle(name, l1, l2)

iss.compute()

def get_latlon(cam):

    iss.compute()
    long_value = [float(i) for i in str(iss.sublong).split(":")]

    if long_value[0] < 0:

        long_value[0] = abs(long_value[0])
        cam.exif_tags['GPS.GPSLongitudeRef'] = "W"
    else:
        cam.exif_tags['GPS.GPSLongitudeRef'] = "E"
    cam.exif_tags['GPS.GPSLongitude'] = '%d/1,%d/1,%d/10' % (long_value[0], long_value[1], long_value[2]*10)

    lat_value = [float(i) for i in str(iss.sublat).split(":")]

    if lat_value[0] < 0:

        lat_value[0] = abs(lat_value[0])
        cam.exif_tags['GPS.GPSLatitudeRef'] = "S"
    else:
        cam.exif_tags['GPS.GPSLatitudeRef'] = "N"

    cam.exif_tags['GPS.GPSLatitude'] = '%d/1,%d/1,%d/10' % (lat_value[0], lat_value[1], lat_value[2]*10)
    print(str(lat_value), str(long_value))

def takePicture(counter):
        camera = PiCamera()
        get_latlon(camera)
        camera.resolution = (1296,972)
        camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))
        sleep(5)
        camera.capture('/tmp/image-'+ str(counter) + '.jpg')
        camera.stop_preview()
        camera.close()
        sleep(5)
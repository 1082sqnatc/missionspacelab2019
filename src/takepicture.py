from picamera import PiCamera
from time import sleep

def takePicture(counter):
        camera = PiCamera()
        camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))
        sleep(5)
        camera.capture('/tmp/image-'+ str(counter) + '.jpg')
        camera.stop_preview()
        camera.close()
        sleep(5)
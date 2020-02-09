#!/usr/bin/python3
import time
import cv2
from PIL import Image
import numpy
import os
from src.takepicture import takePicture
from src.dayornight import isDay
from src.finalportal import remove_portal
from src.stitcher import stitch

# This is the main executable file, pulls in cadets' libraries from src folder
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
    sequence = 0
    image = 0
    lastWasUsable = False
    panorama = 0
    while 1==1:
        print("Taking picture in sequence: " + str(sequence) + ", number: " + str(image))
        latestFile = takePicture(sequence,image,dir_path)
        
        # Load latest image from file
        result = Image.open(latestFile)
        
        # Check if usable (not night, and not 'flared')
        if isDay(latestFile):
            # If usable, and last was not, increment sequence number, reset image number
            if lastWasUsable==False :
                sequence = sequence + 1
                image = 1
            # If usable, cut out portal
            result = remove_portal(result)
            
            # covert from pil to cv2
            # TODO fix colour conversion
            result = numpy.array(result)
            result = result[:,:,::-1].copy()
            result = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
            
            # add to panorama
            if lastWasUsable==False :
                panorama = result
            else :
                (panorama, vis, xDrift, yDrift) = stitch([panorama, result], showMatches=True)
        
            # Save latest panorama
            cv2.imwrite(dir_path+"stitched-panorama-"+str(sequence)+".png",result)
            
            lastWasUsable = True
            image = image + 1
        else :
            lastWasUsable = False 
        
        #time.sleep(5) # don't sleep in production


if __name__ == '__main__':
    main()

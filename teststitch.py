import cv2
import imutils
import time
from PIL import Image
import numpy

from src.stitcher import stitch
#imageC = cv2.imread("/home/pi/Documents/git/missionspacelab2019/spikes/panorama/ISS042-E-104441.jpg")

imageArray = [
    "/home/pi/Documents/git/missionspacelab2019/spikes/panorama/ISS042-E-104433.jpg",
    "/home/pi/Documents/git/missionspacelab2019/spikes/panorama/ISS042-E-104437.jpg",
    "/home/pi/Documents/git/missionspacelab2019/spikes/panorama/ISS042-E-104441.jpg",
    "/home/pi/Documents/git/missionspacelab2019/spikes/panorama/ISS042-E-104445.jpg",
    "/home/pi/Documents/git/missionspacelab2019/spikes/panorama/ISS042-E-104449.jpg",
    "/home/pi/Documents/git/missionspacelab2019/spikes/panorama/ISS042-E-104453.jpg"
    ]

length = len (imageArray)
#pil_image = Image.open(imageArray[0]).convert('RGBA')
result = cv2.imread(imageArray[0],4)
#result = numpy.array(pil_image)
#result = result[:,:,::-1].copy()
result = imutils.resize(result)#, width=600)
for idx in range(1,length):
    print("========================")
    print("Index: " + str(idx))
    #pil_image = Image.open(imageArray[idx]).convert('RGBA')
    #nextimage = numpy.array(pil_image)
    #nextimage = nextimage[:,:,::-1].copy()
    nextimage = cv2.imread(imageArray[idx],4)
    nextimage = imutils.resize(nextimage) #, width=600)
    #cv2.imshow("Prev Result", result)

    (result, vis, xDrift, yDrift) = stitch([result, nextimage], showMatches=True)
    #cv2.imshow("Next Image", nextimage)
    #cv2.imshow("Keypoint Matches", vis)
    #cv2.imshow("Result Now", result)
    #time.sleep(20)
    
    #cv2.waitKey(0)
cv2.imwrite("spikes/stitched.png",result)

#imageA = cv2.imread("/home/pi/Documents/git/missionspacelab2019/spikes/panorama/ISS042-E-104433.jpg")
#imageB = cv2.imread("/home/pi/Documents/git/missionspacelab2019/spikes/panorama/ISS042-E-104437.jpg")
#imageA = imutils.resize(imageA, width=600)
#imageB = imutils.resize(imageB, width=600)
#(result, vis, xDrift, yDrift) = stitch([imageA, imageB], showMatches=True)


#imageA = cv2.imread("/home/pi/Documents/git/missionspacelab2019/spikes/panorama/ISS042-E-104437.jpg")
#image=result
#imageC = cv2.imread("/home/pi/Documents/git/missionspacelab2019/spikes/panorama/ISS042-E-104441.jpg")
#imageA = imutils.resize(imageA, width=600)
#imageC = imutils.resize(imageC, width=600)
#result = imutils.resize(result, width=600)
#(result2, vis2, xDrift2, yDrift2) = stitch([result, imageC], showMatches=True)


#cv2.imshow("Image A", imageA)
#cv2.imshow("Image B", imageB)
#cv2.imshow("Image C", imageC)
cv2.imshow("Result", result)
#cv2.imshow("Keypoint Matches", vis2)
#cv2.imshow("Result 2", result2)
cv2.waitKey(0)
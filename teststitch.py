import cv2
import imutils

from src.stitcher import stitch

imageA = cv2.imread("/home/pi/Documents/git/missionspacelab2019/spikes/panorama/ISS042-E-104433.jpg")
imageB = cv2.imread("/home/pi/Documents/git/missionspacelab2019/spikes/panorama/ISS042-E-104437.jpg")
imageC = cv2.imread("/home/pi/Documents/git/missionspacelab2019/spikes/panorama/ISS042-E-104441.jpg")
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)
imageC = imutils.resize(imageC, width=400)
(result, vis) = stitch([imageA, imageB], showMatches=True)
(result2, vis2) = stitch([result, imageC], showMatches=True)
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
#rotation = cv2.warpAffine(imageC, 90, (400, 400))
cv2.imshow("Image C", imageC)
cv2.imshow("Keypoint Matches", vis2)
cv2.imshow("Result", result2)
cv2.waitKey(0)
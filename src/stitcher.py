import numpy as np
import imutils
import cv2
import math

# Custom absolute function
def myfabs(x):
    if x < 0:
        return x*-1
    else :
        return x

# Heavily customised CV2 based stitcher algorithm, tuned to suit images with transparency
# Will also cut the resultant 'black' border from the joined image
def stitch(images, ratio=0.75, reprojThresh=4.0,
        showMatches=False):
    (imageB, imageA) = images
    (kpsA, featuresA) = detectAndDescribe(imageA)
    (kpsB, featuresB) = detectAndDescribe(imageB)

    M = matchKeypoints(kpsA, kpsB,
    featuresA, featuresB, ratio, reprojThresh)

    if M is None:
        return None

    (matches, H, status) = M
    
    firstMatchLeftIdx = matches[0][0]
    firstMatchRightIdx = matches[0][1]
    firstMatchLeftKps = kpsB[firstMatchLeftIdx]
    firstMatchRightKps = kpsA[firstMatchRightIdx]
    print("left kps")
    print(firstMatchLeftKps)
    print("right kps")
    print(firstMatchRightKps)
    yDrift = math.ceil(myfabs(firstMatchLeftKps[1] - firstMatchRightKps[1]))
    xDrift = math.ceil(myfabs(firstMatchLeftKps[0] - firstMatchRightKps[0]))
    print("xDrift: " + str(xDrift))
    print("yDrift: " + str(yDrift))
    newX = (imageB.shape[1]) + math.ceil(myfabs(xDrift))
    newY = (imageB.shape[0]) + math.ceil(myfabs(yDrift))
    print("New image size: " + str(newX) + "x" + str(newY))
    
    #result = cv2.warpPerspective(imageA, H,
    #    (imageA.shape[1] + imageB.shape[1], imageA.shape[0]))
    #result = cv2.warpPerspective(imageA, H,
    #    (imageB.shape[1] + math.ceil(myfabs(xDrift)),
    #    (imageB.shape[0] + math.ceil(myfabs(yDrift)) ) ))
    imageAWarped = cv2.warpPerspective(imageA, H,
        (newX,newY), borderMode=cv2.BORDER_TRANSPARENT )
    result = imageAWarped.copy()
    result[0:(imageB.shape[0]),
           0:(imageB.shape[1])] = imageB
    (h,w,c) = imageAWarped.shape
    maxj = 0
    maxi = 0
    mini = h
    minj = w
    for i in range(h):
        for j in range(w):
            color = imageAWarped[i,j]
            hascolor = (color[0] != 0 or color[1] != 0 or color[2] != 0)
            haseithercolor = hascolor
            if haseithercolor == False:
                colororig = result[i,j]
                if colororig[0] != 0 or colororig[1] != 0 or colororig[2] != 0:
                    haseithercolor = True
                 
            if hascolor:
                result[i,j] = color
            if haseithercolor:
                if i > maxi:
                    maxi = i
                if j > maxj:
                    maxj = j
                if j<minj:
                    minj = j
                if i < mini:
                    mini = i
    # trim to maxi and maxj
    print("maxi: " + str(maxi) + ", maxj: " + str(maxj))
    print("mini: " + str(mini) + ", minj: " + str(minj))
    result = result[minj:maxj,mini:maxi]
    #result[0:(imageAWarped.shape[0]),
    #       0:(imageAWarped.shape[1])] = imageAWarped

    if showMatches:
        vis = drawMatches(imageA, imageB, kpsA, kpsB, matches,
            status)
        return (result, vis, xDrift, yDrift)
    return result

# Feature detection in the image
def detectAndDescribe(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    descriptor = cv2.ORB_create(nfeatures=1500)
    (kps, features) = descriptor.detectAndCompute(image, None)
    kps = np.float32([kp.pt for kp in kps])
    return (kps, features)

# Matching keypoints between two images
def matchKeypoints(kpsA, kpsB, featuresA, featuresB,
        ratio, reprojThresh):
    matcher = cv2.DescriptorMatcher_create("BruteForce")
    rawMatches = matcher.knnMatch(featuresA, featuresB, 2)
    matches = []
    for m in rawMatches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            matches.append((m[0].trainIdx, m[0].queryIdx))
    if len(matches) > 4:
        ptsA = np.float32([kpsA[i] for (_, i) in matches])
        ptsB = np.float32([kpsB[i] for (i, _) in matches])
        (H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC,
            reprojThresh)
        return (matches, H, status)
    return None

# Draw the matches on an image (for testing)
def drawMatches(imageA, imageB, kpsA, kpsB, matches, status):
    (hA, wA) = imageA.shape[:2]
    (hB, wB) = imageB.shape[:2]
    vis = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")
    vis[0:hA, 0:wA] = imageA
    vis[0:hB, wA:] = imageB
    for ((trainIdx, queryIdx), s) in zip(matches, status):
        if s == 1:
            ptA = (int(kpsA[queryIdx][0]), int(kpsA[queryIdx][1]))
            ptB = (int(kpsB[trainIdx][0]) + wA, int(kpsB[trainIdx][1]))
            cv2.line(vis, ptA, ptB, (0, 255, 0), 1)
        return vis
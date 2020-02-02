from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True,
    help="path to import directory of images to stitch")
ap.add_argument("-o", "--output" , type=str, required=True,
    help="path to the output image")
args = vars9ap.parse_args())

print("[INFO] loading images...")
imagePaths = sorted(list
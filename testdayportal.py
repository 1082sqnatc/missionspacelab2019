#!/usr/bin/python3
import time
import cv2
from PIL import Image
from src.dayornight import isDay


# This is the main executable file, pulls in cadets' libraries from src folder
def main():
    #dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
    # test known full night
    print("================")
    print("Test known night")
    img = Image.open("../../../Sample_Data/zz_astropi_1_photo_455.jpg")
    result = isDay(img)
    print(result)
    # test known flared
    print("================")
    print("Test known flared")
    img = Image.open("../../../Sample_Data/zz_astropi_1_photo_426.jpg")
    result = isDay(img)
    print(result)
    # test known day
    print("================")
    print("Test known day")
    img = Image.open("../../../Sample_Data/zz_astropi_1_photo_372.jpg")
    result = isDay(img)
    print(result)
    # test borderline bad image
    print("================")
    print("Test borderline bad image")
    img = Image.open("../../../Sample_Data/zz_astropi_1_photo_424.jpg")
    result = isDay(img)
    print(result)
    # test borderline good image
    print("================")
    print("Test borderline good image")
    img = Image.open("../../../Sample_Data/zz_astropi_1_photo_418.jpg")
    result = isDay(img)
    print(result)

if __name__ == '__main__':
    main()

#!/usr/bin/python3
import time
from os import listdir

from src.dayornight import isDay

#def take_picture():
#    print("pic taken")
# TODO main executable file, pulls in cadets' libraries from lib fold
def main():
    files = listdir ("../Sample_Data/")
    for fname in files:
        print (str("Processing" + fname)) # Prints the processing notification
        imageFile = "../Sample_Data/" + fname #Stores the current file name
       # t0 = time.time()
        result = isDay(imageFile)
       # t1 = time.time()
       # t = t1 - t0
       # print (str(t))   
       # print(result)
    # Now process a folder of image...
    


if __name__ == '__main__':
    main()

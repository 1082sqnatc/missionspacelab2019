#!/usr/bin/python3
import time
from os import listdir

from src.dayornight import isDay

#def take_picture():
#    print("pic taken")
# TODO main executable file, pulls in cadets' libraries from lib fold
def main():
    files = listdir ("spikes/images")
    for fname in files:
        print (str(fname + " prosesing file name"))
        t0 = time.time()
        isDay("spikes/images/"+fname)
        t1 = time.time()
        t = t1 - t0
        print (str(t))
    # Now process a folder of image...
    


if __name__ == '__main__':
    main()

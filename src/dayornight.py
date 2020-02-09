
import numpy as np

def isDay(imageFile):
    fd = open(imageFile, 'rb')
    f=np.fromfile(fd, dtype=np.uint8, count=2592*1944)
    lum = 0
    count = 0
    
    miny = 4000000
    maxy = -1
    
  #  print("Size of array (data points): " + str(len(f)))
    
    while count*3*16 < len (f):
        y = f[count*3*16]
        lum = y + lum
        count = count + 1
        
        if y > maxy:
            maxy = y
            
        if y < miny:
            miny = y
    
    avg = lum/count
    
   # print (str(miny)+" is minimum y value")
   # print (str(maxy)+" is maximum y value")
    print (str(avg)+" is the average y value")
   # print (str(count)+" is the number of pixels analysed")
    
    
    
    
    if avg < 50 or avg > 130:
        return False
    
    else:
        return True
from PIL import Image
from PIL import ImageOps
import numpy
import time
import cv2

# Calculates the average brightness of a 200x200 image, sampling every 10 pixels for speed
def calcBrightness(img):
    x = 0
    y = 0
    c_brightness = 0;
    count = 0
    while x < 200 and y < 200:
        pixelBGR = img.getpixel((x,y))
        B, G, R = pixelBGR
        c_brightness = (c_brightness + ((B+G+R) / 3))
        if x == 199:
            y = y + 10
            x = 0
        else:
            x = x + 10
        count = count + 1
    print("total brightness: " + str(c_brightness) + ", sample count: " + str(count))
    return c_brightness / count

# Detects a good day vs night image of a portal
# Eliminates Night, and sunrise/sunset 'flared' images
def isDay(image):
    #img = open(imageFile, 'rb')
    #with Image.open(img) as image:
        width, height = image.size # Determins width and height of image and stores it
        print("Width =", width, "\n Height =", height) # Prints width and height
        total_pixels = width * height # Calculates the total number of pixels in the image
        print("Total Pixels =", total_pixels) # Prints total pixels 
        c_width = width / 2 # Calculates middle of x-axis
        c_height = height / 2 # Calculates middle of y-axis
        store_total = 40000 # Stores total pixels of the crop area
        
        #img_cv2 = cv2.imread(imageFile)
        border_tl = (0, 0, 200, 200) # Crops image to top left 200x200
        border_tr = ((width-200), 0, width, 200) # Crops image to top right 200x200
        border_bl = (0, (height-200), 200, height) # Crops image to botom left 200x200
        border_br = ((width-200), (height-200), width, height) # Crops image to bottom right 200x200
        border_ct = ((c_width-100), (c_height-100), (c_width+100), (c_height+100)) # Crops image to center 200x200
        Top_Left = image.crop(border_tl) # " "
        Top_Right = image.crop(border_tr) # " "
        Bottom_Left = image.crop(border_bl) # " "
        Bottom_Right = image.crop(border_br) # " "
        Center_Data = image.crop(border_ct) # " "
        print("pixels in tl: " + str(Top_Left.size))
        print("pixels in tr: " + str(Top_Right.size))
        print("pixels in bl: " + str(Bottom_Left.size))
        print("pixels in br: " + str(Bottom_Right.size))
        print("pixels in ct: " + str(Center_Data.size))
        #Top_Left = numpy.array(Top_Left)
        #Top_Right = numpy.array(Top_Right)
        #Bottom_Left = numpy.array(Bottom_Left)
        #Bottom_Right = numpy.array(Bottom_Right)
        #Center_Data =  numpy.array(Center_Data)
        #Top_Left = cv2.cvtColor(Top_Left, cv2.COLOR_RGB2BGR)
        #Top_Right = cv2.cvtColor(Top_Right, cv2.COLOR_RGB2BGR)
        #Bottom_Left = cv2.cvtColor(Bottom_Left, cv2.COLOR_RGB2BGR)
        #Bottom_Right = cv2.cvtColor(Bottom_Right, cv2.COLOR_RGB2BGR)
        #Center_Data = cv2.cvtColor(Center_Data, cv2.COLOR_RGB2BGR)


        c_brightness = calcBrightness(Center_Data)
        tl_brightness = calcBrightness(Top_Left)
        tr_brightness = calcBrightness(Top_Right)
        bl_brightness = calcBrightness(Bottom_Left)
        br_brightness = calcBrightness(Bottom_Right)

        avg = (tl_brightness + tr_brightness + bl_brightness + br_brightness) / 4
        rg = c_brightness - avg
        print("Centre vs border diff: " + str(rg))
        
        # Our testing shows a rg of 40 is a good analog for day vs night/flared pictures
        if rg > 40:
            return True
        else:
            return False
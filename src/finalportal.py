from PIL import Image # Imports the Image function from Pillow so that the image can be edited.

# Removes the portal from an ISS image, and sets those pixels as transparent to allow stitching
def remove_portal(img):
    img = img.convert('RGBA') # Image is converted to support transparrency (alpha)
    datas = img.getdata() # Image data is stored into a variable

    newData = list()
    for item in datas: # Goes through each pixel, one by one.
        if item[0] <= 50 and item[1] <=50 and item[2] <= 50: # Checks to see if the current pixels are black or dark/medium greys
            newData.append((255, 255, 255, 0)) # Converts current pixel to alpha (Transparrent)
        else:
            newData.append(item) # Leaves the current pixel as is
            
    img.putdata(newData) # Saves the new data into the original img data
    return img
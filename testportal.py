from PIL import Image # Imports the Image function from Pillow so that the image can be edited.
from src.finalportal import remove_portal

img = Image.open('spikes/Sample_Data/zz_astropi_1_photo_181.jpg') # Opens Current image using Pillow
img = remove_portal(img) # Calls the function
img.save("spikes/test1.png") # Saves the image as a PNG File
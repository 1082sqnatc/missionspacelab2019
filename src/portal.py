import numpy as np
import cv2
import matplotlib.pyplot as plt

original_image = cv2.imread("../spikes/portal.jpg")

img = original_image

edges = cv2.Canny(img,150,200)
figure_size=15
plt.figure(figsize=(figure_size,figure_size))
plt.subplot(1,2,1),plt.imshow(img)
plt.title('Original image'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(edges,cmap='gray')
plt.title("Edge Image"), plt.xticks([]), plt.yticks([])
plt.show()


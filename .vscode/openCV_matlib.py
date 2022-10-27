import cv2
from matplotlib import pyplot as plt

img = cv2.imread('sea.jpg', 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

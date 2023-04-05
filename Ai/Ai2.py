import cv2
import numpy as np
import matplotlib.pyplot as plt

imge = cv2.imread("Name.jpg")
rgp = cv2.cvtColor(imge , cv2.COLOR_BGR2GRAY)

plt.imshow(imge)
plt.waitforbuttonpress(0)
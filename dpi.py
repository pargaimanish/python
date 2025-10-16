

from PIL import Image, ImageEnhance

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

im = Image.open("Screenshot 2025-04-24 at 8.17.50 PM.png").convert("L")  
enhancer = ImageEnhance.Contrast(im)
im_c = enhancer.enhance(2.0)

im_c.save("test-400.png", dpi=(400, 400))



img = cv.imread('test-400.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
plt.imsave("test-01.png", thresh4, cmap='gray', dpi=400)


for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
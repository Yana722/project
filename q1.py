import cv2
from matplotlib import pyplot as plt
from SSDmodel import SSD
import numpy as np

imgL = cv2.imread("./2018-07-09-16-11-56_2018-07-09-16-11-56-702-left.jpg", cv2.IMREAD_GRAYSCALE) # left image
imgR = cv2.imread("./2018-07-09-16-11-56_2018-07-09-16-11-56-702-right.jpg", cv2.IMREAD_GRAYSCALE) # right image

# Display the images
#plt.subplot(1,2,1)
#plt.imshow(imgL, cmap='gray')
#plt.title('Left image')
#plt.axis('off')

#plt.subplot(1,2,2)
#plt.imshow(imgR, cmap='gray')
#plt.title('Right image')
#plt.axis('off')

#plt.show()

dmax = 79
ssdL = SSD(imgL, imgR, 33, dmax)

plt.imshow(ssdL, cmap = 'gray')
plt.axis('off')
plt.show()

#gaussian_kernel = cv2.getGaussianKernel(15, 5)
#gaussian_kernel = np.outer(gaussian_kernel, gaussian_kernel)
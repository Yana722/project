import time
import cv2
from matplotlib import pyplot as plt
from SSDmodel import SSD
from NCCmodel import NCC
from SSD_Gaus import SSD_Gaus
from SSD_sub_pixel import SSD_sub_pixel
from SSD_Smooth import SSD_Smooth
from q2 import evaluate
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

dmax = 100
window_size = 7
start = time.time()
weight = 0.5
sub_pixel_weight = 2
ssd = SSD(imgL, imgR, window_size, dmax)
#ssd = SSD_Gaus(imgL, imgR, window_size, dmax)
#ssd = SSD_Smooth(imgL, imgR, window_size, dmax, ssd, weight)
#ssd = SSD_sub_pixel(imgL, imgR, window_size, dmax, sub_pixel_weight)
#ncc =  NCC(imgL, imgR, window_size, dmax)
end = time.time()

print("The runtime of algorithm is", int(end-start), "seconds")

plt.imshow(ssd, cmap='gray')
plt.axis('off')
plt.show()

#plt.imshow(ncc, cmap='gray')
#plt.axis('off')
#plt.show()

img_gt = cv2.imread("./2018-07-09-16-11-56_2018-07-09-16-11-56-702-disparity.png", cv2.IMREAD_UNCHANGED)/256
evaluate(ssd, img_gt)
import copy
import cv2
import numpy as np

def NCC_Gaus(imgL, imgR, size, dmax):

    ncc_image = copy.deepcopy(imgL)

    width = len(imgL)
    lenth = len(imgL[0])
    blank = size//2

    # how about sobel, which makes edge more important？
    #sobel_kernel_x = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    # Y-Direction Kernel (Horizontal)
    #sobel_kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    # Use Sobel filter to approximate the derivative of gaussian (for both x and y)
    #dx = cv2.filter2D(imgL, -1, sobel_kernel_x)
    #dy = cv2.filter2D(imgL, -1, sobel_kernel_y)

    #imgL = np.hypot(dx, dy)  # equivalent to sqrt(x1**2 + x2**2), element-wise

    for i in range(width): # the loop for the y-axis in left image
        for j in range(lenth): # the loop for the x-axis in left image

            best = None
            result = None

            # check size is enouth or not
            if i-blank < 0:
                i_start = 0
            else:
                i_start = i-blank
            if i+blank > width:
                i_end = width
            else:
                i_end = i+blank+1

            if j-blank < 0:
                j_start = 0
            else:
                j_start = j-blank
            if j+blank > lenth:
                j_end = lenth
            else:
                j_end = j+blank+1

            windowL = np.ascontiguousarray(imgL[i_start:i_end, j_start:j_end])
            lsize = len(windowL)
            rsize = len(windowL[0])
            # use Gaussian kernel there but we can change it
            # use a kernel shows the importance of pixels in the matching window
            gk1 = cv2.getGaussianKernel(lsize, 0.3*((lsize-1)*0.5-1)+0.8)
            gk2 = cv2.getGaussianKernel(rsize, 0.3*((lsize-1)*0.5-1)+0.8)
            Gaussian_kernel2d = np.outer(gk1, gk2)

            windowL = cv2.filter2D(windowL, -1, Gaussian_kernel2d)

            #kernel_up = size - len(windowL)//2
            #kernel_down = size + len(windowL) - len(windowL)//2
            #kernel_left = size - len(windowL[0])//2
            #kernel_right = size + len(windowL[0]) - len(windowL[0])//2
            #window_kernel = np.ascontiguousarray(Gaussian_kernel2d[kernel_up:kernel_down,kernel_left:kernel_right])
            #windowL = cv2.filter2D(windowL,-1,window_kernel)

            rsize = len(windowL[0])
            rblank = rsize//2

            if j < dmax:
                krange_start = 0
            else:
                krange_start = j-dmax
            for k in range(krange_start, j+1): # the loop for the x-axis in right image

                if k-rblank < 0:
                    k_start = 0
                    k_end = rsize
                elif k+rblank >= lenth:
                    k_start = lenth-rsize
                    k_end = lenth
                elif rsize%2 != 0:
                    k_start = k-rblank
                    k_end = k+rblank+1
                else:
                    k_start = k-rblank
                    k_end = k+rblank

                windowR = np.ascontiguousarray(imgR[i_start:i_end, k_start:k_end])
                windowR = cv2.filter2D(windowR, -1, Gaussian_kernel2d)

                ncc = np.mean(np.multiply(windowL, windowR)) / (np.std(windowL) * np.std(windowR))

                if best==None or ncc>best:
                    best = ncc
                    result = np.abs(j-k)

            ncc_image[i,j] = result

    return ncc_image
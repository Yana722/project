import copy
import cv2
import numpy as np

def NCC(imgL, imgR, size, dmax):

    ncc_image = copy.deepcopy(imgL)

    width = len(imgL)
    lenth = len(imgL[0])
    blank = size//2

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

                ncc = np.mean(np.multiply(windowL, windowR)) / (np.std(windowL) * np.std(windowR))

                if best==None or ncc>best:
                    best = ncc
                    result = np.abs(j-k)

            ncc_image[i,j] = result

    return ncc_image
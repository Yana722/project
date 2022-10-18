import copy
import numpy as np

def SSD_Smooth(imgL, imgR, size, dmax, ssd_out, lambd):

    ssd_image = copy.deepcopy(ssd_out)

    width = len(imgL)
    lenth = len(imgL[0])
    blank = size//2

    for i in range(1, width-1): # the loop for the y-axis in left image
        for j in range(1,lenth-1): # the loop for the x-axis in left image

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
                d = np.abs(j-k)
                smooth = lambd * (np.abs(d-ssd_out[i-1, j]) + np.abs(d-ssd_out[i, j-1]) + np.abs(d-ssd_out[i+1, j]) + np.abs(d-ssd_out[i, j+1]) + np.abs(d-ssd_out[i-1, j-1]) + np.abs(d-ssd_out[i-1, j+1]) + np.abs(d-ssd_out[i+1, j-1]) + np.abs(d-ssd_out[i+1, j+1]))

                ssd = np.sum((windowL - windowR) ** 2) + smooth

                if best==None or ssd<best:
                    best = ssd
                    result = np.abs(j-k)

            ssd_image[i,j] = result

    return ssd_image
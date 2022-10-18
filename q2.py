import copy
import numpy as np

def evaluate(img_out, ground_truth):
    gt = copy.deepcopy(ground_truth)
    count_true = 0
    count_false = 0
    for i in range(len(gt)):
        for j in range(len(gt[0])):
            if gt[i][j] > 0:
                gt[i][j] = 1
                count_true += 1
            else:
                gt[i][j] = 0
                count_false += 0
    img_out = img_out * gt

    rms = np.sqrt(np.sum((img_out - ground_truth) ** 2) / count_true)
    print("The rms (root mean squared) error is", rms)

    error = np.abs(img_out - ground_truth)
    error_4 = (np.sum(error < 4) - count_false) / count_true
    error_2 = (np.sum(error < 2) - count_false) / count_true
    error_1 = (np.sum(error < 1) - count_false) / count_true
    error_05 = (np.sum(error < 0.5) - count_false) / count_true
    error_025 = (np.sum(error < 0.25) - count_false) / count_true
    print("The fractions of pixels with errors less than 4 pixels is", error_4)
    print("The fractions of pixels with errors less than 2 pixels is", error_2)
    print("The fractions of pixels with errors less than 1 pixels is", error_1)
    print("The fractions of pixels with errors less than 0.5 pixels is", error_05)
    print("The fractions of pixels with errors less than 0.25 pixels is", error_025)

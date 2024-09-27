import cv2
import numpy as np
from matplotlib import pyplot as plt

def compute_histogram(arr, min_v, max_v):
    # Create a mask to filter out pixels within the range [min_v, max_v]
    mask = (arr >= min_v) & (arr <= max_v)
    # Calculate the histogram within the range [min_v, max_v]
    hist = cv2.calcHist([arr[mask]], [0], None, [max_v - min_v + 1], [min_v, max_v + 1])
    return hist.flatten()

def compute_cdf(hist, min_v, max_v):
    cdf = np.cumsum(hist)
    cdf_normalized = ((max_v - min_v) / cdf[-1]) * cdf + min_v
    return cdf_normalized.astype(np.uint8)


def draw_histogram_(hists):
    ### draw a bar picture of the given histogram
    plt.figure()
    plt.bar(range(len(hists)), hists)
    plt.show()
    
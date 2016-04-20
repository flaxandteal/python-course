#!/usr/bin/env python3

import scipy

import numpy as np
import matplotlib.pyplot as pyplot

import skimage.morphology
import skimage.filters
import skimage.io


# Segmentation /without/ the scikit.segmentation module...
# With thanks to the scikit documentation - you will find useful information there

# PLEASE NOTE: this is a basic, instructional approach, breaking down the steps
# so that you can experiment with each. The results will not be
# as effective as when using more advanced, optimized algorithms aimed. Check out
# OpenCV and ITK for more ideas.

# Challenge 1: produce plots for each of the marked letters (use pyplot.imshow),
#    Save to a figure if you do not want interactive plots every time you run...
# Challenge 2: add explanatory comments for each code line
def run():
    knee_image = skimage.io.imread('knee.png', as_grey=True)

    # Plot A - knee_image

    elevation_map = skimage.filters.sobel(knee_image)

    # Plot B - elevation_map

    markers = np.zeros_like(knee_image)
    markers[knee_image < 0.2] = 1
    markers[knee_image < 0.164] = 2

    # Plot C - markers

    segmentation = skimage.morphology.watershed(elevation_map, markers)

    # Plot D - segmentation

    segmentation = segmentation - 1
    segmentation = scipy.ndimage.binary_fill_holes(segmentation)

    # Plot D - segmentation

    labeled_knee_image, _ = scipy.ndimage.label(segmentation)

    # Plot E - labeled_knee_image

    rows, cols = labeled_knee_image.shape
    centre_region = labeled_knee_image[rows // 2, cols // 2]

    tibia = (labeled_knee_image != centre_region)

    pyplot.imshow(tibia, interpolation='nearest')

    np.save('tibia.npy', tibia)

    pyplot.show()

if __name__ == '__main__':
    run()

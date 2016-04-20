#!/usr/bin/env python3

import scipy

import numpy as np
import matplotlib.pyplot as pyplot
import sys

import skimage.segmentation
import skimage.filters
import skimage.io


def run():
    try:
        labeled_knee_image = np.load('tibia.npy')
    except FileNotFoundError:
        print("Could not load output of segment.py (make sure you run it first)")
        sys.exit(1)

    # Find the boundary of our tibia
    boundary = skimage.segmentation.find_boundaries(labeled_knee_image)

    # Turn that into a list of coordinates
    points = np.transpose(np.nonzero(boundary))

    # Triangulate
    tri = scipy.spatial.Delaunay(points)

    # Now we see the limitation...
    pyplot.triplot(points[:,0], points[:,1], tri.simplices.copy())
    pyplot.plot(points[:,0], points[:,1], 'o')
    pyplot.show()

if __name__ == '__main__':
    run()

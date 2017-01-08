#!/usr/bin/env python3

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D, axes3d
import numpy
import datetime
import os

# Load rainfall data
X, Y, rainfall = numpy.loadtxt("rainfall-radar.csv").T

# Some clever 3D plotting
fig = pyplot.figure()
axes = Axes3D(fig)
axes.plot_trisurf(X, Y, rainfall)

# Save image labelled by day data created
creation_timestamp = os.path.getctime("rainfall-radar.csv")
d = datetime.date.fromtimestamp(creation_timestamp)
image_filename = "%d-%d-%d-rainfall.png" % (d.year, d.month, d.day)
pyplot.savefig(image_filename)

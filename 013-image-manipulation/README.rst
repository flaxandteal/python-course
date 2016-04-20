Basic Image Segmentation with Scikit
====================================

This is a basic tutorial starting with a knee image, in 2D.
See <http://www.pcir.org/researchers/24759123_20010101.html> for the
full 3D dataset.

The segment.py script uses a series of numpy, scipy and scikit-image
routines to extract the lower part of the tibia. You can experiment
adjusting values. In practice, especially if you wish to automate
rather than using manually entered values, you will probably use
something like OpenCV, ITK or SimpleITK. These all have Python
bindings (although not yet defaulting to Python3).

The mesh.py script shows how you can achieve a Delaunay triangulation
using numpy. However, there is a limitation here - it will be convex.
While it is a much heavier library, CGAL is sufficiently powerful
to do non-convex 2D and 3D triangulations. See
<https://github.com/CGAL/cgal-swig-bindings/wiki/Package_wrappers_available>
for more detail on SWIG bindings.

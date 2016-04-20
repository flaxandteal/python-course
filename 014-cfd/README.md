CFD Python Introduction
=======================

NOTE: These notes are experimental - please file any feedback issues on Github

This should get you up and running with a stock FEniCS tutorial - you should
checkout their tutorial at
<http://fenicsproject.org/documentation/dolfin/1.0.1/python/demo/pde/navier-stokes/python/documentation.html>

Install Paraview:

    sudo apt-get install paraview

Install FEniCS:

    sudo add-apt-repository ppa:fenics-packages/fenics
    sudo apt-get update
    sudo apt-get install fenics

Head to a directory you have write access to (e.g. home directory):

    cp -R /usr/share/dolfin/demo/documented/navier-stokes .
    cd navier-stokes/python

Now you can run the FEniCS Navier-Stokes simulation:

    python demo_navier-stokes.py

Note that this uses Python2, unlike this Python course.

The resulting *.pvd* file may be opened using Paraview.

If you would like this built into a session in the course, please note it on
your feedback sheet.

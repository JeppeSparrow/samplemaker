# -*- coding: utf-8 -*-
"""
02_Tutorial_CellReferences
"""

# In this tutorial we learn to create multiple GDS cells and instantiate
# references (single or array)

# Let's import basic stuff
import samplemaker.layout as smlay  # used for layout
import samplemaker.makers as sm  # used for drawing

# Create a simple mask layout
themask = smlay.Mask("02_Tutorial_CellReferences")

# Let's draw a simple shape
base = sm.make_rect(x0=0, y0=0, width=2, height=10)
base += sm.make_circle(x0=4, y0=5, r=1, to_poly=True)

# We would like to make identical copies of this.
# Instead of using base.copy() which duplicates the memory and GDS file size
# we can place base in a GDS CELL and refer to it in our main cell

# Create a new GDS cell called "BCELL"
themask.addCell(cellname="BCELL", geom_group=base)

# Now create a single reference to it
geomE = sm.make_sref(
    x0=20, y0=15, cellname="BCELL", group=base, mag=1.0, angle=0, mirror=False
)
# Note that we can move, rotate, scale and mirror the reference

# Let's create another instance but scaledby 50%  and rotated by 45 degrees
geomE += sm.make_sref(
    x0=40, y0=15, cellname="BCELL", group=base, mag=1.5, angle=45, mirror=False
)

# Now geomE contains a single instance of BCELL

# We can continue and make another base cell with a different name
b2 = sm.make_rounded_rect(x0=0, y0=0, width=7, height=3, corner_radius=1)
# We can add an instance of BCELL, the only rule is avoiding cyclic references
b2 += sm.make_sref(x0=10, y0=0, cellname="BCELL", group=base)

# Now let's add this to the layout and call it B_TWO
themask.addCell(cellname="B_TWO", geom_group=b2)

# Referring to B_TWO in the main cell will include both B_TWO and a reference to BASE
# There is no limit in concatenating references.
# Instead of creating a single reference, let's use reference arrays
# We can create an array of references on a regular grid specified by the unit cell vectors
geomE += sm.make_aref(
    x0=0,
    y0=50,
    cellname="B_TWO",
    group=b2,
    ncols=3,
    nrows=4,
    ax=25.0,
    ay=0.0,
    bx=0.0,
    by=20.0,
)
# Above we created a reference starting in (0,50) and a grid with 3 rows and 4 columns
# the unit cell vectors are [25,0] and [0,20], i.e. a rectangular grid.

# If you at any point require flattening the geometry, you simply call
geomFlatten = geomE.flatten()
# Note that flatten() creates a new geometry that needs to be stored.
# You can pass a list of layer to flatten to only select some of the layers during the flattening process
# You need flattening to perform boolean operations with SREF/AREF, otherwise those entities will be ignored.
themask.addCell(cellname="FLATCELL", geom_group=geomFlatten)

# Instantiate it into the main cell
geomE += sm.make_sref(x0=150, y0=0, cellname="FLATCELL", group=geomFlatten)

# Let's add all to main cell
themask.addToMainCell(geom_group=geomE)

# Export to GDS
themask.exportGDS()

# Finished!

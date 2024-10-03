# -*- coding: utf-8 -*-
"""
03_Tutorial_GroupManipulation
"""


# In this tutorial we learn what we can do with geometries after they are created
# and some interesting operations

# Let's import basic stuff
import samplemaker.layout as smlay # used for layout 
import samplemaker.makers as sm # used for drawing

# Create a simple mask layout
themask = smlay.Mask("03_Tutorial_GroupManipulation")

# Let's start again from a simple shape
base = sm.make_rect(x0=0,y0=0,width=2,height=10)
base += sm.make_circle(x0=4,y0=5,r=1,to_poly=True,layer=3)

# You can create empty groups
geomE = sm.GeomGroup()

# We can translate,rotate,scale and mirror (see previous tutorials)

# Layer selection
# We can create a new group that only selects one or more layers
gsel = base.select_layer(1)
# or removes some layers
gsel2 = base.deselect_layers([1])
# Note that both require assignments, the original "base" is untouched

# It might be interesting to calculate the bounding box:
bb = base.bounding_box()
rbox=bb.toRect() # rbox contains 1 rectangle size of the bounding box

# Path/text polygon conversion
# You can decide to create all paths/polygons and circular elements with to_poly=False
# then later you want to convert all to polygon. Then run:
base.all_to_poly()
# Or
base.path_to_poly()
# or
base.text_to_poly()
#depending on what you need

# Adding base to geomE
geomE+=base

# RESIZING operations
# You can resize polygon isotropically
res1 = base.copy() # We keep base for later
res1.set_layer(1) # put all in layer 1
# The following bloats the polygons in layer 1 by 2 um in all directions, note that elements will merge
# Use negative values to shrink
res1.poly_resize(offset=2.0,layer= 1)
res1.translate(dx=20,dy= 0)

geomE+=res1 # adding the result to the main Geometry

# OUTLINING
# You can make the outline of a shape:
out1 = base.copy()
out1.set_layer(1)
# Creates an outline of the shape with width of 0.3 um
out1.poly_outlining(offset=0.3,layer= 1)
out1.translate(dx=40, dy=0)
geomE+=out1

# Let's add all to main cell
themask.addToMainCell(geom_group=geomE)    

# Export to GDS
themask.exportGDS()

# Finished!
# -*- coding: utf-8 -*-
"""
01_Tutorial_Shapes
"""

# In this tutorial we start drawing basic shapes 

# Let's import basic stuff
import samplemaker.layout as smlay # used for layout 
import samplemaker.makers as sm # used for drawing

# Create a simple mask layout
themask = smlay.Mask("01_Tutorial_Shapes")

# Let's look at all shapes available:
    
# Rectangles:
# Here we use numkey parameter to place the origin (0,2) at the lower-right corner
# look at the num keypad on the keyboard to identify the corners (5 is center).
# We also set a different layer  
geomE = sm.make_rect(
                    x0=0,
                    y0=2,
                    width=6,
                    height=3,
                    numkey=3,
                    layer=2
                    )

# Circles:
# A circle in (10,0) with radius 3 um
geomE += sm.make_circle(
                        x0=10,
                        y0=0,
                        r=3
                        )

# Circles are stored in memory as perfect circles with center and radius.
# But you can convert them to polygons straight away:
# Note that you can specify how many vertices should be used
geomE += sm.make_circle(
                        x0=20,
                        y0=0,
                        r=3,
                        layer=1,
                        to_poly=True,
                        vertices=50
                        )           


# Polygons:
# Arbitrary shaped polygons (but avoid self-intersections)
geomE += sm.make_poly(
                    xpts=[30,40,35,31],
                    ypts=[0,-2,8,7]
                    );

# Path:
# Open piece-wise paths with a width
geomE += sm.make_path(
                    xpts=[50,50,60],
                    ypts=[0 ,10,10],
                    width=1,
                    to_poly=True
                    )
# Note that path objects are created as true GDS PATHS if to_poly is set to False
# The GDS path is not recommended as it might be rendered differently from 
# viewer to viewer. To get a polygon instead use to_poly=True

# Text:
geomE += sm.make_text(
                    x0=70,
                    y0=0,
                    text="Hello",
                    height= 10,
                    width= 1,
                    numkey=1,
                    to_poly=True
                    )
# As for path, text is created as true GDS TEXT if to_poly is set to False
# You can use GDS TEXT for annotations (e.g. not for actual lithography)
# To create real polygon text, use to_poly=True. Samplemaker uses stencil fonts
# to avoid floating letters in undercut
# A good ratio width/height is 1/10 as in the example above.

# More shapes...

# Rounded rectangle
geomE += sm.make_rounded_rect(
                            x0=0,
                            y0=20,
                            width=10,
                            height=5,
                            corner_radius=1,
                            resolution = 8
                            )
# Creates a rectangle with 1 um radius rounded edges.

# Ellipse
geomE += sm.make_ellipse(
                        x0=15,
                        y0=20,
                        rX=3,
                        rY=2,
                        rot=45,
                        to_poly=True
                        )
# Ellipse centered in (15,20) X-radius=3, Y-radius=2, 45 degree rotation
# As for circles, you can store the ellipses or convert them straight to polygons
# Except for circles, I recommend always setting to_poly=True. Default is false

# Rings
geomE += sm.make_ring(
                    x0=30,
                    y0= 20,
                    rX=5,
                    rY= 5,
                    rot= 0,
                    w= 0.5,
                    to_poly=True
                    )
# Same as ellipse, but you can specify a width (0.5 um here).
# Can be used for elliptical rings as well (set two different radii, here it's 5 and 5)

# Arcs
geomE += sm.make_arc(
                    x0=40,
                    y0=20,
                    rX=5,
                    rY=5,
                    rot=0,
                    w=0.5,
                    a1=0,a2=90,
                    to_poly=True
                    )
# Same as ring, but you can specify an initial and a final angle to only draw a sector (here from 0 to 90 degrees)
# Can be also elliptical arcs

# Width-variable paths
geomE += sm.make_tapered_path(xpts=[50,55,60],
                              ypts=[15,20,23],
                              widths= [1,0.5,2]
                              )
# Same as path but allows you to specify a list of widths as third arguments
# the path width is linearly tapered from point to point. Produces a polygon object
    
# This is all you can do with basic samplemaker makers, we are only missing SREF and AREF
# which will be the topic of next tutorial.

# Time to add this to the mask
themask.addToMainCell(geomE)

# Export to GDS
themask.exportGDS()

# Finished!

""" Class for wrangling data
"""

import pylab as pl
import pymc as mc

puzzle_t = pl.array([0., .25, .375, .5, .625, .75, 1.])
puzzle_x = .25 + .5*pl.array([-.5, .375, .125, .5, .875, .625, 1.5])
puzzle_y = .5*pl.array([0., 0., .35, .7, .35, 0., 0.])
puzzle_V = pl.array([1.e-6, .0005, .0005, .01, .0005, .0005, 1.e-6])

import networkx as nx
import pylab as pl

import models

# put messy matplotlib code here so I don't have to look at it if I
# don't want to

def plot_nub(a, b):
    X, Y = models.gp_puzzle_nub()
    xy = pl.array([X, Y])

    a = pl.array(a)
    b = pl.array(b)

    r = pl.norm(b-a)
    cosT, sinT = (b-a)/r
    R = pl.array([[cosT, -sinT],
                  [sinT,  cosT]])

    xy = a + r*pl.dot(R, xy).T
    X = xy[:, 0]
    Y = xy[:, 1]

    pl.plot(X, Y)

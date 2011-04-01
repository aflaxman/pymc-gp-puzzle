import networkx as nx
import pylab as pl
import random

import models
import data
reload(data)

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

    pl.plot(X, Y, color='black')

def plot_line(a, b):
    X = [a[0], b[0]]
    Y = [a[1], b[1]]

    pl.plot(X, Y, color='black')


def plot_puzzle_graph(G, pos):
    for u, v in G.edges_iter():
        # if u and v are on the edge of graph, connect with a straight line
        if len(G[u]) < 4 and len(G[v]) < 4:
            plot_line(pos[u], pos[v])
        else:
            if random.random() > .5:
                plot_nub(pos[u], pos[v])
            else:
                plot_nub(pos[v], pos[u])

def plot_grid_puzzle(shape):
    """ Generate a jigsaw puzzle on a square grid with dimensions
    given by shape"""

    G = data.my_grid_graph(shape)

    pl.figure(figsize=shape)
    pl.axes([0,0,1,1], frameon=True)
    plot_puzzle_graph(G, G.pos)
    pl.axis([-.1, shape[0]-.9, -.1, shape[1]-.9])

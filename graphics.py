import networkx as nx
import pylab as pl
import random

import models
import data
reload(data)

# put messy matplotlib code here so I don't have to look at it if I
# don't want to

def plot_nub(a, b):
    """ Plot a puzzle nub from a to b"""
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
    """ Plot a straight line from a to b"""
    X = [a[0], b[0]]
    Y = [a[1], b[1]]

    pl.plot(X, Y, color='black')


def plot_puzzle_graph(G, pos):
    """ Turn graph into puzzle, by making a line for each edge
    
    if the edge has an attribute for 'invisible_line' set to True skip
    it and if the edge has an attrible for 'straight_line' set to
    True, don't make a nub
    """
    # add matching on odd degree nodes
    odd_nodes = [v for v in G if len(G[v])%2 == 1]
    for u,v in zip(odd_nodes[::2], odd_nodes[1::2]):
        G.add_edge(u, v, invisible_line=True)

    for u, v in nx.eulerian_circuit(G):
        if G[u][v].get('invisible_line'):
            continue

        if G[u][v].get('straight_line'):
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

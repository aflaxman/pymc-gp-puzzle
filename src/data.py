""" Class for wrangling data
"""

import pylab as pl
import pymc as mc
import networkx as nx

# puzzle nub coordinates
puzzle_t = pl.array([0., .25, .375, .5, .625, .75, 1.])
puzzle_x = .25 + .5*pl.array([-.5, .375, .125, .5, .875, .625, 1.5])
puzzle_y = .5*pl.array([0., 0., .35, .7, .35, 0., 0.])
puzzle_V = pl.array([1.e-6, .0005, .0005, .01, .0005, .0005, 1.e-6])


def my_grid_graph(shape):
    """ Create an nxn grid graph, with uniformly random edge weights,
    and a position dict G.pos
    """
    G = nx.grid_graph(list(shape))
    G.shape = shape
    
    for u, v in G.edges_iter():
        if len(G[u]) < 4 and len(G[v]) < 4:
            G[u][v]['straight_line'] = True

    G.pos = {}
    for v in G:
        G.pos[v] = [v[0], v[1]]

    return G

def load_svg(fname):
    from xml.dom import minidom
    dom = minidom.parse(fname)

    for path in dom.getElementsByTagName('path'):
        assert 0, 'TODO: parse svg info well enough to form a graph (seems more complicated than I expected)'

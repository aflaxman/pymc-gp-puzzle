""" Tests """

# matplotlib will open windows during testing unless you do the following
import matplotlib
matplotlib.use("AGG") 

import data
import models
import graphics

class TestClass:
    def setUp(self):
        pass

    def test_models(self):
        X, Y = models.gp_puzzle_nub()
        assert -.01 <= X[0] <= .01
        assert -.01 <= Y[0] <= .01

    def test_graphics(self):
        graphics.plot_nub([0,0], [1,0])

        G = data.my_grid_graph([3, 3])
        graphics.plot_puzzle_graph(G, G.pos)

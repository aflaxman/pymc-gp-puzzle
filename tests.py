""" Tests """

# matplotlib will open windows during testing unless you do the following
import matplotlib
matplotlib.use("AGG") 

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

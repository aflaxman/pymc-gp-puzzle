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

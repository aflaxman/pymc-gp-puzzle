""" Module for setting up statistical models
"""

import pylab as pl
import pymc as mc
from pymc import gp

import data
reload(data)

def gp_puzzle_nub(diff_degree=2., amp=1., scale=1.5, steps=100):
    """ Generate a puzzle nub connecting point a to point b"""

    M, C = uninformative_prior_gp(0., diff_degree, amp, scale)
    gp.observe(M, C, data.puzzle_t, data.puzzle_x, data.puzzle_V)
    GPx = gp.GPSubmodel('GP', M, C, pl.arange(1))
    X = GPx.value.f(pl.arange(0., 1.0001, 1. / steps))

    M, C = uninformative_prior_gp(0., diff_degree, amp, scale)
    gp.observe(M, C, data.puzzle_t, data.puzzle_y, data.puzzle_V)
    GPy = gp.GPSubmodel('GP', M, C, pl.arange(1))
    Y = GPy.value.f(pl.arange(0., 1.0001, 1. / steps))
    
    return X, Y
    
def const_func(x, c):
    """ A constant function, f(x) = c

    To be used as a non-informative prior on a Gaussian process.

    Example
    -------
    >>> const_func([1,2,3], 17.0)
    array([ 17., 17., 17.])
    """
    return pl.zeros(pl.shape(x)) + c

def uninformative_prior_gp(c=0.,  diff_degree=2., amp=1., scale=1.5):
    """ Uninformative Mean and Covariance Priors
    Parameters
    ----------
    c : float, the prior mean
    diff_degree : float, the prior on differentiability (2 = twice differentiable?)
    amp : float, the prior on the amplitude of the Gaussian Process
    scale : float, the prior on the scale of the Gaussian Process

    Results
    -------
    M, C : mean and covariance objects
      this constitutes an uninformative prior on a Gaussian Process
      with a euclidean Matern covariance function
    """
    M = gp.Mean(const_func, c=c)
    C = gp.Covariance(gp.matern.euclidean, diff_degree=diff_degree,
                      amp=amp, scale=scale)

    return M,C

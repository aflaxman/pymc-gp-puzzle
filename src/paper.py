""" Script for generating graphics for paper"""

import pylab as pl

import data
import models
import graphics
reload(graphics)

def figure1():
    pl.figure(1, figsize=(6, 2))
    pl.subplots_adjust(bottom=.25, top=.9, left=.1, right=.95, wspace=.5)
    pl.clf()

    steps = 100
    X, Y = models.gp_puzzle_nub(steps=steps)
    T = pl.arange(0., 1.0001, 1. / steps)

    pl.subplot(1,3,1)
    pl.text(-.35, 1, 'a)', va='bottom', ha='right')
    pl.errorbar(data.puzzle_t, data.puzzle_x, pl.sqrt(data.puzzle_V)*1.96,
                marker='o', color='black', linestyle='dotted')
    graphics.my_plot(T, X, color='red', alpha=.5, linewidth=2)
    pl.axis([-.1, 1.1, -.1, 1.1])
    pl.xticks([0,1])
    pl.yticks([0,1])
    pl.xlabel('$t$')
    pl.ylabel('$x(t)$')

    pl.subplot(1,3,2)
    pl.text(-.35, 1, 'b)', va='bottom', ha='right')
    pl.errorbar(data.puzzle_t, data.puzzle_y, pl.sqrt(data.puzzle_V)*1.96,
                marker='o', color='black', linestyle='dotted')
    graphics.my_plot(T, Y, color='red', alpha=.5, linewidth=2)
    pl.axis([-.1, 1.1, -.1, 1.1])
    pl.xticks([0,1])
    pl.yticks([0,1])
    pl.xlabel('$t$')
    pl.ylabel('$y(t)$')

    pl.subplot(1,3,3)
    pl.text(-.35, 1, 'c)', va='bottom', ha='right')
    pl.plot(data.puzzle_x, data.puzzle_y,
            marker='o', color='black', linestyle='dotted')
    graphics.my_plot(X, Y, color='red', alpha=.5, linewidth=2)
    pl.axis([-.1, 1.1, -.1, 1.1])
    pl.xticks([0,1])
    pl.yticks([0,1])
    pl.xlabel('$x(t)$')
    pl.ylabel('$y(t)$')

    pl.savefig('../tex/fig1.pdf')
    pl.savefig('../fig1.png')


def figure2():
    pl.figure(2, figsize=(11,3))
    pl.clf()
    graphics.plot_grid_puzzle([12, 4], linewidth=2)
    pl.axis('off')
    pl.xticks([])
    pl.yticks([])
    pl.savefig('../tex/fig2.pdf')
    pl.savefig('../fig2.png')

def figure3():
    pl.figure(3, figsize=(10,6))
    pl.clf()
    G = data.my_grid_graph([2,2])
    for u,v in G.edges():
        G[u][v]['straight_line'] = False

    param = ['\sigma', '\\rho', '\\nu']
    val = [[.25, 1., 2., 4., 8.],
           [3., 1.5, 1., .75, .5],
           [4., 2., 1.5, 1., .75]]

    for i in range(3):
        for j in range(5):
            params = {}
            if i == 0: params['amp'] = val[i][j]
            if i == 1: params['scale'] = val[i][j]
            if i == 2: params['diff_degree'] = val[i][j]

            if j >= 3: params['steps'] = 350  # more detail for the really weird ones

            pl.subplot(3, 5, i*5 + j + 1)
            graphics.plot_puzzle_graph(G, G.pos, **params)
            pl.axis([-.6, 1.6, -.6, 1.6])
            pl.axis('off')
            pl.text(-.5, 1.5, '$%s = %.2f$' % (param[i], val[i][j]))

    pl.savefig('../tex/fig3.pdf')
    pl.savefig('../fig3.png')


if __name__ == '__main__':
    figure1()
    figure2()
    figure3()

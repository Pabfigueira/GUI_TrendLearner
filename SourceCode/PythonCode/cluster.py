# -*- coding: utf8

from __future__ import division, print_function

from pyksc import dist
from pyksc import ksc

from matplotlib import pyplot as plt
from matplotlib import rc

import ioutil
import numpy as np
import os
import plac

def initialize_matplotlib():
    rc('axes', labelsize=20)
    rc('axes', unicode_minus=False)
    rc('axes', grid=True)
    rc('grid', color='lightgrey')
    rc('grid', linestyle=':')
    rc('font', family='serif')
    rc('legend', fontsize=18)
    rc('lines', linewidth=2)
    rc('ps', usedistiller='xpdf')
    rc('text', usetex=True)
    rc('xtick', labelsize=20)
    rc('ytick', labelsize=20)


def clusterKSC(tseries_fpath, base_folder, k):

    initialize_matplotlib()

    k = int(k)
    
    idx_fpath = os.path.join(base_folder,'train.dat')
    X = ioutil.load_series(tseries_fpath, idx_fpath)

    cent, assign, shift, dists_cent = ksc.inc_ksc(X, k)

    base_folder = os.path.join(os.path.join(base_folder,'..'),"Clustering_KSC")

    os.makedirs(base_folder)


    ## Parte vinda do PlotCentroids
    for i in xrange(cent.shape[0]):
        t_series = cent[i]
        
        plt.plot(t_series, '-k')
        plt.gca().get_xaxis().set_visible(False)
        plt.gca().get_yaxis().set_visible(False)
        #plt.ylabel('Views')
        #plt.xlabel('Time')
        plt.savefig(os.path.join(base_folder, '%d.pdf' % i))
        plt.close()
        
        half = t_series.shape[0] // 2
        to_shift = half - np.argmax(t_series)
        to_plot_peak_center = dist.shift(t_series, to_shift, rolling=True)
        plt.plot(to_plot_peak_center, '-k')
        plt.gca().get_xaxis().set_visible(False)
        plt.gca().get_yaxis().set_visible(False)
        #plt.ylabel('Views')
        #plt.xlabel('Time')
        plt.savefig(os.path.join(base_folder, '%d-peak-center.pdf' % i))
        plt.close()
        
        to_shift = 0 - np.argmin(t_series)
        to_plot_min_first = dist.shift(t_series, to_shift, rolling=True)
        plt.plot(to_plot_min_first, '-k')
        plt.gca().get_xaxis().set_visible(False)
        plt.gca().get_yaxis().set_visible(False)
        #plt.ylabel('Views')
        #plt.xlabel('Time')
        plt.savefig(os.path.join(base_folder, '%d-min-first.pdf' % i))
        plt.close()
    ## Fim da Parte vinda do PlotCentroids

    np.savetxt(os.path.join(base_folder, 'cents.dat'), cent, fmt='%.5f')
    np.savetxt(os.path.join(base_folder, 'assign.dat'), assign, fmt='%d')
    np.savetxt(os.path.join(base_folder, 'shift.dat'), shift, fmt='%d')
    np.savetxt(os.path.join(base_folder, 'dists_cent.dat'), dists_cent, 
               fmt='%.5f')
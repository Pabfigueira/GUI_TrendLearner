# -*- coding: utf8

from __future__ import division, print_function

from matplotlib import pyplot as plt
from matplotlib import rc

from pyksc import dist
from pyksc import metrics
from pyksc import ksc

from scipy.stats import t, norm

#from scripts import initialize_matplotlib

#from vod.stats.ci import half_confidence_interval_size as hci

import argparse
import numpy as np
import os
import sys
import traceback
import math

def t_table(freedom, confidence):
    """
    Looks up the t_table (i.e. calls the inverse CDF of the 
    t-student distribution).
    
    >>> t_table(1, 0.95)
    12.706204736432099
    >>> t_table(9, 0.90)
    1.8331129326536333
    >>> t_table(8, 0.99)
    3.3553873313333957
    >>> t_table(10, 0.85)
    1.5592359332425447
    """
    return t.ppf((1+confidence)/2.,freedom)

def z_table(confidence):
    """
    Looks up the z_table (i.e. calls the inverse CDF of the 
    normal distribution).
    
    >>> z_table(0.95)
    1.959963984540054
    >>> z_table(0.90)
    1.6448536269514722
    >>> z_table(0.99)
    2.5758293035489004
    >>> z_table(0.85)
    1.4395314709384561
    """
    return norm.ppf((1+confidence)/2.)

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

def half_confidence_interval_size(data, confidence, axis=None):
    """
    Determines the half of the confidence interval size
    for some data. The confidence interval is mean +- return values.
    
    >>> data = [8.0, 7.0, 5.0, 9.0, 9.5, 11.3, 5.2, 8.5]
    >>> confidence_interval(data, 0.95)
    1.6772263663789651
    """
    
    a = np.asanyarray(data)
    if axis is None:
        n = a.size
    else:
        n = a.shape[axis]
        
    std = np.std(a, axis=axis)
    
    # calls the inverse CDF of the Student's t
    # distribution
    if n <= 30:
        h = std * t_table(n-1, confidence) / math.sqrt(n)
    else:
        h = std * z_table(confidence) / math.sqrt(n)
    return h

def run_clustering(X, k, dists_all):

    cent, assign, shift, dists_cent = ksc.inc_ksc(X, k)

    intra = metrics.avg_intra_dist(X, assign, dists_all)[0]
    inter = metrics.avg_inter_dist(X, assign, dists_all)[0]
    bcv = metrics.beta_cv(X, assign, dists_all)
    cost = metrics.cost(X, assign, None, dists_cent)

    return intra, inter, bcv, cost
    
def main(tseries_fpath, plot_foldpath, maxValue):
    assert os.path.isdir(plot_foldpath)
    initialize_matplotlib()
    
    X = np.genfromtxt(tseries_fpath)[:,1:].copy()

    n_samples = X.shape[0]
    sample_rows = np.arange(n_samples)
    
    clust_range = range(2, maxValue + 1)
    n_clustering_vals = len(clust_range)
    
    intra_array = np.zeros(shape=(25, n_clustering_vals))
    inter_array = np.zeros(shape=(25, n_clustering_vals))
    bcvs_array = np.zeros(shape=(25, n_clustering_vals))
    costs_array = np.zeros(shape=(25, n_clustering_vals))
    
    r = 0
    for i in xrange(5):
        np.random.shuffle(sample_rows)
        rand_sample = sample_rows[:200]
        
        X_new = X[rand_sample]
        D_new = dist.dist_all(X_new, X_new, rolling=True)[0]
        
        for j in xrange(5):
            for k in clust_range:
                intra, inter, bcv, cost = run_clustering(X_new, k, D_new)
                
                intra_array[r, k - 2] = intra
                inter_array[r, k - 2] = inter
                bcvs_array[r, k - 2]  = bcv
                costs_array[r, k - 2] = cost
                
            r += 1
            print(r)

    intra_err = np.zeros(n_clustering_vals)
    inter_err = np.zeros(n_clustering_vals)
    bcvs_err = np.zeros(n_clustering_vals)
    costs_err = np.zeros(n_clustering_vals)

    for k in clust_range:
        j = k - 2
        intra_err[j] = half_confidence_interval_size(intra_array[:,j], .95)
        inter_err[j] = half_confidence_interval_size(inter_array[:,j], .95)
        bcvs_err[j] = half_confidence_interval_size(bcvs_array[:,j], .95)
        costs_err[j] = half_confidence_interval_size(costs_array[:,j], .95)
            
    plt.errorbar(clust_range, np.mean(inter_array, axis=0), fmt='gD', 
                 label='Inter Cluster', yerr=inter_err)
    plt.errorbar(clust_range, np.mean(bcvs_array, axis=0), fmt='bo', 
                 label='BetaCV', yerr=bcvs_err)
    plt.errorbar(clust_range, np.mean(intra_array, axis=0), fmt='rs', 
                 label='Intra Cluster', yerr=intra_err)
    plt.ylabel('Average Distance')
    plt.xlabel('Number of clusters')
    plt.xlim((0., maxValue+1))
    plt.ylim((0., 1.))
    plt.legend(frameon=False, loc='lower left')
    plt.savefig(os.path.join(plot_foldpath, 'bcv.pdf'))
    plt.close()
    
    plt.errorbar(clust_range, np.mean(costs_array, axis=0), fmt='bo', 
                 label='Cost', yerr=costs_err)
    plt.ylabel('Cost (F)')
    plt.xlabel('Number of clusters')
    plt.xlim((0., maxValue+1))
    plt.ylim((0., 1.))
    plt.legend(frameon=False, loc='lower left')
    plt.savefig(os.path.join(plot_foldpath, 'cost.pdf'))
    plt.close()

def create_parser(prog_name):
    
    desc = __doc__
    formatter = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog_name, description=desc,
                                     formatter_class=formatter)
    
    parser.add_argument('tseries_fpath', type=str, help='Time series file')
    parser.add_argument('plot_foldpath', type=str, help='Folder to store plots')
    return parser

def entry_point(args=None):
    '''Fake main used to create argparse and call real one'''
    
    if not args: 
        args = []

    parser = create_parser(args[0])
    values = parser.parse_args(args[1:])
    
    try:
        return main(values.tseries_fpath, values.plot_foldpath)
    except:
        traceback.print_exc()
        parser.print_usage(file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(entry_point(sys.argv))

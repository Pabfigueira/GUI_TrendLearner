#!/usr/bin/env python

from pyksc import dist

import ioutil
import numpy as np
import plac
import sys

def create_test_assignMethod(tseries_fpath, test_fpath, cents_fpath, file_fpath):

    X = ioutil.load_series(tseries_fpath, test_fpath)

    C = np.loadtxt(cents_fpath)
    dist_cents = dist.dist_all(C, X, rolling=True)[0]
    y_true = dist_cents.argmin(axis=0)

    fout = open(file_fpath, "w")

    for t in y_true:
        print >> fout, t


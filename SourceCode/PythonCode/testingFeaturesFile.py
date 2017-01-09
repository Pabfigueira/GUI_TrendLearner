# -*- coding: utf8

from __future__ import division, print_function

from sklearn.base import clone
from sklearn.metrics import classification_report

from learn_base import create_grid_search
from learn_base import load_categories

import boosting
import cotrain
import stacking
import numpy as np
import os
import plac
import sys


def testTwo(features_folder, best_by, gamma_max):
	
	try:
		F = []
		matrices = {}
		feats_fname = 'year#%d.txt'

		for i  in xrange(best_by.shape[0]):
			bby = best_by[i]

			if bby == np.inf:
				feats_file = os.path.join(features_folder, feats_fname % gamma_max)
			else:
				bby = int(bby)
				feats_file = os.path.join(features_folder, feats_fname % bby)

			if bby in matrices:
				Fi = matrices[bby]
			else:
				Fi = np.genfromtxt(feats_file)[:,1:]
				matrices[bby] = Fi

			feats = Fi[i]

			F.append(feats)

		referrers = np.asanyarray(F)
	except:
		return False
	return True


def testOne(features_folder, fold_folder, results_name, gamma_max):

	try:
		#File paths
		best_by_test_fpath = os.path.join(fold_folder, results_name,
				'best-by.dat')
		best_by_train_fpath = os.path.join(fold_folder, results_name + '-train',
				'best-by.dat')
		
		
		test_fpath = os.path.join(fold_folder, '..', '..', '..', 'Data', 'test.dat')
		train_fpath = os.path.join(fold_folder, '..', '..', '..', 'Data', 'train.dat')

		#Loading Matrices
		best_by_test = np.genfromtxt(best_by_test_fpath)
		best_by_train = np.genfromtxt(best_by_train_fpath)
		
		test = np.loadtxt(test_fpath, dtype='bool')
		train = np.loadtxt(train_fpath, dtype='bool')

		assert np.logical_xor(train, test).all()
		assert best_by_train.shape == train.sum()
		assert best_by_test.shape == test.sum()

		best_by = np.zeros(best_by_test.shape[0] + best_by_train.shape[0])
		best_by[test] = best_by_test
		best_by[train] = best_by_train

		
		if testTwo(features_folder, best_by, gamma_max):
			return True
		else:
			return False
	except:
		return False

	return True
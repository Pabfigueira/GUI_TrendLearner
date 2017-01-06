#!/usr/bin/env python
# -*- coding: utf8
from __future__ import print_function, division

from sklearn import model_selection

import numpy as np
import os
import plac
import sys
from shutil import copyfile
from math import isnan

EPS = 1e-6

def tryload_series(tseries_fpath):
	try: 
		X = np.genfromtxt(tseries_fpath)[:,0:] + EPS
		matrix = np.asanyarray(X)
		if(len(matrix) < 2):
			return False
		for vector in matrix:
			for value in vector:
				if isnan(value) or value < (0 + EPS):
					return False
		return True
	except:
		return False

def generateCrossValsSequential(tseries_fpath, out_folder, tax):
	X = np.genfromtxt(tseries_fpath)[:,0:]
	num_series = X.shape[0]
	
	to_save_train = np.zeros(len(X), dtype='b')
	to_save_test = np.zeros(len(X), dtype='b')

	curr_out_folder = os.path.join(out_folder, 'Data')
		
	try:
		os.makedirs(curr_out_folder)
		copyfile(tseries_fpath, curr_out_folder + "/Input.txt")
	except:
		pass

	to_save_train[:] = False
	to_save_test[:] = False

	for atual in range(0,len(X)):
		if atual < int(len(X)*tax):
			to_save_train[atual] = True
		else:
			to_save_test[atual] = True

	np.savetxt(os.path.join(curr_out_folder, 'train.dat'), to_save_train, fmt='%i')
	np.savetxt(os.path.join(curr_out_folder, 'test.dat'), to_save_test, fmt='%i')




def generateCrossValsRandom(tseries_fpath, out_folder):
	X = np.genfromtxt(tseries_fpath)[:,0:]
	num_series = X.shape[0]
	
	cv = model_selection.KFold(2, shuffle=True)
	to_save_train = np.zeros(len(X), dtype='b')
	to_save_test = np.zeros(len(X), dtype='b')

	for train, test in cv.split(X):
		curr_out_folder = os.path.join(out_folder, 'Data')
		
		try:
			os.makedirs(curr_out_folder)
			copyfile(tseries_fpath, curr_out_folder + "/Input.txt")
		except:
			pass
		
		to_save_train[:] = False
		to_save_test[:] = False
		to_save_train[train] = True
		to_save_test[test] = True

		np.savetxt(os.path.join(curr_out_folder, 'train.dat'), to_save_train, fmt='%i')
		np.savetxt(os.path.join(curr_out_folder, 'test.dat'), to_save_test, fmt='%i')

#!/usr/bin/python
#--------------------------------------------------------------------------#
# DILATION.PY                                                              #
#                                                                          #
# Functions for performing unitary dilation                                #
#                                                                          #
# Dependencies:                                                            #
#  * numpy                                                                 #
#  * cmath                                                                 #
#  * scipy.linalg                                                          #
#                                                                          #
#--------------------------------------------------------------------------#

import numpy
import cmath

from scipy import linalg

def defect(M):
  '''Matrix defect, defined by (I-MM*)^{1/2}, where M* is the conjugate
transpose of matrix M
M      : (numpy array) complex matrix
return : (numpy array) matrix defect of M'''
  size = len(M)
  I = numpy.matrix(numpy.identity(size, dtype=complex))
  D2 = I-M*M.getH()
  evals, evecs = linalg.eig(D2)
  diag = numpy.matrix(numpy.identity(size, dtype=complex))
  U = numpy.matrix(evecs)
  for i in range(size):
    diag[i,i] = cmath.sqrt(evals[i])
  D = U*diag*U.getH()
  return D

def dilate(M):
  '''Unitary dilation of dxd matrix M. The return matrix will have
dimension 2d and will be unitary as long as the operator norm of
M is <=1.
M      : (numpy array) complex matrix
return : (numpy array) unitary dilation of M'''
  size = len(M)
  D = defect(M)
  Ddag = defect(M.getH())
  V = numpy.matrix(numpy.identity(2*size, dtype=complex))
  V[0:size,0:size] = M.copy()            # Top left
  V[size:2*size,0:size] = Ddag.copy()    # Bottom left
  V[0:size,size:2*size] = D.copy()       # Top right
  V[size:2*size,size:2*size] = -M.getH() # Bottom right
  return V

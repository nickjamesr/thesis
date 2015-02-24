#!/usr/bin/python
#--------------------------------------------------------------------------#
# PTTOOLS.PY                                                               #
# Functions required for the analysis of PT-symmetric matrices             #
#                                                                          #
# Dependencies                                                             #
#  * numpy                                                                 #
#  * scipy.linalg                                                          #
#  * dilation.dilate                                                       #
#                                                                          #
#--------------------------------------------------------------------------#

import numpy

from scipy import linalg
from dilation import dilate

def abs2(z):
  '''Absolute square of an object
z      : input object. Must have __abs__ defined
return : |z|^{2}'''
  return abs(z)**2

def ptmatrix(gamma, J, t, verbose=False):
  '''Generate the matrix corresponding to a PT symmetric Hamiltonian 
with parameters gamma and J, evolved to a time t.
The form of the (non-Hermitian) Hamiltonian is:
  H = -J \sigma_x - i \gamma -sigma_z
gamma   : on-site potential
J       : cross-site tunneling
t       : evolution time
verbose : print verbose output to stdout
return  : (numpy array) time-evolution operator (not necessarily
          unitary'''
  G = numpy.empty((2,2),dtype=complex)
  if gamma<J:
    if verbose:
      print "PT-symmetric\n"
    eps = numpy.sqrt(J**2-gamma**2)
    alpha = eps*t
    G[0,0] = numpy.cos(alpha)-gamma*numpy.sin(alpha)/eps
    G[0,1] = complex(0,J*numpy.sin(alpha)/eps)
    G[1,0] = complex(0,J*numpy.sin(alpha)/eps)
    G[1,1] = numpy.cos(alpha)+gamma*numpy.sin(alpha)/eps
  elif gamma>J:
    if verbose:
      print "non-PT-symmetric\n"
    eps = numpy.sqrt(gamma**2-J**2)
    beta = eps*t
    G[0,0] = numpy.cosh(beta)-gamma*numpy.sinh(beta)/eps
    G[0,1] = complex(0,J*numpy.sinh(beta)/eps)
    G[1,0] = complex(0,J*numpy.sinh(beta)/eps)
    G[1,1] = numpy.cosh(beta)+gamma*numpy.sinh(beta)/eps
  else:
    if verbose:
      print "PT-phase boundary\n"
    G[0,0] = 1-J*t
    G[0,1] = complex(0,J*t)
    G[1,0] = complex(0,J*t)
    G[1,1] = 1+J*t

  evals,evecs = linalg.eig(numpy.dot(G,numpy.conjugate(numpy.transpose(G))))
  normG = numpy.sqrt(max(abs(evals)))
  G /= normG
  U = dilate(numpy.matrix(G))
  return U, normG

def singles(u, col=0):
  '''Count rates for single photons injected into a 4x4 unitary matrix
u      : unitary matrix
col    : input mode
return : count rates at outputs a,b,c,d
'''
  a=abs2(u[0,col])
  b=abs2(u[1,col])
  c=abs2(u[2,col])
  d=abs2(u[3,col])
  return (a,b,c,d)

def pairs(u, cols=(0,1)):
  '''Count rates for photon pairs injected into a 4x4 unitary matrix
u      : unitary matrix
cols   : input modes
return : count rates in output pairs ab,ac,ad,bc,bd,cd'''
  rows=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
  k,l=cols
  rtn=[abs2(u[i,k]*u[j,l]+u[j,k]*u[i,l]) for i,j in rows]
  return tuple(rtn)

def cpairs(u, cols=(0,1)):
  '''Count rates for pairs of classical particles injected into a 4x4
unitary matrix
u      : unitary matrix
cols   : input modes
return : count rates in output pairs ab,ac,ad,bc,bd,cd'''
  rows=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
  k,l=cols
  rtn=[abs2(u[i,k]*u[j,l])+abs2(u[j,k]*u[i,l]) for i,j in rows]
  return tuple(rtn)

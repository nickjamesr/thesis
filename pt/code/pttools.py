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

def threesitematrix(gamma, eta, t, verbose=False, tol=1e-12):
  '''Generate the matrix corresponding to a 3-site PT symmetric
Hamiltonian with parameters gamma and eta, evolved to time t.
The form of the (non-Hermitian) Hamiltonian is:
    / i*gamma -eta     0   \
H = |  -eta     0    -eta   |
    \    0    -eta -i*gamma /
gamma   : (imaginary) on-site potential
eta     : coupling between adjacent sites
t       : evolution time
verbose : (optional) print verbose output to stdout
return  : (numpy array) time-evolution operator (not unitary)'''
  gamma=float(gamma)
  eta=float(eta)
  t=float(t)
  H=numpy.array([[1j*gamma, -eta, 0], [-eta, 0, -eta], [0, -eta, -1j*gamma]],\
dtype=complex)
  if abs(2*eta**2-gamma**2)<tol:
    # critical case
    raise Exception('Critical case', 'Singular matrix')
  elif 2*eta**2>gamma**2:
    # symmetric case
    if verbose:
      print "Symmetric case"
    evals=numpy.array([0,numpy.sqrt(2*eta**2-gamma**2),\
-numpy.sqrt(2*eta**2-gamma**2)], dtype=complex)
    vzero=1/numpy.sqrt(gamma**2+2*eta**2)*numpy.array([eta,gamma*1j,-eta],\
dtype=complex)
    vplus=1/(2*numpy.sqrt(2)*eta)*numpy.array([-1j*gamma-numpy.sqrt(2*eta**2-\
gamma**2), 2*eta, 1j*eta-numpy.sqrt(2*eta**2-gamma**2)],dtype=complex)
    vminus=1/(2*numpy.sqrt(2)*eta)*numpy.array([-1j*gamma+numpy.sqrt(2*eta**2-\
gamma**2), 2*eta, 1j*gamma+numpy.sqrt(2*eta**2-gamma**2)],dtype=complex)
  elif 2*eta**2 < gamma**2:
    # broken case
    if verbose:
      print "Broken case"
    evals=numpy.array([0,1j*numpy.sqrt(gamma**2-2*eta**2),\
-1j*numpy.sqrt(gamma*2-2*eta**2)], dtype=complex)
    vzero=1/numpy.sqrt(gamma**2+2*eta**2)*numpy.array([eta,gamma*1j,-eta],\
dtype=complex)
    vplus=1/(2*gamma)*numpy.array([1j*(-gamma - numpy.sqrt(gamma**2-2*eta**2)),\
2*eta, 1j*(gamma - numpy.sqrt(gamma**2 - 2*eta**2))], dtype=complex)
    vminus=1/(2*gamma)*numpy.array([1j*(-gamma + numpy.sqrt(gamma**2 -\
2*eta**2)), 2*eta, 1j*(gamma + numpy.sqrt(gamma**2 - 2*eta**2))], dtype=complex)

  # Now calculate the exponential

  V=numpy.array([[vzero[0],vplus[0],vminus[0]],\
                 [vzero[1],vplus[1],vminus[1]],\
                 [vzero[2],vplus[2],vminus[2]]],dtype=complex)
  D=numpy.array([[numpy.exp(-1j*evals[0]*t),0,0],
                 [0,numpy.exp(-1j*evals[1]*t),0],
                 [0,0,numpy.exp(-1j*evals[2]*t)]],dtype=complex)
  G=numpy.dot(V, numpy.dot(D, numpy.linalg.inv(V)))

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

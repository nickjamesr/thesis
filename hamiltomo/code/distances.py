#!/usr/bin/python

#----------------------------------------------------------------------------#
# DISTANCES.PY                                                               #
#                                                                            #
# Distance measures to compare fidelities between matrices                   #
#  * trace distance (Hermitian matrices)                                     #
#  * unitary fidelity                                                        #
#  * trace distance (general matrices)                                       #
#                                                                            #
# Dependencies:                                                              #
#  * hamiltomo.py                                                            #
#  * numpy                                                                   #
#  * scipy.linalg                                                            #
#                                                                            #
#----------------------------------------------------------------------------#

import hamiltomo
import numpy

from scipy import linalg

def TraceDistance(A,B):
  '''Trace distance between two matrices, defined as
0.5*Tr(sqrt((A-B)(A-B)^))
A      : reference matrix
B      : test matrix
return : (float) trace distance between A and B'''
  dim=A.shape[0]                          # assume square and same shape
  ab=numpy.dot(A-B,hamiltomo.dagger(A-B)) # always hermitian
  evals,evecs=linalg.eigh(ab)
  diag=hamiltomo.Identity(dim)
  for i in range(dim):
    diag[i,i]=numpy.sqrt(evals[i])
  root=numpy.dot(evecs,numpy.dot(diag,hamiltomo.dagger(evecs)))
  return 0.5*sum(root.flatten()[::dim+1])

def HermitianDistance(H,G):
  '''Distance measure between two Hermitian matrices
Uses a trace distance 0.5*Tr(sqrt((H-G)(H-G)^))
H      : reference matrix (assume Hermitian)
G      : test matrix (take the Hermitian part of this)
return : (float) trace distance between H and G'''
  Gh=0.5*(H+hamiltomo.dagger(H)) # Hermitian part of G
  d=H-G                          # Hermitian
  evals=linalg.eigvalsh(d)
  return 0.5*sum(abs(evals))

def UnitaryFidelity(U,V):
  '''Distance measure between two unitary matrices.
Uses a trace distance (1/N) Tr(U^V)
U      : reference matrix (always unitary)
V      : test matrix (not necessarily unitary)
return : (float) trace distance between U and V'''
  dim=U.shape[0]
  uv=numpy.dot(U, hamiltomo.dagger(V))
  return hamiltomo.abs2((1./dim)*sum(uv.flatten()[0::dim+1]))


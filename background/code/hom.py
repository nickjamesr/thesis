#!/usr/bin/python

import numpy

from scipy import linalg

def abs2(z):
  '''Absolute square of any object with __abs__ defined'''
  return abs(z)**2

def expi(H,t=1):
  '''Return the matrix exponential e^{-iHt} for a matrix H and a (real) time
parameter t'''
  if H.ndim != 2:
    raise ShapeError("Matrix must be 2 dimensional for exponential")
  m,n = H.shape
  if m != n:
    raise ShapeError("Matrix must be square for exponential")
  evals,evecs=linalg.eig(H)
  diag = numpy.zeros(H.shape, dtype=complex)
  for i in range(n):
    diag[i,i] = numpy.exp(-complex(0,1)*evals[i]*t)
  return numpy.dot(numpy.dot(evecs, diag), linalg.inv(evecs))

def quantumwalk(nmodes, t, potential=2, coupling=0.5):
  H=numpy.zeros((nmodes,nmodes),dtype=complex)
  for i in range(nmodes):
    H[i,i]=potential
  for i in range(nmodes-1):
    H[i,i+1]=coupling
    H[i+1,i]=complex(coupling).conjugate()
  return expi(H,t)

def bosons(U):
  M=numpy.zeros_like(U,dtype=float)
  return M

def fermions(U):
  M=numpy.zeros_like(U,dtype=float)
  return M

def classical(U):
  M=numpy.zeros_like(U,dtype=float)
  return M

if __name__=='__main__':
  U=quantumwalk(7,3)
  numpy.savetxt("singles.dat",abs2(U[:,3]))
  numpy.savetxt("bosons.dat",bosons(U))
  numpy.savetxt("fermions.dat",fermions(U))
  numpy.savetxt("classical.dat",classical(U))

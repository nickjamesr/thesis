#!/usr/bin/python

import numpy

from matplotlib import pyplot
from sys import argv

def expi(phi):
  return numpy.exp(1j*phi)

def root(r):
  return numpy.sqrt(r)

def toor(r):
  return numpy.sqrt(1-r)

def unitary_from_reck(r, phi):
  R0 = numpy.array(
[
  [
    +expi(phi[2,0])*root(r[2,1]),
    +expi(phi[2,0])*toor(r[2,1]),
    0
  ],
  [
    +expi(phi[2,1])*toor(r[2,1])*root(r[2,2]),
    -expi(phi[2,1])*root(r[2,1])*root(r[2,2]),
    +expi(phi[2,1])*toor(r[2,2])
  ],
  [
    +expi(phi[2,2])*toor(r[2,1])*toor(r[2,2]),
    -expi(phi[2,2])*root(r[2,1])*toor(r[2,2]),
    -expi(phi[2,2])*root(r[2,2])
  ]
])
  R1 = numpy.array(
[
  [
    1,
    0,
    0
  ],
  [
    0,
    +expi(phi[1,0])*root(r[1,1]),
    +expi(phi[1,0])*toor(r[1,1])
  ],
  [
    0,
    +expi(phi[1,1])*toor(r[1,1]),
    -expi(phi[1,1])*root(r[1,1])
  ]
])
  return numpy.dot(R0, R1)

def trace(u):
  for i in range(3):
    return u[0,0]+u[1,1]+u[2,2]

def generate():
  r      = numpy.random.uniform(0, 1, (3,3))
  phi    = numpy.random.uniform(0, 2*numpy.pi, (3,3))
  r[2,1] = numpy.random.beta(1,2)
  return (r,phi)

def elements(x):
  return 4*x*(1-x**2)

if __name__=='__main__':
  nsamples=1000
  if len(argv)>1:
    numpy.random.seed(int(argv[1]))
  if len(argv)>2:
    nsamples=int(argv[2])

  nmetrics = 4
  register = numpy.empty((nmetrics,nsamples))

  for i in range(nsamples):
    u=unitary_from_reck(*generate())
    register[0,i] = abs(u[0,0])
    register[1,i] = abs(u[1,0])
    register[2,i] = abs(u[2,0])
    register[3,i] = abs(trace(u))**2

  nbins = 25
  print "0,0 element (mean {0:.4f})".format(numpy.mean(register[0]))
  count, bins, ignored = pyplot.hist(register[0], nbins, normed=True)
  pyplot.plot(bins, elements(bins), linewidth=2, color='r')
  pyplot.show()

  print "|trace|^2   (mean {0:.4f})".format(numpy.mean(register[3]))
  count, bins, ignored = pyplot.hist(register[3], nbins, normed=True)
  pyplot.show()

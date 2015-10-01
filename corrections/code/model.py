#!/usr/bin/python

import numpy
import cmath

from matplotlib import pyplot
from sys import argv,exit

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

  register = numpy.empty((9,nsamples))
  for i in range(nsamples):
    r,phi = generate()
    register[0,i] = r[2,1]
    register[1,i] = r[2,2]
    register[2,i] = root(r[2,1])
    register[3,i] = root(r[2,2])
    register[4,i] = toor(r[2,1])
    register[5,i] = toor(r[2,2])
    register[6,i] = root(r[2,1])
    register[7,i] = toor(r[2,1])*root(r[2,2])
    register[8,i] = toor(r[2,1])*toor(r[2,2])
  print "r(2,1) - linear"
  count, bins, ignored = pyplot.hist(register[0], 15, normed=True)
  pyplot.show()
  print "r(2,2) - uniform"
  count, bins, ignored = pyplot.hist(register[1], 15, normed=True)
  pyplot.show()
  print "root(r_21)"
  count, bins, ignored = pyplot.hist(register[2], 15, normed=True)
  pyplot.show()
  print "root(r_22)"
  count, bins, ignored = pyplot.hist(register[3], 15, normed=True)
  pyplot.show()
  print "root(1-r_21)"
  count, bins, ignored = pyplot.hist(register[4], 15, normed=True)
  pyplot.show()
  print "root(1-r_22)"
  count, bins, ignored = pyplot.hist(register[5], 15, normed=True)
  pyplot.show()
  print "|rho_0|"
  count, bins, ignored = pyplot.hist(register[6], 15, normed=True)
  pyplot.plot(bins, elements(bins))
  pyplot.show()
  print "|rho_1|"
  count, bins, ignored = pyplot.hist(register[7], 15, normed=True)
  pyplot.plot(bins, elements(bins))
  pyplot.show()
  print "|rho_2|"
  count, bins, ignored = pyplot.hist(register[8], 15, normed=True)
  pyplot.plot(bins, elements(bins))
  pyplot.show()

  exit(0)
  nmetrics = 18
  register = numpy.empty((nmetrics,nsamples))
    
  for i in range(nsample):
    u   = unitary_from_reck(*generate())
    r   = abs(u[0,0])
    phi = cmath.phase(u[0,0])
    n=0
    register[n,i] = r
    n+=1
    register[n,i] = r**2
    n+=1
    register[n,i] = r**3
    n+=1
    register[n,i] = r**4
    n+=1
    register[n,i] = r**5
    n+=1
    register[n,i] = r**6
    n+=1
    register[n,i] = phi
    n+=1
    register[n,i] = phi**2
    n+=1
    register[n,i] = phi**3
    n+=1
    register[n,i] = phi**4
    n+=1
    register[n,i] = phi**5
    n+=1
    register[n,i] = phi**6
    n+=1
    v = u.copy()
    register[n,i] = abs(trace(v))**2
    n+=1
    v = numpy.dot(u,v)
    register[n,i] = abs(trace(v))**2
    n+=1
    v = numpy.dot(u,v)
    register[n,i] = abs(trace(v))**2
    n+=1
    v = numpy.dot(u,v)
    register[n,i] = abs(trace(v))**2
    n+=1
    v = numpy.dot(u,v)
    register[n,i] = abs(trace(v))**2
    n+=1
    v = numpy.dot(u,v)
    register[n,i] = abs(trace(v))**2

  for i in range(nmetrics):
    print numpy.mean(register[i])

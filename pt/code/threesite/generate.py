#!/usr/bin/python
#--------------------------------------------------------------------------#
# GENERATE.PY                                                              #
#                                                                          #
# Functions to generate data for the three site model                      #
#                                                                          #
# Dependencies:                                                            #
#  * numpy                                                                 #
#  * pttools.threesite                                                     #
#                                                                          #
#--------------------------------------------------------------------------#

import sys
sys.path.append("code")
import numpy

from pttools import threesitematrix
from bintree import node, bintree

def abs2(z):
  return abs(z)*abs(z)

def trees(s,b):
  '''Generate the binary tree objects for the experimental points.
s      : (tmin,tmax) for symmetric tree
b      : (tmin,tmax) for broken tree
return : symmetric,broken'''
  symmetric=bintree(*s)
  symmetric.root.split()
  symmetric.root.left.split()
  symmetric.root.right.split()
  symmetric.root.left.left.split()
  symmetric.root.left.right.split()
  symmetric.root.right.left.split()
  symmetric.root.right.right.split()
  symmetric.root.left.left.left.split()
  symmetric.root.right.right.right.split()
  symmetric.root.right.right.right.right.split()

  broken=bintree(*b)
  broken.root.split()
  broken.root.left.split()
  broken.root.right.split()
  broken.root.left.left.split()
  broken.root.left.right.split()
  broken.root.left.left.left.split()
  broken.root.left.left.right.split()
  broken.root.left.left.left.left.split()
  broken.root.left.left.right.left.split()
  broken.root.left.left.right.left.left.split()
  broken.root.left.left.left.left.left.split()

  return symmetric,broken

def singles_incr(gamma,eta,tmin,tmax,tstep,fname,mode=0):
  '''Print the singles rates to a file for a range of times with constant
increment
gamma  : Magnitude of (complex) on-site potential
eta    : Magnitude of couplings
tmin   : Start time
tmax   : End time
tstep  : Increment between times
fname  : Path to output file
mode   : (optional) input mode
return : None'''
  t=tmin
  fmt="{0:.6f} {1:.6f} {2:.6f} {3:.6f} {4:.6f} {5:.6f} {6:.6f} {7:.6f}\n"
  with open(fname,'w') as fout:
    fout.write("# gamma {0:.4f}\n# eta   {1:.4f}\n\
# t norm 0 1 2 3 4 5\n".format(gamma,eta))
    while t<tmax:
      U,norm = threesitematrix(gamma,eta,t)
      powers=[abs2(U[i,mode]) for i in range(6)]
      fout.write(fmt.format(t,norm,*powers))
      t+=tstep

def pairs_incr(gamma,eta,tmin,tmax,tstep,fname,mode=(0,1)):
  '''Print the coincidence rates to a file for a range of times with constant
increment
gamma  : Magnitude of (complex) on-site potential
eta    : Magnitude of couplings
tmin   : Start time
tmax   : End time
tstep  : Increment between times
fname  : Path to output file
mode   : (optional) input modes
return : None'''
  pairs=[(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),\
(2,5),(3,4),(3,5),(4,5)]
  t=tmin
  fmt="{0:.6f} {1:.6f}"
  for i in range(len(pairs)):
    fmt+=" {"+str(i+2)+":.6f}"
  fmt+="\n"
  with open(fname, 'w') as fout:
    fout.write("# gamma {0:.4f}\n# eta   {1:.4f}\n# t norm 01 02 03 04 \
05 12 13 14 15 23 24 25 34 35 45\n".format(gamma,eta))
    while t<tmax:
      U,norm = threesitematrix(gamma,eta,t)
      #powers = [abs2(U[i,mode[0]]*U[j,mode[1]]+U[i,mode[1]]*U[j,mode[0]])\
      powers = [abs2(U[i,mode[0]]*U[j,mode[1]]+U[i,mode[1]]*U[j,mode[0]])\
for i,j in pairs]
      fout.write(fmt.format(t,norm,*powers))
      powers/=sum(powers) # Normalise visible coincidences to 1
      t+=tstep

def singles_exp(gamma,eta,tree,sym,mode=0):
  '''Print the singles rates to a file for the range of times that I
want in the experiment. Generate unitaries for experimental run
gamma  : Magnitude of (complex) on-site potential
eta    : Magnitude of couplings
tree   : Binary tree representing points
sym    : Symmetry of the matrix (symmetric | broken)
mode   : (optional) input mode
return : None'''
  fmt="{0:.6f} {1:.6f} {2:.6f} {3:.6f} {4:.6f} {5:.6f} {6:.6f} {7:.6f}\n"
  with open("data/threesite/"+sym+"/simulation/singles{0:d}.dat".format(mode),\
'w') as fout:
    fout.write("# gamma {0:.4f}\n# eta   {1:.4f}\n\
# t norm 0 1 2 3 4 5\n".format(gamma,eta))
    for n,t in enumerate(tree.points()):
      U,norm = threesitematrix(gamma,eta,t)
      powers=[abs2(U[i,mode]) for i in range(6)]
      fout.write(fmt.format(t,norm,*powers))
      with open("data/threesite/"+sym+"/unitaries/"+sym+str(n)+".csv", 'w') \
as matrix:
        matrix.write("# gamma {0:.4f}\n# eta   {1:.4f}\n\
# t     {2:.4f}\n# norm  {3:.4f}\n".format(gamma,eta,t,norm))
        for i in range(6):
          for j in range(5):
            z=U[i,j]
            matrix.write("({0:.6f},{1:.6f}),".format(z.real,z.imag))
          z=U[i,5]
          matrix.write("({0:.6f},{1:.6f})\n".format(z.real,z.imag))

def pairs_exp(gamma,eta,tree,sym,mode=(0,1)):
  '''Print the singles rates to a file for the range of times that I
want in the experiment.
gamma  : Magnitude of (complex) on-site potential
eta    : Magnitude of couplings
tree   : Binary tree representing points
sym    : Symmetry of the matrix (symmetric | broken)
mode   : (optional) input mode
return : None'''
  pairs=[(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),\
(2,5),(3,4),(3,5),(4,5)]
  fmt="{0:.6f} {1:.6f}"
  for i in range(len(pairs)):
    fmt+=" {"+str(i+2)+":.6f}"
  fmt+="\n"
  with open("data/threesite/"+sym+"/simulation/pairs{0:d}{1:d}.dat".format(\
mode[0],mode[1]), 'w') as fout:
    fout.write("# gamma {0:.4f}\n# eta   {1:.4f}\n# t norm 01 02 03 04 \
05 12 13 14 15 23 24 25 34 35 45\n".format(gamma,eta))
    for n,t in enumerate(tree.points()):
      U,norm = threesitematrix(gamma,eta,t)
      powers = [abs2(U[i,mode[0]]*U[j,mode[1]]+U[i,mode[1]]*U[j,mode[0]])\
for i,j in pairs]
      fout.write(fmt.format(t,norm,*powers))

if __name__=='__main__':

  period=5.135 # Empirical - period for symmetric case
  level=6.000  # Broken case levels off after approximately this time
  s=(0,period)
  b=(0,level)
  symmetric_tree,broken_tree=trees(s,b)

### SYMMETRIC ###
  eta=1
  gamma=0.5*numpy.sqrt(2)*eta
  tmin=s[0]
  tmax=s[1]

  # Theory (smooth curve)
  tstep=0.01
  singles_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/symmetric/theory/singles0.dat",mode=0)
  singles_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/symmetric/theory/singles1.dat",mode=1)
  singles_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/symmetric/theory/singles2.dat",mode=2)
  singles_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/symmetric/theory/singles3.dat",mode=3)
  singles_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/symmetric/theory/singles4.dat",mode=4)
  singles_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/symmetric/theory/singles5.dat",mode=5)

  pairs_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/symmetric/theory/pairs01.dat",mode=(0,1))
  pairs_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/symmetric/theory/pairs12.dat",mode=(1,2))
  pairs_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/symmetric/theory/pairs02.dat",mode=(0,2))

  # Simulation (sparse points)
  singles_exp(gamma,eta,symmetric_tree,"symmetric",\
mode=0)
  singles_exp(gamma,eta,symmetric_tree,"symmetric",\
mode=1)
  singles_exp(gamma,eta,symmetric_tree,"symmetric",\
mode=2)
  singles_exp(gamma,eta,symmetric_tree,"symmetric",\
mode=3)
  singles_exp(gamma,eta,symmetric_tree,"symmetric",\
mode=4)
  singles_exp(gamma,eta,symmetric_tree,"symmetric",\
mode=5)
  pairs_exp(gamma,eta,symmetric_tree,"symmetric",\
mode=(0,1))
  pairs_exp(gamma,eta,symmetric_tree,"symmetric",\
mode=(1,2))
  pairs_exp(gamma,eta,symmetric_tree,"symmetric",\
mode=(0,2))

### BROKEN ###
  eta=1
  gamma=1.05*numpy.sqrt(2)*eta
  tmin=b[0]
  tmax=b[1] # Levels off after approximately this time

  # Theory (smooth curve)
  tstep=0.01
  singles_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/broken/theory/singles0.dat",mode=0)
  singles_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/broken/theory/singles1.dat",mode=1)
  singles_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/broken/theory/singles2.dat",mode=2)
  singles_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/broken/theory/singles3.dat",mode=3)
  singles_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/broken/theory/singles4.dat",mode=4)
  singles_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/broken/theory/singles5.dat",mode=5)

  pairs_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/broken/theory/pairs01.dat",mode=(0,1))
  pairs_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/broken/theory/pairs12.dat",mode=(1,2))
  pairs_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/broken/theory/pairs02.dat",mode=(0,2))

  # Simulation (sparse points)
  singles_exp(gamma,eta,broken_tree,"broken",\
mode=0)
  singles_exp(gamma,eta,broken_tree,"broken",\
mode=1)
  singles_exp(gamma,eta,broken_tree,"broken",\
mode=2)
  singles_exp(gamma,eta,broken_tree,"broken",\
mode=3)
  singles_exp(gamma,eta,broken_tree,"broken",\
mode=4)
  singles_exp(gamma,eta,broken_tree,"broken",\
mode=5)
  pairs_exp(gamma,eta,broken_tree,"broken",\
mode=(0,1))
  pairs_exp(gamma,eta,broken_tree,"broken",\
mode=(1,2))
  pairs_exp(gamma,eta,broken_tree,"broken",\
mode=(0,2))



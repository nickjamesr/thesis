#!/usr/bin/python
#--------------------------------------------------------------------------#
# THREESITE.PY                                                             #
#                                                                          #
# Functions to deal with the 3 site model                                  #
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
    fout.write("# gamma {0:.4f}\n# eta   {1:.4f}\n# t norm 00 01 02 03 04 \
05 12 13 14 15 23 24 25 34 35 45\n".format(gamma,eta))
    while t<tmax:
      U,norm = threesitematrix(gamma,eta,t)
      powers = [abs2(U[i,mode[0]]*U[j,mode[1]]+U[i,mode[1]]*U[j,mode[0]])\
for i,j in pairs]
      fout.write(fmt.format(t,norm,*powers))
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
  with open("data/threesite/"+sym+"/simulation/singles.dat", 'w') as fout:
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

def pairs_exp(gamma,eta,tree,sym,mode=0):
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
  with open("data/threesite/"+sym+"/simulation/pairs.dat", 'w') as fout:
    fout.write("# gamma {0:.4f}\n# eta   {1:.4f}\n# t norm 00 01 02 03 04 \
05 12 13 14 15 23 24 25 34 35 45\n".format(gamma,eta))
    for n,t in enumerate(tree.points()):
      U,norm = threesitematrix(gamma,eta,t)
      powers = [abs2(U[i,mode[0]]*U[j,mode[1]]+U[i,mode[1]]*U[j,mode[0]])\
for i,j in pairs]
      fout.write(fmt.format(t,norm,*powers))

if __name__=='__main__':

### SYMMETRIC ###
  eta=1
  gamma=0.5*numpy.sqrt(2)*eta
  period=5.135 # Empirical
  tmin=0
  tmax=period

  # Theory (smooth curve)
  tstep=0.01
  singles_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/symmetric/theory/singles.dat",mode=0)
  pairs_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/symmetric/theory/pairs.dat",mode=(0,1))

  # Simulation (sparse points)
  tree=bintree(tmin,tmax)
  tree.root.split()
  tree.root.left.split()
  tree.root.right.split()
  tree.root.left.left.split()
  tree.root.left.right.split()
  tree.root.right.left.split()
  tree.root.right.right.split()
  tree.root.left.left.left.split()
  tree.root.right.right.right.split()
  tree.root.right.right.right.right.split()
  singles_exp(gamma,eta,tree,"symmetric",\
mode=0)
  pairs_exp(gamma,eta,tree,"symmetric",\
mode=(0,1))

### BROKEN ###
  eta=1
  gamma=1.05*numpy.sqrt(2)*eta
  tmin=0
  tmax=6 # Levels off after approximately this time

  # Theory (smooth curve)
  tstep=0.01
  singles_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/broken/theory/singles.dat",mode=0)
  pairs_incr(gamma,eta,tmin,tmax,tstep,\
"data/threesite/broken/theory/pairs.dat",mode=(0,1))

  # Simulation (sparse points)
  tree=bintree(tmin,tmax)
  tree.root.split()
  tree.root.left.split()
  tree.root.right.split()
  tree.root.left.left.split()
  tree.root.left.right.split()
  tree.root.left.left.left.split()
  tree.root.left.left.right.split()
  tree.root.left.left.left.left.split()
  #tree.root.left.left.left.right.split()
  tree.root.left.left.right.left.split()
  tree.root.left.left.right.left.left.split()
  #tree.root.left.left.right.right.split()
  tree.root.left.left.left.left.left.split()
  singles_exp(gamma,eta,tree,"broken",\
mode=0)
  pairs_exp(gamma,eta,tree,"broken",\
mode=(0,1))



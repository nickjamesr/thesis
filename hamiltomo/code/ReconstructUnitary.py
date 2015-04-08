#!/usr/bin/python
#--------------------------------------------------------------------------#
# ReconstructUnitary.py                                                    #
#                                                                          #
# Reconstruct the unitary from experimental data. Assumes that the scripts #
# ExperimentalPhases.py and ExperimentalSingles.py have already been run   #
# in order to generate the required data files                             #
#                                                                          #
# Dependencies:                                                            #
#  * numpy                                                                 #
#  * sys.argv                                                              #
#  * sys.exit                                                              #
#  * random.Random                                                         #
#                                                                          #
# Output directory:                                                        #
#   data/Unitaries                                                         #
#                                                                          #
#--------------------------------------------------------------------------#

import numpy

from sys import argv,exit
from random import Random

if __name__=='__main__':
  if len(argv)<4:
    print '''Usage: ReconstructUnitary.py <wavelength> <refcol> <refrow>
wavelength : Wavelength (774,776,778)
refcol     : Reference column (8,9)
refrow     : Reference row (3,4,6)'''
    exit(1)
  else:
    wavelength=int(argv[1])
    refcol=int(argv[2])
    refrow=int(argv[3])
  i=refrow
  k=refcol
  eps=1e-10

  columns=range(8,12)
  columns.remove(refcol)
  rows=range(21)
  rows.remove(refrow)

  rng=Random(314)

  U=numpy.loadtxt('data/Singles/{0:d}_absolutes.dat'.format(wavelength))
  U=numpy.sqrt(U)
  for l in columns:
    signs=numpy.loadtxt('data/{0:d}/Dips/refs{1:02d}{2:02d}_\
col{3:02d}_signs.dat'.format(wavelength,refcol,refrow,l), usecols=(1,),\
dtype=int)
    for jdx,j in enumerate(rows):
      if abs(U[j,l])<eps:
        pass # Matrix element is zero: phase does not matter
        '''elif abs(U[i,k]*U[j,l]*U[i,l]*U[j,k])<eps:
        # Ratio is not defined: cannot determine phase
        # Randomise phase?
        r=rng.uniform(0,1)
        if r>0.5:
          pass
          #U[j,l]*=-1'''
      else:
        if signs[jdx]==1:
          U[j,l]*=-1
        elif signs[jdx]==0:
          print "({0:02d},{1:02d}) undefined".format(j,l)
  numpy.savetxt("data/Unitaries/{0:d}_refs{1:02d}{2:02d}.dat".format(wavelength,
refcol,refrow),U[:,8:12])
  # test orthogonality
  for i,j in [(8,9),(8,10),(8,11),(9,10),(9,11),(10,11)]:
    print "{0:02d} {1:02d} {2:.4f}".format(i,j,abs(numpy.dot(U[:,i],U[:,j])))



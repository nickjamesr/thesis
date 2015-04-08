#!/usr/bin/python
#--------------------------------------------------------------------------#
# ReconstructHamiltonian.py                                                #
#                                                                          #
# Reconstruct the hamiltonian from the calculated unitaries. Assumes that  #
# the script ReconstructUnitaries.py has been run on the appropriate       #
# combination of reference row and column in order to generate the         #
# required files.                                                          #
#                                                                          #
# Dependencies:                                                            #
#  * numpy                                                                 #
#  * sys.argv                                                              #
#  * sys.exit                                                              #
#                                                                          #
# Output directory:                                                        #
#   data/Hamiltonians                                                      #
#                                                                          #
#--------------------------------------------------------------------------#

import numpy

from sys import argv,exit

if __name__=='__main__':
  if len(argv)<3:
    print '''Usage: ReconstructUnitary.py <refcol> <refrow>
refcol     : Reference column (8,9)
refrow     : Reference row (3,4,6)'''
    exit(1)
  else:
    refcol=int(argv[1])
    refrow=int(argv[2])
  i=refrow
  k=refcol

  Uminus=numpy.loadtxt("data/Unitaries/778_refs{0:02d}{1:02d}.dat".format(
refcol,refrow),dtype=complex)
  U=numpy.loadtxt("data/Unitaries/776_refs{0:02d}{1:02d}.dat".format(
refcol,refrow),dtype=complex)
  Uplus=numpy.loadtxt("data/Unitaries/774_refs{0:02d}{1:02d}.dat".format(
refcol,refrow),dtype=complex)

  H=1j*numpy.dot(U.T, (Uplus-Uminus))
  #H=1j*(numpy.dot(Uminus.T,Uplus)-numpy.dot(Uplus.T,Uminus))
  # Take Hermition part
  H=(H+H.conjugate().T)
  
  fout=open("data/Hamiltonians/refs{0:02d}{1:02d}.dat".format(refcol,refrow),
'w')
  for i in range(4):
    for j in range(4):
      fout.write("{0:.5f} ".format(abs(1j*H[i,j])))
    fout.write("\n")

#!/usr/bin/python
#--------------------------------------------------------------------------#
# MANIFOLD.PY                                                              #
# Write the data file required to plot the a manifold                      #
#                                                                          #
# Dependencies:                                                            #
#  * numpy                                                                 #
#  * pttools.abs2, pttools.ptmatrix                                        #
#                                                                          #
# Output:                                                                  #
#    manifold_A.dat                                                        #
#    rawmanifold_A.dat                                                     #
#                                                                          #
#--------------------------------------------------------------------------#

import numpy

from pttools import abs2,ptmatrix

if __name__=='__main__':
  J=1.0

  fout=open("../data/manifold/manifold_A.dat", 'w')
  for gamma in numpy.linspace(0.9,1.1,100):
    for t in numpy.linspace(0,11,110):
      U,norm=ptmatrix(gamma,J,t)
      fout.write("{0:.4f} {1:.4f} {2:.4f}\n".format(gamma,t,\
norm*norm*abs2(U[0,0])))
    fout.write("\n")
  fout.close()

  fout=open("../data/manifold/rawmanifold_A.dat", 'w')
  for gamma in numpy.linspace(0.9,1.1,100):
    for t in numpy.linspace(0,11,110):
      U,norm=ptmatrix(gamma,J,t)
      fout.write("{0:.4f} {1:.4f} {2:.4f}\n".format(gamma,t,abs2(U[0,0])))
    fout.write("\n")
  fout.close()

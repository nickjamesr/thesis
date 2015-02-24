#!/usr/bin/python
#--------------------------------------------------------------------------#
# MATRICES.PY                                                              #
# Write matrices for pt-symmetry experiment                                #
#                                                                          #
# Dependencies:                                                            #
#  * numpy                                                                 #
#  * math                                                                  #
#  * bintree.node, bintree.bintree                                         #
#  * pttools.ptmatrix                                                      #
#  * output.addline, output.printmatrix                                    #
#                                                                          #
# Output directory:                                                        #
#    data                                                                  #
#                                                                          #
#--------------------------------------------------------------------------#

import numpy
import math

from bintree import node, bintree
from pttools import ptmatrix
from output import addline, printmatrix

if __name__=='__main__':
  ### SYMMETRIC ###
  J=1.0
  gamma=0.95
  if (J!=gamma):
    period=math.pi/math.sqrt(abs(J**2-gamma**2))
  else:
    period=10
  with open("../data/symmetric/theory.dat","w") as fout:
    fout.write("# t J gamma norm A B C D AB AC AD BC BD CD\n")
    for t in numpy.linspace(0,period,200):
      U,norm=ptmatrix(gamma,J,t)
      addline(gamma,J,t,U,norm,fout)

  # Set up binary tree describing experimental data
  tree=bintree(0.,period)
  tree.root.split()
  tree.root.left.split()
  tree.root.right.split()
  tree.root.left.left.split()
  tree.root.right.right.split()
  tree.root.left.left.left.split()
  tree.root.right.right.right.split()
  tree.root.left.left.left.left.split()
  tree.root.right.right.right.right.split()
  
  with open("../data/symmetric/simulated.dat","w") as fout:
    fout.write("# t J gamma norm A B C D AB AC AD BC BD CD\n")
    for n,t in enumerate(tree.points()):
      U,norm=ptmatrix(gamma,J,t)
      addline(gamma,J,t,U,norm,fout)
      with open("../data/symmetric/{0:02d}/matrix.dat".format(n),"w") as mout:
        printmatrix(U,mout);
      with open("../data/symmetric/{0:02d}/info.txt".format(n),"w") as out:
        out.write("J     = {0:.4f}\ngamma = {1:.4f}\nt     = {2:.4f}\
\nnorm  = {3:.4f}\n".format(J,gamma,t,norm))

  ### CRITICAL ###
  J=1.0
  gamma=1.0
  if (J!=gamma):
    period=math.pi/math.sqrt(abs(J**2-gamma**2))
  else:
    period=10
  with open("../data/critical/theory.dat","w") as fout:
    fout.write("# t J gamma norm A B C D AB AC AD BC BD CD\n")
    for t in numpy.linspace(0,period,200):
      U,norm=ptmatrix(gamma,J,t)
      addline(gamma,J,t,U,norm,fout)

  # Set up binary tree describing experimental data
  tree=bintree(0.,10.)
  tree.root.split()
  tree.root.left.split()
  tree.root.right.split()
  tree.root.left.left.split()
  tree.root.left.right.split()
  tree.root.left.left.left.split()
  tree.root.left.left.left.left.split()
  tree.root.left.left.left.left.left.split()
  
  with open("../data/critical/simulated.dat","w") as fout:
    fout.write("# t J gamma norm A B C D AB AC AD BC BD CD\n")
    for n,t in enumerate(tree.points()):
      U,norm=ptmatrix(gamma,J,t)
      addline(gamma,J,t,U,norm,fout)
      with open("../data/critical/{0:02d}/matrix.dat".format(n),"w") as mout:
        printmatrix(U,mout);
      with open("../data/critical/{0:02d}/info.txt".format(n),"w") as out:
        out.write("J     = {0:.4f}\ngamma = {1:.4f}\nt     = {2:.4f}\
\nnorm  = {3:.4f}\n".format(J,gamma,t,norm))

  ### BROKEN ###
  J=1.0
  gamma=1.05
  if (J!=gamma):
    period=math.pi/math.sqrt(abs(J**2-gamma**2))
  else:
    period=10
  with open("../data/broken/theory.dat","w") as fout:
    fout.write("# t J gamma norm A B C D AB AC AD BC BD CD\n")
    for t in numpy.linspace(0,period,200):
      U,norm=ptmatrix(gamma,J,t)
      addline(gamma,J,t,U,norm,fout)

  # Set up binary tree describing experimental data
  tree=bintree(0.,period)
  tree.root.split()
  tree.root.left.split()
  tree.root.right.split()
  tree.root.left.left.split()
  tree.root.left.right.split()
  tree.root.left.left.left.split()
  tree.root.left.left.left.left.split()
  tree.root.left.left.left.left.left.split()
  
  with open("../data/broken/simulated.dat","w") as fout:
    fout.write("# t J gamma norm A B C D AB AC AD BC BD CD\n")
    for n,t in enumerate(tree.points()):
      U,norm=ptmatrix(gamma,J,t)
      addline(gamma,J,t,U,norm,fout)
      with open("../data/broken/{0:02d}/matrix.dat".format(n),"w") as mout:
        printmatrix(U,mout);
      with open("../data/broken/{0:02d}/info.txt".format(n),"w") as out:
        out.write("J     = {0:.4f}\ngamma = {1:.4f}\nt     = {2:.4f}\
\nnorm  = {3:.4f}\n".format(J,gamma,t,norm))





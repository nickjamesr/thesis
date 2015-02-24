#!/usr/bin/python
#--------------------------------------------------------------------------#
# OUTPUT.PY                                                                #
#                                                                          #
# Fuctions for writing pt data to files                                    #
#                                                                          #
# Dependencies:                                                            #
#  * sys.stdout                                                            #
#  * pttools.singles, pttools.pairs, pttools.cpairs                        #
#                                                                          #
#--------------------------------------------------------------------------#

from sys import stdout
from pttools import singles,pairs,cpairs

def addline(gamma, J, t, u, norm, fout=stdout, cols=(0,1)):
  '''Write a line to a file (default stdout) containing the expected
output probabilities when light (single photons and photon pairs) is
injected into the specified pt-evolution matrix.
gamma  : on-site potential
J      : cross-site tunneling
t      : evolution time
u      : unitary matrix given by evolution
norm   : matrix norm
fout   : file to write to
cols   : injection modes
return : None'''
  a,b,c,d=singles(u,cols[0])
  ab,ac,ad,bc,bd,cd=pairs(u,cols)
  fmt=""
  for i in range(14):
    fmt+="{"+str(i)+":.4f} "
  fmt+="\n"
  fout.write(fmt.format(t,J,gamma,norm,a,b,c,d,ab,ac,ad,bc,bd,cd))

def printmatrix(U, fout=stdout):
  '''Write a complex matrix to a file
U      : matrix to write
fout   : file to write to
return : None'''
  for i in range(4):
    for j in range(4):
      x,y=U[i,j].real, U[i,j].imag
      fout.write("{0:+.4f}{1:+.4f}j ".format(x,y))
    fout.write("\n")

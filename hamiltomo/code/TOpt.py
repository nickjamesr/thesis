#!/usr/bin/python
#--------------------------------------------------------------------------#
# TOpt.py                                                                  #
#                                                                          #
# Estimate the optimum time difference for the quantum walk based on       #
# Pete's estimate of the Hamiltonian and noise in the amplitude            #
# reconstruction.                                                          #
#                                                                          #
# Dependencies:                                                            #
#                                                                          #
# Output directory:                                                        #
#                                                                          #
#--------------------------------------------------------------------------#

import sys
sys.path.append("code")

import numpy
import hamiltomo
import noise
import distances

def WriteMatrix(fname,M):
  fout=open(fname,'w')
  for i in range(21):
    for j in range(21):
      if i==j:
        fout.write("{0:.4f} ".format(abs(0.5*(M[i,j]+M[j,i].conjugate()))))
      else:
        fout.write("{0:.4f} ".format(abs(0.5*(M[i,j]+M[j,i].conjugate()))))
    fout.write("\n")
  fout.close()

if __name__=='__main__':
  t=6.682 # Determined by TEvol.py
  eps=5e-5
  pairs=1e8
  refs=(4,9)

  H=hamiltomo.PetesHamiltonian()
  Hrb=hamiltomo.DerivativeRealBorder(H,t,2**-10,refs)
  WriteMatrix('data/TOpt/ideal.dat',Hrb)
  texp=0.06
  G=hamiltomo.Derivative(H,t,texp,noise.WalkWithExperimentalNoise,\
    (eps,pairs,refs))
  WriteMatrix('data/TOpt/experimental.dat',G)

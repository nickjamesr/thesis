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

  dt=0.5
  eps=1e-4
  tstep=2**(0.25)
  nsteps=21
  nreps=16
  dist=numpy.zeros((nreps,))
  fout=open("data/TOpt/ErrorVsTime.dat",'w')
  for i in range(nsteps):
    for j in range(nreps):
      G=hamiltomo.Derivative(H,t,dt,noise.PowerMeterNoise,(eps,))
      dist[j]=distances.HermitianDistance(H,G)
    fout.write("{0:.4g} {1:.4g} {2:.4g} {3:.4g}\n".format(dt,numpy.mean(dist),\
      numpy.mean(dist)-numpy.std(dist), numpy.mean(dist)+numpy.std(dist)))
    print dt,numpy.mean(dist)
    dt/=tstep
  fout.close()

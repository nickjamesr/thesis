#!/usr/bin/python

#----------------------------------------------------------------------------#
# COMPARISON.PY                                                              #
#                                                                            #
# Compare the time derivative (Hamiltomo) to an expansion using the matrix   #
# logerithm.                                                                 #
#                                                                            #
# Dependencies:                                                              #
#  * hamiltomo.py                                                            #
#  * noise.py                                                                #
#  * distances.py                                                            #
#  * numpy                                                                   #
#                                                                            #
#----------------------------------------------------------------------------#

import hamiltomo
import noise
import distances

import numpy

if __name__=='__main__':
  # General parameters
  dim=9
  seed=314
  ntrials=100
  td=numpy.empty((ntrials,))

  # Timestep parameters
  t=1.0
  dt=0.5

  # Noise parameters
  p=-1
  dtheta=pow(10,p)

  params=[(0.5,1e-3,13), (0.5,1e-2,13), (0.5,1e-1,13), (0.5,1e-1,8),\
(0.05,1e-6,6), (0.05,1e-5,6), (0.05,1e-4,6)]

  # Choose a Hamiltonian
  H=hamiltomo.RandomHamiltonian(dim,seed=seed)

  j=0
  for dt,dtheta,nmax in params:
    # Calculate performance of time derivative method
    for i in xrange(ntrials):
      Gdt=hamiltomo.Derivative(H,t,dt,noise.ReckNoise,(dtheta,))
      td[i]=distances.HermitianDistance(H,Gdt)
    Ddt=(numpy.mean(td), numpy.std(td))

    with open("data/comparison{0:02d}.dat".format(j),'w') as fout:
      fout.write("# {0:d} modes, {1:d} trials, seed {2:.4f}\n".format(dim,\
        ntrials,seed))
      fout.write("# noise : {0:.1g}\n".format(dtheta))
      fout.write("# t1    : {0:.4f}\n".format(t))
      fout.write("# t2    : {0:.4f}\n".format(t+dt))
      fout.write("# Order Log dLog Diff dDiff\n")
      for n in range(1,nmax+1):
        for i in xrange(ntrials):
          Glog=hamiltomo.TaylorSeries(H,t,t+dt,n,noise.ReckNoise,(dtheta,))
          td[i]=distances.HermitianDistance(H,Glog)
          Dlog=(numpy.mean(td), numpy.std(td))
        fout.write("{0:d} {1:.4g} {2:.4g} {3:.4g} {4:.4g}\n".format(n,\
          Dlog[0], Dlog[1], Ddt[0], Ddt[1]))
    j+=1






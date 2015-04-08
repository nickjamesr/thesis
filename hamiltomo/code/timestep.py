#!/usr/bin/python
#--------------------------------------------------------------------------#
# TIMESTEP.PY                                                              #
#                                                                          #
# Takes a nearest-neighbour Hamiltonian ( average couplings 0.5+0.5i) and  #
# uses the time derivative method to reconstruct (with noise in unitary)   #
# for a range of timesteps                                                 #
#                                                                          #
# Noise is applied directly to the unitary by considering dialling errors  #
# in a Reck scheme realisation.                                            #
#                                                                          #
# Dependencies:                                                            #
#  * hamiltomo.py                                                          #
#  * distances.py                                                          #
#  * noise.py                                                              #
#  * numpy                                                                 #
#                                                                          #
# Output directory:                                                        #
#   data/timestep                                                          #
#                                                                          #
#--------------------------------------------------------------------------#

import hamiltomo
import distances
import noise
import numpy

### Run this on execute command
if __name__=='__main__':
  dim=9
  t=1.5

  ntimesteps=40
  nsteps=20

  H=hamiltomo.RandomHamiltonian(dim,0.5,0.1)

  # No noise
  fname="data/timestep0.dat"
  fout=open(fname,'w')
  dt=0.5
  for j in range(ntimesteps):
    G=hamiltomo.Derivative(H,t,dt,noise.NoNoise)
    td=distances.HermitianDistance(H,G)
    fout.write("{0:.5g} {1:.5g} {2:.5g}\n".format(dt,td,0.))
    dt/=2
  fout.close()

  # Vary level of noise in unitary
  for p in range(4,10,2):
    dt=0.5
    dtheta=pow(10,-p)
    print p
    fname="data/timestep_1e-{0:02d}.dat".format(p)
    fout=open(fname,'w')
    for i in range(ntimesteps):
      # Graph error vs timestep
      td=[]
      for j in range(nsteps):
        # Average over noise
        G=hamiltomo.Derivative(H,t,dt,noise.ReckNoise,(dtheta,))
        td.append(distances.HermitianDistance(H,G))
      fout.write("{0:.5g} {1:.5g} {2:.5g}\n".format(dt,numpy.mean(td),\
numpy.std(td)))
      dt/=pow(2,0.25)
    fout.close()




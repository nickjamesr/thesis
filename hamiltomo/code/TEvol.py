#!/usr/bin/python
#--------------------------------------------------------------------------#
# TEvol.py                                                                 #
#                                                                          #
# Estimate the evolution time of the quantum walk based on Pete's estimate #
# of the Hamiltonian and the singles data from the experiment              #
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
import distances

if __name__=='__main__':
  for wl in (774,776,778):
    # Get the singles data
    exp=numpy.loadtxt("data/Singles/{0:d}_absolutes.dat".format(wl))
    print distances.KolmogorovDistance(exp,exp)

    # Open output file
    fout=open("data/TOpt/tevol_{0:d}.dat".format(wl),'w')

    for t in numpy.linspace(6.2,7.0,801):
      # Get simulated amplitudes
      sim=abs(hamiltomo.RealWalk(t))**2
      # Calculate the trace distance
      kd=distances.KolmogorovDistance(sim,exp)
      td=abs(distances.TraceDistance(sim,exp))
      # Write to the file
      fout.write("{0:.4f} {1:.4f} {2:.6f}\n".format(t,td,kd))

    # Close file
    fout.close()
      

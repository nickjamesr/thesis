#!/usr/bin/python

#----------------------------------------------------------------------------#
# NOISE.PY                                                                   #
#                                                                            #
# Functions for applying noise to unitaries. Most likely to be physically    #
# motivated in some way, but not all are complete simulations of experiment  #
#                                                                            #
# Dependencies:                                                              #
#  * hamiltomo.py                                                            #
#  * random.Random                                                           #
#  * numpy                                                                   #
#                                                                            #
#----------------------------------------------------------------------------#

import hamiltomo
import numpy

from random import Random

def WriteMatrix(fname,M):
  fout=open(fname,'w')
  for i in range(21):
    for j in range(21):
      if i==j:
        fout.write("0.000 ")
      else:
        fout.write("{0:.4f} ".format(M[i,j].real))
    fout.write("\n")
  fout.close()

def NoNoise(U,args=()):
  '''Token function to apply no noise to a unitary
U      : input unitary
args   : For consistency with other noise functions. Ignored.
return : (numpy array) U'''
  return U

def ReckNoise(U,dtheta,seed=None):
  '''Return a unitary with noise applied as error in phase shifts of Reck
scheme
U      : unitary to apply noise to
dtheta : magnitude of noise in phase shifts
seed   : (optional) seed for rng
return : (numpy array) unitary with noise applied'''
  dim=U.shape[0] # assume square
  R=hamiltomo.Reck(dim)
  R.from_unitary(U)
  R.perturb(dtheta,seed)
  V=R.unitary()
  return V

def AmplitudeNoise(U,counts,losses=None,seed=None):
  '''Return a unitary with noise applied as Poissonian noise in amplitude
reconstruction but ideal phases
U      : unitary to apply noise to
counts : singles counts for Poissonian noise
losses : input and output losses
seed   : (optional) seed for rng
return : (numpy array) unitary with noise applied'''
  pre,V,post=hamiltomo.Normalise(hamiltomo.ExperimentalAmplitudes(U,counts,\
losses,seed),eps=1e-15)
  return V

def PowerMeterNoise(U,eps,losses=None,seed=None):
  '''Return a unitary with noise applied as +-eps on power meter readings
but ideal phases. The total power in each column (i.e. input) is 1.
U      : unitary to apply noise to
eps    : error on power meter readings
losses : input and output losses
seed   : (optional) seed for rng
return : (numpy array) unitary with noise applied'''
  dim=U.shape[0] # assume square
  amps=hamiltomo.abs2(U)
  rng=Random(seed)
  if losses is None:
    losses=numpy.ones((2,dim))
  V=numpy.zeros_like(U)
  for i in range(dim):
    for j in range(dim):
      amp=numpy.sqrt(max(amps[i,j]*losses[0,j]*losses[1,i]+rng.gauss(0,eps),0))
      phase=U[i,j]/abs(U[i,j])
      V[i,j]=amp*phase
  pre,V,post=hamiltomo.Normalise(V,eps=1e-10,maxiter=200)
  return V

def WalkWithExperimentalNoise(U,eps,pairs,refs=(0,0),losses=None,seed=None):
  '''Return a unitary with noise applied as Poissonian noise in both
amplitude and phase reconstructions. Function assumes U is a
quantum walk unitary, therefore all elements in real-bordered
form are real and only signs must be deduced from dips. These
signs are determined by taking single point measurements for
classical and quantum coincidences, rather than fitting a full
dip.
U      : (ideal) unitary to apply noise to
eps    : error in power meter readings for amplitudes
pairs  : rate of coincidence counts  for Poissonian noise
refs   : reference row and column (respectively) for phases
losses : input and output losses
seed   : (optional) seed for rng
return : (numpy array) unitary with noise applied'''
  # Get the amplitudes
  V=numpy.abs(PowerMeterNoise(U,eps,losses,seed))

  # Get the phases
  nrows,ncols=U.shape
  refrow,refcol=refs
  rows=range(nrows)
  rows.remove(refrow)
  cols=range(ncols)
  cols.remove(refcol)
  for i in rows:
    for j in cols:
      # Get the phase (sign)
      cmean=float(pairs)*(hamiltomo.abs2(U[refrow,refcol]*U[i,j])+\
hamiltomo.abs2(U[refrow,j]*U[i,refcol]))
      qmean=float(pairs)*hamiltomo.abs2(U[refrow,refcol]*U[i,j]+\
U[refrow,j]*U[i,refcol])
      if cmean<1000:
        # Poissonian
        classical=numpy.random.poisson(cmean)
      else:
        # Gaussian approximation
        classical=numpy.random.normal(cmean,numpy.sqrt(cmean))
      if qmean<1000:
        # Poissonian
        quantum=numpy.random.poisson(qmean)
      else:
        # Gaussian approximation
        quantum=numpy.random.normal(qmean,numpy.sqrt(qmean))
      #if cmean > qmean:
      if classical > quantum:
        # Dip => negative sign
        V[i,j]*=float(-1)
  return V






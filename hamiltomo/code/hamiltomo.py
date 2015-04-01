#!/usr/bin/python

#---------------------------------------------------------------#
# HAMILTOMO.PY                                                  #
#                                                               #
# Comparison of errors in Hamiltonian reconstruction between 3  #
# different methods:                                            #
#  * time derivative                                            #
#  * power series of logarithm                                  #
#  * power series of sine                                       #
#                                                               #
# Dependencies                                                  #
#  * numpy                                                      #
#  * cmath                                                      #
#  * math                                                       #
#  * scipy.linalg                                               #
#  * random.Random                                              #
#  * noise.py                                                   #
#  * distances.py                                               #
#                                                               #
#---------------------------------------------------------------#

import numpy
import cmath
import math

import noise
import distances

from scipy import linalg
from random import Random
from sys import exit # DEBUG

### Class definitions

class Reck:
  '''Class to contain a Reck scheme representation of a unitary,
including the (physically unobservable) input and output phases.'''
  def __init__(self,dim):
    '''Initialise to the identity
dim    : number of dimensions
return : None'''
    self.dim=dim
    self.params=numpy.zeros((dim,dim))
    for i in range(int(dim/2)):
      self.params[2*i,2*i]=numpy.pi
    for i in range(dim-1):
      for j in range(i+1,dim):
        self.params[i,j]=numpy.pi

  def from_unitary(self,V):
    '''Calculate the Reck scheme (circuit) parameters from an
existing unitary matrix
V      : unitary matrix
return : None'''
    U=V.copy()
    for i in range(self.dim-1):
      # Reverse the i-th diagonal
      for j in range(self.dim-1,i,-1):
        # Reverse the j-th element in that diagonal
        # Phase shift on mode j-1
        z=U[j-1,i]/U[j,i]
        self.params[j,i]=cmath.phase(z)
        phi=z.conjugate()/abs(z)
        U[j-1,:]*=phi
        # MZI on modes j-1,j
        r=abs2(U[j-1,i])/(abs2(U[j-1,i])+abs2(U[j,i])) # Power reflectivity
        self.params[i,j]=2*numpy.arcsin(numpy.sqrt(r))
        phi=numpy.exp(-0.5j*(self.params[i,j]+numpy.pi))
        t=phi*numpy.sqrt(1-r)  # Amplitude transmission
        r=phi*numpy.sqrt(r)    # Amplitude reflection
        U[j-1,:],U[j,:]=r*U[j-1,:]+t*U[j,:], t*U[j-1,:]-r*U[j,:]
    for i in range(self.dim):
      # Reverse input phases
      self.params[i,i]=cmath.phase(U[i,i])
      U[i,i]=abs(U[i,i])

  def unitary(self):
    '''Compute and return the unitary matrix describing the Reck scheme
return : numpy array containing the unitary matrix description'''
    U=Identity(self.dim)
    for i in range(self.dim-1):
      # Apply the i-th diagonal
      for j in range(self.dim-1,i,-1):
        # Apply the j-th element in that diagonal
        # Phase shift on mode j-1
        U[:,j-1]*=numpy.exp(1j*self.params[j,i])
        # MZI on modes j-1,j
        phi=numpy.exp(0.5j*(self.params[i,j]+numpy.pi))
        r=phi*numpy.sin(self.params[i,j]/2)
        t=phi*numpy.cos(self.params[i,j]/2)
        U[:,j-1],U[:,j]=r*U[:,j-1]+t*U[:,j], t*U[:,j-1]-r*U[:,j]
    for i in range(self.dim):
      # Apply the input phase
      U[:,i]*=numpy.exp(1j*self.params[i,i])
    return U

  def real_border(self):
    '''Set input and output phases to match and cancel internal phases.
Resulting unitary will have zero phase on the border elements.
Note that this is not the same as setting input and output phases
to zero.
return : None'''
    # Remove output phases
    for i in range(self.dim):
      self.params[i,0]=0
    # Negate input phases
    phi=0
    for i in range(1,self.dim-1):
      phi-=self.params[i+1,i]
      self.params[i,i]=phi
    self.params[dim-1,dim-1]=phi

  def perturb(self,dtheta,seed=None):
    '''Perturb the unitary by applying the sort of errors that we
may experience in a Reck scheme realisation.
Shifts each phase by a random amount drawn from a Gaussian with
width dtheta.
dtheta : amplitude of error in phase.
seed   : (optional) seed for rng
return : None'''
    rng=Random(seed)
    for i in range(self.dim):
      for j in range(self.dim):
        d=rng.gauss(0,dtheta)
        self.params[i,j]+=d
    pass

### Function definitions

def Identity(dim, dtype=complex):
  '''Return the identity matrix
dim    : number of dimensions
dtype  : data type of returned array (default complex)
return : numpy array containing the identity'''
  I=numpy.zeros((dim,dim), dtype)
  for i in range(dim):
    I[i,i]=1
  return I

def proj(u,v):
  '''Project u onto the direction of v'''
  uv = numpy.vdot(u,v)
  uu = numpy.vdot(u,u)
  return (uv/uu)*u

def vecnorm(v):
  '''Return the norm of a complex vector'''
  n = 0
  for i in range(len(v)):
    n += v[i]*v[i].conj()
  return numpy.sqrt(abs(n))

def abs2(z):
  '''Absolute square of a complex number'''
  return abs(z)**2

def RealBorder(M,refs=(0,0)):
  '''Apply phases to a complex matrix to make the border elements real.
Equivalent to pre- and post-multiplying by diagonal matrices
of phases.
M      : complex numpy array
refs   : reference row and column (respectively) for calculating
         phases
return : numpy array containing real-bordered matrix.'''
  dim=M.shape[0]
  refrow,refcol=refs
  for i in range(dim):
    z=M[i,refcol].conjugate()/abs(M[i,refcol])
    M[i,:]*=z
  for i in range(1,dim):
    z=M[refrow,i].conjugate()/abs(M[refrow,i])
    M[:,i]*=z
  return M

def RandomUnitary(dim, seed=None):
  '''Return a Haar unitary random matrix
dim    : number of dimensions
seed   : (optional) seed for rng
return : numpy array containing a Haar random unitary matrix'''
  rng = Random(seed)
  # Generate a random Gaussian matrix
  M = numpy.zeros((dim,dim), dtype=complex)
  for i in range(dim):
    for j in range(dim):
      M[i,j] = complex(rng.gauss(0,1), rng.gauss(0,1))
  # Gram-Schmidt orthogonalisation
  for i in range(dim):
    v = M[:,i]
    v /= vecnorm(v)
    for j in range(i+1, dim):
      u = M[:,j]
      u -= proj(v,u)
  return M

def RandomHamiltonian(dim, mu=0.5, sigma=0.05, seed=None):
  '''Generate a random tridiagonal Hamiltonian. Diagonal terms are zero,
off-diagonal (coupling) terms have the mean and standard deviation
specified.
dim    : number of dimensions
mu     : mean of disorder (default 0.5)
sigma  : standard deviation of disorder (default 0.05)
seed   : (optional) random seed for rng
return : dim x dim complex array containing a randomised Hamiltonian'''
  H=numpy.zeros((dim,dim),dtype=complex)
  rng=Random(seed)
  for i in range(dim-1):
    x=rng.gauss(mu,sigma)
    y=rng.gauss(mu,sigma)
    H[i,i+1]=complex(x,y)
    H[i+1,i]=complex(x,-y)
  return H

def dagger(U):
  '''Hermitian conjugate (conjugate transpose) of a matrix
U      : complex matrix
return : Hermitian conjugate of U'''
  return (U.T).conjugate()

def Derivative(H,t,dt,noise,args=()):
  '''Return an estimate of H using the (3 point) time derivative method
H      : exact Hamiltonian underlying the unitary
t      : central time at which measurements are taken
dt     : timestep
noise  : noise function to apply to unitaries
args   : args to pass to noise function
return : numpy array containing estimate of Hamiltonian'''
  # t : Central timestep
  U=noise(expi(H,t),*args)
  # t-h
  Uminus=noise(expi(H,t-dt),*args)
  # t+h
  Uplus=noise(expi(H,t+dt),*args)

  return (0.5j/dt)*numpy.dot((Uplus-Uminus),dagger(U))

def TaylorSeries(H,t1,t2,order,noise,args=()):
  '''Return an estimate of H using the Taylor expansion method to the
specified order.
H      : exact Hamiltonian underlying the unitary evolution
t1     : first measurement of U
t2     : second measurement of U
order  : order of Taylor series
oise   : noise function to apply to unitaries
args   : arguments to pass to noise function
return : (numpy array) estimate of Hamiltonian'''
  dim=H.shape[0]
  dt=t2-t1
  # t1 : initial time
  U_init=noise(expi(H,t1),*args)
  # t2 : final time
  U_final=noise(expi(H,t2),*args)
  # propagator between t1 and t2
  U=numpy.dot(U_final,dagger(U_init))
  matsin=0.5j*(U-dagger(U))
  matcos=0.5*(U+dagger(U))
  identity=Identity(dim)
  matpow=Identity(dim)
  c_k=1
  G=Identity(dim)
  for k in range(1,order):
    matpow=numpy.dot(matpow,(matcos-identity))
    c_k*=(-1/2.)*(k/(k+0.5))
    G+=c_k*matpow
  return (1/(2*dt))*numpy.dot(matsin,G)

def expi(H,t):
  '''Evolve the Hamiltonian H for time t
H      : evolution Hamiltonian (assumed Hermitian)
t      : evolution time
return : unitary matrix U=e^{-iHt}'''
  dim=H.shape[0]
  evals,evecs=linalg.eigh(H)
  diag=numpy.zeros((dim,dim),dtype=complex)
  for i in range(dim):
    diag[i,i]=numpy.exp(0-1j*evals[i]*t)
  return numpy.dot(evecs,numpy.dot(diag,dagger(evecs)))

def ExperimentalAmplitudes(U,counts,losses=None,seed=None):
  '''Perform the amplitude (singles) part of the reconstruction of U,
but keep the ideal phases. This represents a best-case scenario
for real, experimental reconstructions.
U      : Input (ideal) unitary
counts : Count rate of source in simulated experiment
losses : (optional) 2xN array of losses (must be <=1) input
         then output
seed   : (optional) seed for rng
return : matrix with amplitudes from simulated experiment but no
         error in phases (may not be unitary)'''
  dim=U.shape[0] # Assume square
  V=numpy.zeros_like(U)
  if seed is not None:
    numpy.random.seed(seed)
  if losses is None:
    losses=numpy.ones((2,dim))
  for i in range(dim):
    for j in range(dim):
      mean=abs2(U[i,j])*counts*losses[0,j]*losses[1,i]
      if mean<1000:
        # Take from Poisson distribution
        V[i,j]=numpy.sqrt(numpy.random.poisson(mean))*U[i,j]/abs(U[i,j])
      else:
        # Approximate Poisson as normal distribution
        V[i,j]=numpy.sqrt(numpy.random.normal(mean,numpy.sqrt(mean)))*\
U[i,j]/abs(U[i,j])
  return V

def Defect(S):
  '''Calculate how far the matrix S is from being normalised
S      : (numpy array) non-normalised matrix
return : (float) distance from normalised'''
  nrows,ncols=S.shape
  rowsum=sum([abs(sum(abs2(S[i,:]))-1) for i in range(nrows)])
  colsum=sum([abs(sum(abs2(S[:,j]))-1) for j in range(ncols)])
  err=(rowsum+colsum)/(nrows+ncols)
  return err

def Normalise(S, eps=1e-7, maxiter=100):
  '''Simultaneously normalise all rows and columns in matrix S, to
specified tolerance, using iterative process
S       : (numpy array) non-normalised matrix
eps     : tolernance
maxiter : Maximum number of iterations
return  : pre,S,post'''
  nrows,ncols=S.shape
  pre=numpy.ones((nrows,))   # Keep track of the transformation.
  post=numpy.ones((ncols,))  # This gives the input/output losses
  err=Defect(S)
  n=0
  while err>eps and n<maxiter:
    for i in range(nrows):
      # Normalise columns
      post[i]*=1/sum(abs2(S[:,i]))
      S[:,i]/=numpy.sqrt(sum(abs2(S[:,i])))
      # Normalise rows
      pre[i]*=1/sum(abs2(S[i,:]))
      S[i,:]/=numpy.sqrt(sum(abs2(S[i,:])))
    err=Defect(S)
    n+=1
  return pre,S,post

def Reconstruct(wavelength, refs=(6,8)):
  '''Reconstruct the matrix for the specified wavelength from pre-
processed experimental data.
wavelength : (int) 774,776,778
res        : (tuple) reference row and column (respectively) for
             real border
return     : 21x4 array containing the reconstructed unitary'''
  cols=(8,9,10,11)
  mode={8:19, 9:18, 10:17, 11:16}
  refrow,refcol=refs
  refcolidx=cols.index(refcol)
  U=numpy.zeros((21,4),dtype=complex)
  M=numpy.loadtxt("../data/{0:d}/absolutes.dat".format(wavelength))
  S=numpy.zeros((21,4),dtype=complex)

  # Get singles (from heralded photons)
  for i,col in enumerate(cols):
    S[:,i]=numpy.loadtxt("../data/{0:d}/Singles/singles_D{1:d}.dat".format(\
      wavelength, mode[col]))
  
  # Get amplitudes (precomputed from blocking data)
  for i,col in enumerate(cols):
    U[:,i]=numpy.sqrt(M[:,col])

  # Get absolute phases (using prefittid dips)
  for j,col in enumerate(cols):
    if col==refcol:
      continue
    C,D=min(mode[col],mode[refcol]),max(mode[col],mode[refcol])
    dips=numpy.loadtxt("../data/{0:d}/Dips/visibilities_D{1:d}_C{2:d}.dat"\
.format(wavelength,D,C))
    for row in range(21):
      if row==refrow:
        continue
      Rnum=S[refrow,refcolidx]*S[row,j]
      Rden=S[refrow,j]*S[row,refcolidx]
      if Rden==0 or Rnum==0:
        continue
      R=Rnum/Rden
      V=dips[row,refrow]
      c=-V*(1+R)/(2*numpy.sqrt(R))
      if c>=0:
        phi=0
      elif c<0:
        phi=numpy.pi
      U[row,j]*=numpy.exp(1j*phi)
  return U

### Run this on execute command
if __name__=='__main__':
  dim=21
  t1=6.0
  t2=6.5
  order=5
  losses=None

  numpy.set_printoptions(precision=3)

  H=RandomHamiltonian(dim,0.5,0.3)
  G=TaylorSeries(H,t1,t2,order,noise.NoNoise)
  print distances.HermitianDistance(H,G)

  fdir="data/series"
  fout=open(fdir+"/ideal.dat",'w')
  for row in H:
    for x in row:
      fout.write("{0:.5g} ".format(abs(x)))
    fout.write("\n")
  fout.close()

  fout=open(fdir+"/reconstructed.dat", 'w')
  for row in G:
    for x in row:
      fout.write("{0:.5g} ".format(abs(x)))
    fout.write("\n")
  fout.close()

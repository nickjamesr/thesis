#----------------------------------------------------------------------------#
# ERRORS.PY                                                                  #
#                                                                            #
# Method to compute the expected errors in count rates due to imperfect      #
# dialling                                                                   #
#                                                                            #
#----------------------------------------------------------------------------#

import numpy as np
import math
import sys

sys.path.append("code")
from scatterbox import Circuit

def DiallingErrors(mat,ntrials,errs=None,level=68.2):
  '''Calculate the dialling errors when attempting to dial unitary mat
with component errors errs
mat     : unitary to dial
ntrials : number of trials in Monte-Carlo
errs    : magnitude of dialling errors. Expecting tuple
          (at0, at1, pt1, pt2, aq0, aq1, aq2) of values
          in degrees. Defaults to 0.5 for amplitudes, 3 for phases
level   : percentile for errors
return  : tuple (quantum, classical, quart trit). Each item is a
          list of (-,+) tuples representing l-th percentile errors
          for a level l.'''
  lo=0.005*(100-level)
  hi=1-lo
  lo=int(math.floor(lo*ntrials))
  hi=int(math.ceil(hi*ntrials))
  c=Circuit()
  c.fromMatrix(mat)
  params=c.params()

  if errs is None:
    errs=(0.5,0.5,3,3,0.5,0.5,0.5)
  
  # Set up the arrays to store the data
  quart=np.empty((ntrials,4))     # A, B, C, D
  trit=np.empty((ntrials,4))      # A, B, C, D
  quantum=np.empty((ntrials,6))   # AB, AC, AD, BC, BD, CD
  classical=np.empty((ntrials,6)) # AB, AC, AD, BC, BD, CD

  # Populate the arrays with results of Monte-Carlo
  for i in xrange(ntrials):
    p=[np.random.normal(mu,s) for mu,s in zip(params,errs)]
    c.fromList(*p)
    quart[i]=c.quart()
    trit[i]=c.trit()
    quantum[i]=c.quantum()
    classical[i]=c.classical()

  # Find percentiles
  quart_lo=[sorted(quart[:,i])[lo] for i in range(4)]
  quart_hi=[sorted(quart[:,i])[hi] for i in range(4)]
  trit_lo=[sorted(trit[:,i])[lo] for i in range(4)]
  trit_hi=[sorted(trit[:,i])[hi] for i in range(4)]
  quantum_lo=[sorted(quantum[:,i])[lo] for i in range(6)]
  quantum_hi=[sorted(quantum[:,i])[hi] for i in range(6)]
  classical_lo=[sorted(classical[:,i])[lo] for i in range(6)]
  classical_hi=[sorted(classical[:,i])[hi] for i in range(6)]

  # Construct return values
  return [zip(x,y) for x,y in zip(\
 [quantum_lo,classical_lo,quart_lo,trit_lo],
 [quantum_hi,classical_hi,quart_hi,trit_hi])]

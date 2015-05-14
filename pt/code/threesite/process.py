#!/usr/bin/python
#--------------------------------------------------------------------------#
# PROCESS.PY                                                               #
#                                                                          #
# Functions to process data from the three site model                      #
#                                                                          #
# Dependencies:                                                            #
#  * numpy                                                                 #
#                                                                          #
#--------------------------------------------------------------------------#

import sys
sys.path.append("code/threesite")
sys.path.append("code")
import numpy

from os import path

from generate import trees
from pttools import threesitematrix
from bintree import node,bintree

def abs2(z):
  '''Calculate the absolute square of z
z      : object supporting abs and power
return : |z|**2'''
  return abs(z)**2

def Defect(S):
  '''Calculate how far the matrix S is from being normalised
S      : (numpy array) non-normalised matrix
return : (float) distance from normalised'''
  nrows,ncols=S.shape
  rowsum=sum([abs(sum(S[i,:])-1) for i in range(nrows)])
  colsum=sum([abs(sum(S[:,j])-1) for j in range(ncols)])
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
      post[i]*=1/sum(S[:,i])
      S[:,i]/=numpy.sqrt(sum(S[:,i]))
      # Normalise rows
      pre[i]*=1/sum(S[i,:])
      S[i,:]/=numpy.sqrt(sum(S[i,:]))
    err=Defect(S)
    n+=1
  return pre,S,post

def GetData(sym,num):
  '''Get the experimental data
sym    : symmetry ("symmetric" | "broken")
num    : number of matrix
return : (numpy arrays) singles,singles_err,pairs,pairs_err'''
  # Singles
  singles=numpy.zeros((6,6))
  singles_err=numpy.zeros((6,6))
  pairs=numpy.zeros((3,15))
  pairs_err=numpy.zeros((3,15))
  for mode in range(6):
    if num==0:
      fname="data/threesite/experimental/singles/identity_mode_{0:d}.ctx".\
format(mode+1)
    else:
      fname="data/threesite/experimental/singles/"+sym+\
"{0:d}_mode_{1:d}.ctx".format(num,mode+1)
    with open(fname,'r') as fin:
      for i in range(7):
        fin.readline() # Skip metadata and unheralded singles
      for i in range(6):
        label,count=fin.readline().strip().split(":")
        singles[mode][i]=float(count)
  singles_err=numpy.sqrt(singles)
  for i in range(6):
    # Normalise probabilities for each input. Do not correct for detector
    # efficiencies
    singles_err[i]/=sum(singles[i])
    singles[i]/=sum(singles[i])
    
  # Pairs
  for n,modes in enumerate([(0,1),(1,2),(0,2)]):
    i,j = modes
    fname="data/threesite/experimental/twofolds/{0:d}{1:d}/".format(i,j)+sym+\
"{0:d}.ctx".format(num)
    with open(fname,'r') as fin:
      fin.readline() # Skip metadata
      for k in range(15):
        label,count=fin.readline().strip().split(":")
        pairs[n][k]=float(count)
  pairs_err=numpy.sqrt(pairs)
  for i in range(3):
    # Normalise probabilities for each input combination. Do not correct for
    # detector efficiencies
    pairs_err[i]/=sum(pairs[i])
    pairs[i]/=sum(pairs[i])

  return singles,singles_err,pairs,pairs_err

def IdealPairs(U,mode):
  '''Get the pairs (normalised over visible pairs to unity) for matrix U
and input modes mode
U      : unitary
mode   : input modes (i,j)
return : (numpy array) 15 pairs normalised to 1'''
  pairs=[(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),\
(2,5),(3,4),(3,5),(4,5)]
  powers = numpy.array([abs2(U[i,mode[0]]*U[j,mode[1]]+\
U[i,mode[1]]*U[j,mode[0]]) for i,j in pairs])
  powers /= sum(powers)
  return powers
  
if __name__=='__main__':
  s=(0,5.135)
  b=(0,6.000)
  symmetric_tree,broken_tree=trees(s,b)

### SYMMETRIC
  eta=1
  gamma=0.5*numpy.sqrt(2)*eta
  singles_out=[open("data/threesite/symmetric/experimental/singles{0:d}.dat".\
format(i),'w') for i in range(6)]
  pairs_out=[open("data/threesite/symmetric/experimental/pairs{0:d}{1:d}.dat".\
format(i,j),'w') for i,j in [(0,1),(1,2),(0,2)]]
  fidelities_out=open("data/threesite/symmetric/fidelities.dat",'w')
  for i in range(6):
    singles_out[i].write("# gamma {0:.4f}\n# eta   {1:.4f}\n# t 0 1 2 3 4 5 d0\
 d1 d2 d3 d4 d5\n".format(gamma,eta))
  for i in range(3):
    pairs_out[i].write("# gamma {0:.4f}\n# eta   {1:.4f}\n# t 01 02 03 04 05\
 12 13 14 15 23 24 25 34 35 45 d01 d02 d03 d04 d05 d12 d13 d14 d15 d23 d24 d25\
 d34 d35 d45\n".format(gamma,eta))
  fidelities_out.write("# gamma {0:.4f}\n# eta   {1:.4f}\n# t 0 1 2 3 4 5 01\
 12 02\n".format(gamma,eta))
  singles_fmt="{0:.6f}"
  for i in range(1,13):
    singles_fmt+=" {"+str(i)+":.6f}"
  singles_fmt+="\n"
  pairs_fmt="{0:.6f}"
  for i in range(1,31):
    pairs_fmt+=" {"+str(i)+":.6f}"
  pairs_fmt+="\n"
  fidelities_fmt="{0:.6f}"
  for i in range(1,10):
    fidelities_fmt+=" {"+str(i)+":.6f}"
  fidelities_fmt+="\n"

  for n,t in enumerate(symmetric_tree.points()):
    U,norm=threesitematrix(gamma,eta,t)
    singles,singles_err,pairs,pairs_err=GetData("symmetric",n)
    # Get fidelities
    singles_fidelities=[1-0.5*sum(abs(numpy.array([abs2(U[i,j]) \
for j in range(6)])-singles[i])) for i in range(6)]
    pairs_ideal=[IdealPairs(U,mode) for mode in [(0,1),(1,2),(0,2)]]
    pairs_fidelities=[1-0.5*sum(abs(pairs_ideal[i]-pairs[i])) for i in range(3)]
    fidelities_out.write(fidelities_fmt.format(t,*numpy.append(\
singles_fidelities,pairs_fidelities)))
    # Write experimental data
    for i in range(6):
      singles_out[i].write(singles_fmt.format(t,*numpy.append(singles[i],\
singles_err[i])))
    for i in range(3):
      pairs_out[i].write(pairs_fmt.format(t,*numpy.append(pairs[i],\
pairs_err[i])))

  for i in range(6):
    singles_out[i].close()
  for i in range(3):
    pairs_out[i].close()
  fidelities_out.close()

### BROKEN
  eta=1
  gamma=1.05*numpy.sqrt(2)*eta
  singles_out=[open("data/threesite/broken/experimental/singles{0:d}.dat".\
format(i),'w') for i in range(6)]
  pairs_out=[open("data/threesite/broken/experimental/pairs{0:d}{1:d}.dat".\
format(i,j),'w') for i,j in [(0,1),(1,2),(0,2)]]
  fidelities_out=open("data/threesite/broken/fidelities.dat",'w')
  for i in range(6):
    singles_out[i].write("# gamma {0:.4f}\n# eta   {1:.4f}\n# t 0 1 2 3 4 5 d0\
 d1 d2 d3 d4 d5\n".format(gamma,eta))
  for i in range(3):
    pairs_out[i].write("# gamma {0:.4f}\n# eta   {1:.4f}\n# t 01 02 03 04 05\
 12 13 14 15 23 24 25 34 35 45 d01 d02 d03 d04 d05 d12 d13 d14 d15 d23 d24 d25\
 d34 d35 d45\n".format(gamma,eta))
  fidelities_out.write("# gamma {0:.4f}\n# eta   {1:.4f}\n# t 0 1 2 3 4 5 01\
 12 02\n".format(gamma,eta))
  singles_fmt="{0:.6f}"
  for i in range(1,13):
    singles_fmt+=" {"+str(i)+":.6f}"
  singles_fmt+="\n"
  pairs_fmt="{0:.6f}"
  for i in range(1,31):
    pairs_fmt+=" {"+str(i)+":.6f}"
  pairs_fmt+="\n"
  fidelities_fmt="{0:.6f}"
  for i in range(1,10):
    fidelities_fmt+=" {"+str(i)+":.6f}"
  fidelities_fmt+="\n"

  for n,t in enumerate(broken_tree.points()):
    U,norm=threesitematrix(gamma,eta,t)
    singles,singles_err,pairs,pairs_err=GetData("broken",n)
    # Get fidelities
    singles_fidelities=[1-0.5*sum(abs(numpy.array([abs2(U[i,j]) \
for j in range(6)])-singles[i])) for i in range(6)]
    pairs_ideal=[IdealPairs(U,mode) for mode in [(0,1),(1,2),(0,2)]]
    pairs_fidelities=[1-0.5*sum(abs(pairs_ideal[i]-pairs[i])) for i in range(3)]
    fidelities_out.write(fidelities_fmt.format(t,*numpy.append(\
singles_fidelities,pairs_fidelities)))
    # Wrte experimental data
    for i in range(6):
      singles_out[i].write(singles_fmt.format(t,*numpy.append(singles[i],\
singles_err[i])))
    for i in range(3):
      pairs_out[i].write(pairs_fmt.format(t,*numpy.append(pairs[i],\
pairs_err[i])))

  for i in range(6):
    singles_out[i].close()
  for i in range(3):
    pairs_out[i].close()
  fidelities_out.close()

  f_symmetric=numpy.loadtxt("data/threesite/symmetric/fidelities.dat")
  fout=open("data/threesite/symmetric/fidelities.dat",'a')
  fout.write("\n")
  fout.write("# singles:  {0:.4f}+-{1:.4f}\n".format(\
numpy.mean(f_symmetric[:,1:7]),\
numpy.std(f_symmetric[:,1:7])))
  fout.write("# twofolds: {0:.4f}+-{1:.4f}\n".format(\
numpy.mean(f_symmetric[:,8:11]),\
numpy.std(f_symmetric[:,8:11])))
  fout.close()

  f_broken=numpy.loadtxt("data/threesite/broken/fidelities.dat")
  fout=open("data/threesite/broken/fidelities.dat",'a')
  fout.write("\n")
  fout.write("# singles:  {0:.4f}+-{1:.4f}\n".format(\
numpy.mean(f_broken[:,1:7]),\
numpy.std(f_broken[:,1:7])))
  fout.write("# twofolds: {0:.4f}+-{1:.4f}\n".format(\
numpy.mean(f_broken[:,8:11]),\
numpy.std(f_broken[:,8:11])))
  fout.close()

  

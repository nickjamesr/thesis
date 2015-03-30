#!/usr/bin/python

import numpy
import sys

from matplotlib import pyplot

import scipy.optimize as opt

def getprobs(fname, col=2):
  '''Retrieve probabilities of n-clouded events from the file fname'''
  probs=numpy.loadtxt(fname, usecols=(col,), unpack=True)
  return probs/sum(probs)

def expectation(data,uniform,rate):
  '''Return expectation value for clouding metric'''
  nphotons=len(data)-1
  clicks=numpy.array([numpy.random.poisson(x*rate) for x in data])
  return sum(clicks*weights(nphotons))/sum(clicks)

def weights(p):
  '''Return the correct weights for i out of p photons detected on the left.
Takes the value +1 for fully-clouded and -1 for fully-balanced events'''
  return numpy.array([(4./p)*abs(i-p/2.)-1 for i in range(p+1)])

def histogram(data, nbins=20):
  '''data: list of values to be histogrammed
nbins: desired number of bins (default 20)
Returns 2 arrays: bincenters and (normalised) probability densities'''
  # Set up the parameters for the histogram
  xmin,xmax=min(data),max(data)
  bins=numpy.linspace(xmin,xmax,nbins)
  vals=numpy.zeros(nbins)
  xspan=xmax-xmin
  binwidth=xspan/float(nbins+1)
  xmin-=binwidth/2
  xmax+=binwidth/2
  xspan=xmax-xmin
  incr=1./(binwidth*len(data))
  # Fill the bins
  for x in data:
    vals[int(nbins*(x-xmin)/xspan)]+=incr
  return bins,vals

def bhattacharyya(mu,sigma):
  '''Bhattacharyya distance between two Gaussian distributions. This varies
between zero (disjoint distributions) and one (identical distributions)'''
  return 0.25*numpy.log(0.25*((sigma[0]/sigma[1])**2 + (sigma[1]/sigma[0])**2 +\
2)) + 0.25*(mu[0]-mu[1])**2/(sigma[0]**2+sigma[1]**2)

def gauss(x,mu,sigma):
  return (1/(numpy.sqrt(2*numpy.pi)*sigma))*numpy.exp(-(x-mu)**2/(2*sigma**2))

def exponential(x,amp,dc):
  return amp*numpy.exp(-x/dc)

if __name__=='__main__':
  ntrials=5000
  nbins=50
  clickvals = range(100,1020,20)
  threshold = 0.01

  #for nphotons in (4,5,6,7,8,10,12,14):
  for nphotons in (4,5,6,7):
    p0=(-0.5,0.1)
    nmodes=nphotons**2

    # Open output file
    fout=open("{0:d}x{1:d}scaling.dat".format(nphotons,nmodes),'w')
    fout.write("# {0:d}x{1:d}\n".format(nphotons,nmodes))

    # Open input files (quantum and classical respectively)
    fq="{0:d}x{1:d}quantum.dat".format(nphotons,nmodes)
    fc="{0:d}x{1:d}classical.dat".format(nphotons,nmodes)

    # Read from the files the probabilities of n-clouded events for each of
    # quantum, classical and uniform sampling
    qprobs=getprobs(fq)
    cprobs=getprobs(fc)
    uprobs=getprobs(fq,1)

    # Gradually increase the number of clicks in the simulated experiment
    bvals = []
    for nclicks in clickvals:
      # These arrays will contain a series of <ntrials> values of the clouding
      # metric, for independent simulated experiments with <nclicks> events
      qdata=numpy.empty(ntrials)
      cdata=numpy.empty(ntrials)
      for i in range(ntrials):
        qdata[i]=expectation(qprobs,uprobs,nclicks)
        cdata[i]=expectation(cprobs,uprobs,nclicks)

      # Histogram the data
      qbins,qhist=histogram(qdata,nbins)
      cbins,chist=histogram(cdata,nbins)
      # Find Gaussian fit to the histogram
      qopt,qcov=opt.curve_fit(gauss,qbins,qhist,p0)
      copt,ccov=opt.curve_fit(gauss,cbins,chist,p0)
      # Output the Bhattacharyya distance between the two distributions
      fout.write("{0:d} {1:.4g}\n".format(nclicks,
numpy.exp(-bhattacharyya(*zip(qopt,copt)))))
      bvals.append(numpy.exp(-bhattacharyya(*zip(qopt,copt))))
    fout.close()

    p0=(1,500)
    popt,pcov=opt.curve_fit(exponential, numpy.array(clickvals),
numpy.array(bvals), p0)
    print nphotons, popt[1]*numpy.log(popt[0]/threshold)






#!/usr/bin/python

import numpy

from sys import argv, exit

def expectation(data,uniform,rate):
  nphotons=len(data)-1
  clicks=numpy.array([numpy.random.poisson(x*rate) for x in data])
  return sum(clicks*weights(nphotons))/sum(clicks)

def weights(p):
  '''Return the correct weights for i out of p photons detected on the left.
Takes the value +1 for fully-clouded and -1 for fully-balanced events'''
  return numpy.array([(4./p)*abs(i-p/2.)-1 for i in range(p+1)])

def counts(counting):
  '''Return the weightings to compensate for the number of events expected by
the counting argument. That is, amplify unlikely (clouded events) and penalise
very likely (balanced) events'''
  # I don't use this anymore because it was exponentially suppressing the part
  # of the pdf that differed the most. In fact, I think that's why it looked
  # like it didn't scale.
  norm=sum(1./counting)
  return ((1./counting)/norm)

def getdata(fname, col):
  '''Gets the clouding probabilities from column <col> of the file <fname>
Return array is normalised'''
  data=numpy.loadtxt(fname,usecols=(col,),unpack=True)
  return data/sum(data)

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

if __name__=='__main__':
  qname=argv[1]
  cname=argv[2]
  nclicks=int(argv[3])
  ntrials=50000 # Number of experiments to simulate
  nbins=30

  qdata=getdata(qname,2)
  cdata=getdata(cname,2)
  udata=getdata(qname,1)

  qvals=numpy.zeros(ntrials)
  cvals=numpy.zeros(ntrials)
  uvals=numpy.zeros(ntrials)

  for i in range(ntrials):
    qvals[i]=expectation(qdata,udata,nclicks)
    cvals[i]=expectation(cdata,udata,nclicks)
    uvals[i]=expectation(udata,udata,nclicks)

  qbins,qhist=histogram(qvals,nbins)
  cbins,chist=histogram(cvals,nbins)
  ubins,uhist=histogram(uvals,nbins)

  fout=open("histogram.dat",'w')
  fout.write("# qbins qhist cbins chist ubins uhist\n")
  for i in range(nbins):
    fout.write("{0:.5f} {1:.5f} {2:.5f} {3:.5f} {4:.5f} {5:.5f}\n".format(
qbins[i], qhist[i], cbins[i], chist[i], ubins[i], uhist[i]))
  fout.close()








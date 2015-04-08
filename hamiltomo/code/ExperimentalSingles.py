#!/usr/bin/python
#--------------------------------------------------------------------------#
# ExperimentalSingles.py                                                   #
#                                                                          #
# Take Jacques' CSV files and combine the data into matrices of single     #
# photon (power meter) count rates. Output both the raw (unnormalised)     #
# matrix and the (normalised) matrix of absolutes.                         #
#                                                                          #
# Dependencies:                                                            #
#  * numpy                                                                 #
#                                                                          #
# Output directory:                                                        #
#   data/Singles                                                           #
#                                                                          #
#--------------------------------------------------------------------------#

import numpy

def get_data():
  '''Get the data from Jacques' .csv files
returns 3 matrices: one for each wavelength in (774,776,778)nm'''
  fdir="data/blocking/"
  data774=numpy.zeros((21,21))
  data776=numpy.zeros((21,21))
  data778=numpy.zeros((21,21))

  nfile=0
  for f in ["1_6.csv", "6_11.csv", "11_16.csv", "16_21.csv"]:
    '''Get the data from the csv files'''
    modein=0
    with open(fdir+f, "r") as fin:
      for line in fin:
        p774,p776,p778 =\
[[int(float(x)) for x in line.strip("\"{}\r\n").split("\",\"")[i].strip("{}").\
split(",")] for i in range(3)]
        j=modein
        for i in range(6):
          data774[nfile*5+i,j]+=p774[i]
          data776[nfile*5+i,j]+=p776[i]
          data778[nfile*5+i,j]+=p778[i]
        modein+=1
    nfile+=1

  return data774,data776,data778

def deviation(m):
  '''Calculate how far the matrix m deviates from being normalised.
Normalisation defined by sum of all columns and sum of all rows being equal to
1.
m : matrix of absolute values of a unitary.
returns a floating point number equal to the devation from normalisation'''
  d=0.
  for i in range(21):
    d+=abs(sum(m[:,i])-1.) # Columns
    d+=abs(sum(m[i,:])-1.) # Rows
  return d/42.

def iterate(m):
  '''Perform one iteration of relaxation procedure. This consists of dividing
each row by its sum, then the same for columns.
m : matrix of absolute values of a unitary.'''
  for i in range(21):
    m[:,i]/=sum(m[:,i])
  for i in range(21):
    m[i,:]/=sum(m[i,:])

def relax(m, eps=1e-15, maxiter=100):
  '''Relax the matrix to normalised form by iterative procedure.
m       : matrix of absolute values of a unitary
eps     : tolerance. Return when deviation is less than this.
maxiter : maximum number of iterations to apply. Break and return when this is
          exceeded'''
  d=deviation(m)
  niter=0
  while d>eps and niter<maxiter:
    iterate(m)
    d=deviation(m)
    niter+=1

if __name__=='__main__':
  data774, data776, data778=get_data()

  # Save raw data
  numpy.savetxt("data/Singles/774_raw.dat",data774,fmt='%.5g')
  fout=open("data/Singles/774_raw.dat",'a')
  fout.write("\n# ")
  for i in range(21):
    fout.write("{0:.5g} ".format(sum(data774[:,i])))
  fout.write("\n")
  fout.close()

  numpy.savetxt("data/Singles/776_raw.dat",data776,fmt='%.5g')
  fout=open("data/Singles/776_raw.dat",'a')
  fout.write("\n# ")
  for i in range(21):
    fout.write("{0:.5g} ".format(sum(data776[:,i])))
  fout.write("\n")
  fout.close()

  numpy.savetxt("data/Singles/778_raw.dat",data778,fmt='%.5g')
  fout=open("data/Singles/778_raw.dat",'a')
  fout.write("\n# ")
  for i in range(21):
    fout.write("{0:.5g} ".format(sum(data778[:,i])))
  fout.write("\n")
  fout.close()

  # Normalise matrices
  relax(data774)
  relax(data776)
  relax(data778)
  # Save processed (normalised) data
  numpy.savetxt("data/Singles/774_absolutes.dat", data774, fmt='%+.6f')
  numpy.savetxt("data/Singles/776_absolutes.dat", data776, fmt='%+.6f')
  numpy.savetxt("data/Singles/778_absolutes.dat", data778, fmt='%+.6f')



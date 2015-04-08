#!/usr/bin/python
#--------------------------------------------------------------------------#
# DipSigns.py                                                              #
#                                                                          #
# Plot the dips successively and allow the user to assign +-1 to each of   #
# them according to dip (+1) or antidip (-1). This is enough information   #
# to deduce the sign of the matrix element.                                #
#                                                                          #
# Dependencies:                                                            #
#  * numpy                                                                 #
#  * matplotlib.pyplot                                                     #
#  * sys.argv, sys.exit                                                    #
#                                                                          #
# Output directory:                                                        #
#   same as input directory                                                #
#                                                                          #
#--------------------------------------------------------------------------#

import numpy

from matplotlib import pyplot
from sys import argv, exit

if __name__=='__main__':
  if len(argv)<4:
    print '''Usage
DipSigns.py <wavelength> <refcol> <refrow>
wavelength : wavelength (774,776,778)
refcol     : reference column (8,9)
refrow     : reference row (3,4,6)'''
    exit(0)
  else:
    wavelength=int(argv[1])
    refcol=int(argv[2])
    refrow=int(argv[3])
  columns=range(8,12)
  columns.remove(refcol)
  for col in columns:
    print "\ncolumn {0:02d}".format(col)
    fin="data/{0:d}/Dips/refs{1:02d}{2:02d}_col{3:02d}.csv".format(
wavelength,refcol,refrow,col)
    fout=open("data/{0:d}/Dips/refs{1:02d}{2:02d}_col{3:02d}_signs.dat"\
.format(wavelength,refcol,refrow,col),'w')
    data=numpy.loadtxt(fin,delimiter=',',converters={0: (lambda x:0)})
    labels=numpy.loadtxt(fin,delimiter=',',usecols=(0,),dtype=str)
    ndips=len(data)-1
    signs=numpy.zeros((ndips,),dtype=int)
    x=data[0,1:]
    for i in range(ndips):
      print labels[i+1],
      y=data[i+1,1:]
      s=None
      while s is None:
        pyplot.plot(x,y)
        pyplot.show()
        s=raw_input(">> ")
        if s=="dip" or s=="d":
          signs[i]=+1
        elif s=="anti" or s=="antidip" or s=="a":
          signs[i]=-1
        elif s=="none":
          signs[i]=0
        else:
          s=None
      fout.write("{0:s} {1:d}\n".format(labels[i+1],signs[i]))
    fout.close()
    
    
    

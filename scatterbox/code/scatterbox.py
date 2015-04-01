#!/usr/bin/python

import numpy
import math
import cmath

from sys import argv,exit
from os import path

def abs2(z):
  return (z*z.conjugate()).real

def principal(phi, base=math.pi):
  return phi-2*base*math.floor((phi+base)/(2*base))

def usage():
  print '''scatterbox.py fname
fname  : location of matrix file (4x4 unitary matrix)
output : list of circuit parameters'''

class Circuit:
  def __init__(self):
    self.at0 = 0
    self.at1 = 0
    self.pt1 = 0
    self.pt2 = 0
    self.aq0 = 0
    self.aq1 = 0
    self.aq2 = 0
    self.phase = [0,0,0,0,0,0,0,0]
    self.unitary = numpy.array([[1,0],[0,0],[0,0],[0,1]], dtype=numpy.float64)
    self.update()

  def update(self):
    fullu = self.mat_unitary()
    self.unitary = fullu[:,0:2]

  def fromList(self, at0, at1, pt1, pt2, aq0, aq1, aq2):
    degtorad=math.pi/180.
    self.at0 = at0*degtorad
    self.at1 = at1*degtorad
    self.pt1 = pt1*degtorad
    self.pt2 = pt2*degtorad
    self.aq0 = aq0*degtorad
    self.aq1 = aq1*degtorad
    self.aq2 = aq2*degtorad
    fullu = self.mat_unitary()
    self.unitary = fullu[:,0:2]

  def load(self, fname):
    '''Load a unitary matrix from the file 'filename'. Each line of the file is
  a row in the matrix, and values in the row may be separated by any
  whitespace. Complex numbers must be of the form x+yj'''
    fullu = numpy.loadtxt(fname,dtype=complex)[:,0:2]
    self.fromMatrix(fullu)

  def fromMatrix(self, fullu):
# Real border
    for i in range(4):
      phi = cmath.phase(fullu[i,0])
      fullu[i,0] = fullu[i,0]*numpy.exp(complex(0,-phi))
      fullu[i,1] = fullu[i,1]*numpy.exp(complex(0,-phi))
    phi = cmath.phase(fullu[0,1])
    for i in range(4):
      fullu[i,1] = fullu[i,1]*numpy.exp(complex(0,-phi))
# TODO: orthonormalise the input unitary
# positive phase in 1,1 component
    if cmath.phase(fullu[1,1]) < 0:
      for i in range(4):
        fullu[i,1] = fullu[i,1].conjugate()
    self.unitary = fullu
    #print "Real border:\n", self.unitary
# Find quart amplitudes
    cosaq0 = math.sqrt(abs2(fullu[0,0])+abs2(fullu[1,0]))
    sinaq0 = math.sqrt(abs2(fullu[2,0])+abs2(fullu[3,0]))
    if (cosaq0 != 0):
      cosaq1 = abs(fullu[0,0])/cosaq0
      sinaq1 = abs(fullu[1,0])/cosaq0
    else:
      cosaq1 = 1
      sinaq1 = 0
    if (sinaq0 != 0):
      cosaq2 = abs(fullu[2,0])/sinaq0
      sinaq2 = abs(fullu[3,0])/sinaq0
    else:
      cosaq2 = 1
      sinaq2 = 0
    self.aq0 = 0.5*math.acos(cosaq0)
    self.aq1 = 0.5*math.acos(cosaq1)
    self.aq2 = 0.5*math.acos(cosaq2)
    self.at0 = self.at1 = self.pt1 = self.pt2 = 0
    self.update()
# Reverse aq2
    t2 = fullu[2,1]
    t3 = fullu[3,1]
    fullu[2,1] = cosaq2*t2 + sinaq2*t3
    fullu[3,1] = sinaq2*t2 - cosaq2*t3
# Reverse aq1 (negative because of an output phase of pi that I used to make the
# quart real-bordered)
    t0 = fullu[0,1]
    t1 = fullu[1,1]
    fullu[0,1] = -(cosaq1*t0 + sinaq1*t1)
    fullu[1,1] = -(sinaq1*t0 - cosaq1*t1)
# Reverse aq0
    t0 = fullu[0,1]
    t2 = fullu[2,1]
    fullu[2,1] = cosaq0*t2 + sinaq0*t0
    fullu[0,1] = sinaq0*t2 - cosaq0*t0
# Find trit phases
    delta = 0.5*(cmath.phase(fullu[1,1])+cmath.phase(fullu[3,1]))
    for i in range(1,4):
      fullu[i,1] = fullu[i,1]*numpy.exp(complex(0,-delta))
    if cmath.phase(fullu[1,1]) < 0:
      # take complex conjugate to maintain canonical form
      for i in range(1,4):
        fullu[i,1] = fullu[i,1].conjugate()
    self.pt1 = principal(0.25*cmath.phase(fullu[2,1]),math.pi/4)
    self.pt2 = principal(0.50*cmath.phase(fullu[1,1]),math.pi/2)
    self.pt1 = 0.25*cmath.phase(fullu[2,1])
    self.pt2 = 0.50*cmath.phase(fullu[1,1])
    #if abs(self.pt2) > math.pi/4:
    #  self.pt1 = principal(math.pi/8 + self.pt1, math.pi/4)
    #  self.pt2 = principal(math.pi/4 + self.pt2, math.pi/2)
# Reverse phases
    fullu[1,1] = fullu[1,1]*numpy.exp(complex(0,-2*self.pt2))
    fullu[2,1] = fullu[2,1]*numpy.exp(complex(0,-4*self.pt1))
    fullu[3,1] = fullu[3,1]*numpy.exp(complex(0,+2*self.pt2))
# Find trit amplitudes
    d = math.sqrt(abs2(fullu[3,1])+abs2(fullu[1,1]))
    if (d==0):
      cosat1 = 1
      sinat1 = 0
    else:
      cosat1 = abs(fullu[3,1])/d
      sinat1 = abs(fullu[1,1])/d
    cosat0 = d
    sinat0 = abs(fullu[2,1])
    self.at1 = 0.5*math.acos(cosat1)
    self.at0 = 0.5*math.acos(cosat0)
    self.update()
    if cmath.phase(self.unitary[1,1]) < 0:
      self.pt1 = -self.pt1
      self.pt2 = -self.pt2
    self.update()
# Reverse at1 and at0 (sanity check - should get [0,0,0,1]
    t1 = fullu[1,1]
    t3 = fullu[3,1]
    fullu[3,1] = cosat1*t3 + sinat1*t1
    fullu[1,1] = sinat1*t3 - cosat1*t1
    t2 = fullu[2,1]
    t3 = fullu[3,1]
    fullu[3,1] = cosat0*t3 + sinat0*t2
    fullu[2,1] = sinat0*t3 - cosat0*t2
    #print "Reconstructed:\n", self.unitary

  def amplitudes(self):
    '''Return the counts expected for bosons'''
# Assumes we don't have number resolving detectors
    u = self.unitary
    aa = 2*abs2(u[0,0]*u[0,1])
    ab = abs2(u[0,0]*u[1,1] + u[0,1]*u[1,0])
    ac = abs2(u[0,0]*u[2,1] + u[0,1]*u[2,0])
    ad = abs2(u[0,0]*u[3,1] + u[0,1]*u[3,0])
    bb = 2*abs2(u[1,0]*u[1,1])
    bc = abs2(u[1,0]*u[2,1] + u[1,1]*u[2,0])
    bd = abs2(u[1,0]*u[3,1] + u[1,1]*u[3,0])
    cc = 2*abs2(u[2,0]*u[2,1])
    cd = abs2(u[2,0]*u[3,1] + u[2,1]*u[3,0])
    dd = 2*abs2(u[3,0]*u[3,1])
    a = aa + ab + ac + ad
    b = ab + bb + bc + bd
    c = ac + bc + cc + cd
    d = ad + bd + cd + dd
    singles = [x/sum([a,b,c,d]) for x in [a,b,c,d]]
    coincidences = [ab,ac,ad,bc,bd,cd]
    return (singles, coincidences)

  def amplitudes_classical(self):
    '''Return the counts expected for classical particles'''
    u = self.unitary
    aa = 2*abs2(u[0,0])*abs2(u[0,1])
    ab = abs2(u[0,0])*abs2(u[1,1]) + abs2(u[0,1])*abs2(u[1,0])
    ac = abs2(u[0,0])*abs2(u[2,1]) + abs2(u[0,1])*abs2(u[2,0])
    ad = abs2(u[0,0])*abs2(u[3,1]) + abs2(u[0,1])*abs2(u[3,0])
    bb = 2*abs2(u[1,0])*abs2(u[1,1])
    bc = abs2(u[1,0])*abs2(u[2,1]) + abs2(u[1,1])*abs2(u[2,0])
    bd = abs2(u[1,0])*abs2(u[3,1]) + abs2(u[1,1])*abs2(u[3,0])
    cc = 2*abs2(u[2,0])*abs2(u[2,1])
    cd = abs2(u[2,0])*abs2(u[3,1]) + abs2(u[2,1])*abs2(u[3,0])
    dd = 2*abs2(u[3,0])*abs2(u[3,1])
    a = aa + ab + ac + ad
    b = ab + bb + bc + bd
    c = ac + bc + cc + cd
    d = ad + bd + cd + dd
    singles = [x/sum([a,b,c,d]) for x in [a,b,c,d]]
    coincidences = [ab,ac,ad,bc,bd,cd]
    return (singles, coincidences)

  def dips(self):
    '''Return the visibilities of HOM-type dips'''
    classical = self.amplitudes_classical()[1]
    quantum = self.amplitudes()[1]
    v = [1-quantum[i]/classical[i] for i in range(len(quantum))]
    return v

  def dips_plot(self, fname):
    '''Return the visibilities of HOM-type dips and plot a visualisation of how
    ideal data would look. Data for the plot is stored in the file with the name
    supplied'''
    classical = self.amplitudes_classical()[1]
    quantum = self.amplitudes()[1]
    v = [1-quantum[i]/classical[i] for i in range(len(quantum))]
    fout = open(fname, "w")
    fout.write("x AB AC AD BC BD CD\n")
    for i in range(-40,41):
      x = i/10.
      points = [classical[i] * (1 - v[i]*math.exp(-(x*x))) for i in
          range(len(v))]
      fout.write(str(x) + " ")
      for p in points:
        fout.write(str(p) + " ")
      fout.write("\n")
    fout.close()
    return v

  def params(self):
    '''Return the circuit parameters (in radians) as a list'''
    return [180/math.pi*x for x in [self.at0, self.at1, self.pt1, self.pt2,\
      self.aq0, self.aq1,self.aq2]]

  def singles(self):
    '''Return a list of expected singles counts in each detector'''
    return self.amplitudes()[0]

  def coincidences(self):
    '''Return a list of expected coincidence counts for each pair of
    detectors'''
    return self.amplitudes()[1]

  def scan(self, wp, fname):
    '''Scan over one of the waveplate parameters. Amplitudes data is stored in
    the file <fname>'''
    fout = open(fname, 'w')
    if wp not in ('at0', 'at1', 'pt1', 'pt2', 'aq0', 'aq1', 'aq2'):
      print "invalid component:", wp
      return
    angle = self.get(wp)
    fout.write("angle A B C D AB AC AD BC BD CD\n")
    for i in range(360):
      self.set(wp, i)
      s,c = self.amplitudes()
      fout.write("{0:.4f} {1:.4f} {2:.4f} {3:.4f} {4:.4f} {5:.4f} {6:.4f} \
{7:.4f} {8:.4f} {9:.4f} {10:.4f}\n".format(i, s[0], s[1], s[2], s[3],\
c[0], c[1], c[2], c[3], c[4], c[5]))
    self.set(wp, angle)

# angles in degrees
  def get(self, wp):
    radtodeg = 180/math.pi
    if wp == 'at0':
      return self.at0*radtodeg
    elif wp == 'at1':
      return self.at1*radtodeg
    elif wp == 'pt1':
      return self.pt1*radtodeg
    elif wp == 'pt2':
      return self.pt2*radtodeg
    elif wp == 'aq0':
      return self.aq0*radtodeg
    elif wp == 'aq1':
      return self.aq1*radtodeg
    elif wp == 'aq2':
      return self.aq2*radtodeg
    else:
      print "invalid component:", wp
      return 0

# Set angles in degrees
  def set(self, wp, deg):
    degtorad = math.pi/180
    if wp == 'at0':
      self.at0 = deg*degtorad
    elif wp == 'at1':
      self.at1 = deg*degtorad
    elif wp == 'pt1':
      self.pt1 = deg*degtorad
    elif wp == 'pt2':
      self.pt2 = deg*degtorad
    elif wp == 'aq0':
      self.aq0 = deg*degtorad
    elif wp == 'aq1':
      self.aq1 = deg*degtorad
    elif wp == 'aq2':
      self.aq2 = deg*degtorad
    else:
      print "invalid component:", wp
      return 0
    self.update()

# array functions
  def mat_unitary(self):
    s = [math.sin(2*self.at0), math.sin(2*self.at1), math.sin(2*self.aq0),\
      math.sin(2*self.aq1), math.sin(2*self.aq2)]
    c = [math.cos(2*self.at0), math.cos(2*self.at1), math.cos(2*self.aq0),\
      math.cos(2*self.aq1), math.cos(2*self.aq2)]
    phi = [numpy.exp(complex(0,4*self.pt1)), numpy.exp(complex(0,2*self.pt2)),\
      numpy.exp(complex(0,-2*self.pt2))]

    U = numpy.array([[c[2]*c[3], -phi[0]*s[0]*s[2]*c[3]-phi[1]*c[0]*s[1]*s[3]],\
      [c[2]*s[3], -phi[0]*s[0]*s[2]*s[3]+phi[1]*c[0]*s[1]*c[3]],
      [s[2]*c[4], phi[0]*s[0]*c[2]*c[4]+phi[2]*c[0]*c[1]*s[4]],
      [s[2]*s[4], phi[0]*s[0]*c[2]*s[4]-phi[2]*c[0]*c[1]*c[4]]])

    theta = cmath.phase(U[0,1])
    for i in range(4):
      U[i,1] = U[i,1]*numpy.exp(complex(0,-theta))

    return U

if __name__=='__main__':
  if len(argv)<2:
    usage()
    exit(1)
  if path.exists(argv[1]):
    c=Circuit()
    c.load(argv[1])
    print "at0 : {0:.2f}".format(c.at0*180/math.pi)
    print "at1 : {0:.2f}".format(c.at1*180/math.pi)
    print "aq0 : {0:.2f}".format(c.aq0*180/math.pi)
    print "aq1 : {0:.2f}".format(c.aq1*180/math.pi)
    print "aq2 : {0:.2f}".format(c.aq2*180/math.pi)
    print "pt1 : {0:.2f}".format(c.pt1*180/math.pi)
    print "pt2 : {0:.2f}".format(c.pt2*180/math.pi)
  else:
    usage()
    exit(1)

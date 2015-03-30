#!/usr/bin/python
#--------------------------------------------------------------------------#
# RECONSTRUCT.PY                                                           #
# Reconstruct the (hopefully unitary) transfer matrix from experimental    #
# data                                                                     #
#                                                                          #
# Dependencies:                                                            #
#  * math                                                                  #
#  * cmath                                                                 #
#  * numpy                                                                 #
#  * scipy.optimize                                                        #
#  * matplotlib.pyplot                                                     #
#  * sys.argv                                                              #
#  * pttools.abs2                                                          #
#                                                                          #
# Output directory                                                         #
#    data                                                                  #
#                                                                          #
#--------------------------------------------------------------------------#

import math
import cmath

import numpy as np
import scipy.optimize as opt

from matplotlib import pyplot
from sys import argv
from pttools import abs2

def principal(x, base=math.pi):
  '''Shift an angle to within a standard range
x      : unbounded number
base   : restrict to value in range [-base,base)
return : shifted value'''
  return 2*base*(((x+base)/(2*base))%1)-base

def getEfficiencies(fname):
  '''Get efficiencies for the experimental run in a specified directory
fname  : location of exprimental data
return : (numpy array) detector efficiencies for modes A,B,C,D'''
  names = ["background", "A", "B", "C", "D"]
  counts = []
  for i in range(5):
    fin = open(fname+"/"+names[i]+".txt", 'r')
    counts.append([int(float(x)) for x in fin.readline().strip('[] \n\r').split()])
  counts = np.array(counts)
  adjusted = np.array([counts[i]-counts[0] for i in range(1,5)])
  eta = np.array([counts[1,0]/float(counts[i+1,i]) for i in range(4)])
  return eta

def realBorder(U):
  '''Real-bordered form of a unitary matrix
U      : arbitrary (normally unitary) matrix
return : real-bordered form of U'''
  for i in range(4):
    phi = cmath.phase(U[i,0])
    U[i,0] *= np.exp(complex(0,-phi))
    U[i,1] *= np.exp(complex(0,-phi))
  phi = cmath.phase(U[0,1])
  for i in range(4):
    U[i,1] *= np.exp(complex(0,-phi))
  return U

def visibility(U,i,j):
  '''Calculate the visibility of a dip when photons are injected in the
first two modes and measured in the specified modes
U      : Unitary matrix
i,j    : measured modes
return : visibility'''
  quantum = abs2(U[i,0]*U[j,1] + U[j,0]*U[i,1])
  classical = abs2(U[i,0]*U[j,1]) + abs2(U[j,0]*U[i,1])
  if (classical==0):
    return 0
  else:
    return (classical-quantum)/classical

def dVis(phi, b_exp, v_exp):
  '''Target function for optimization over trit phases
phi    : phases on trit
b_exp  : experimental power ratios (blocking data)
v_exp  : experimental dip visibilities
return : distance from ideal (expected) phases'''
  pairs = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
  v_exp = np.array([v_exp[i,j] for (i,j) in pairs])
  phi = [0,phi[0],phi[1],phi[2]]
  cosines = np.array([math.cos(phi[i]-phi[j]) for (i,j) in pairs])
  b_mod = np.array([b_exp[i,j] for (i,j) in pairs])
  v_mod = -2*cosines/(b_mod + 1.0/b_mod)
  return sum((v_exp-v_mod)**2)

def reconstruct(sym, num, verbose=False):
  '''Reconstruct the unitary from experimental data in a specified
directory.
sym    : symmetry (symmetric, critical, broken)
num    : number of experiment
return : None'''
  fname="../data/"+sym+"/{0:02d}".format(num)
### Get Necessary data from files ###
  dips = np.loadtxt(fname+"/params.dat", usecols=(3,2,1))

  # Info on PT parameters
  with open(fname+"/info.txt",'r') as fin:
    J = float(fin.readline().split()[2])
    gamma = float(fin.readline().split()[2])
    t = float(fin.readline().split()[2])
    norm = float(fin.readline().split()[2])
    

  matrix = np.loadtxt(fname+"/matrix.dat", dtype=complex)[0:4,0:2]
  matrix = realBorder(matrix)
  qin = abs2(matrix[:,0])
  tin = abs2(matrix[:,1])

  singles = np.loadtxt(fname+"/singles.txt")
  quart = singles[0,:]
  quart_err = singles[1,:]
  trit = singles[2,:]
  trit_err = singles[3,:]
### Got data - now start processing ###

  eta = getEfficiencies(fname)

  # Blocking data (loss invariants)
  B_exp = np.sqrt(np.array([[quart[i]*trit[j]/(quart[j]*trit[i])\
      for i in range(4)] for j in range(4)]))

  vis_exp = np.array([[-1,dips[0,0],dips[1,0],dips[2,0]],\
      [dips[0,0],-1,dips[3,0],dips[4,0]],\
      [dips[1,0],dips[3,0],-1,dips[5,0]],\
      [dips[2,0],dips[4,0],dips[5,0],-1]])
  quant_exp = np.array([[-1,dips[0,1],dips[1,1],dips[2,1]],\
      [dips[0,1],-1,dips[3,1],dips[4,1]],\
      [dips[1,1],dips[3,1],-1,dips[5,1]],\
      [dips[2,1],dips[4,1],dips[5,1],-1]])
  class_exp = np.array([[-1,dips[0,2],dips[1,2],dips[2,2]],\
      [dips[0,2],-1,dips[3,2],dips[4,2]],\
      [dips[1,2],dips[3,2],-1,dips[5,2]],\
      [dips[2,2],dips[4,2],dips[5,2],-1]])
  
  cosines_exp = -0.5*vis_exp*(B_exp+1/B_exp)
  # Force cosines into range [-1:1]
  for i in range(4):
    for j in range(4):
      if cosines_exp[i,j] < -1:
        cosines_exp[i,j] = -1
      elif cosines_exp[i,j] > 1:
        cosines_exp[i,j] = 1
  phi_exp = np.array([[math.acos(cosines_exp[i,j]) for i in range(4)] for j in
    range(4)])
  
### Find phases by optimisation (accounting for signs)
  modphi_exp = phi_exp[0,1:4]
  dphi_exp = phi_exp[1,2:4]
  sgn_exp = (1,1)

  phi_ide = np.array([cmath.phase(x) for x in matrix[1:4,1]])
  vis_ide = np.array([[visibility(matrix, i, j) for i in range(4)]\
      for j in range(4)])

  phi_init = [modphi_exp[0], modphi_exp[1], modphi_exp[2]]
  diff = dVis(phi_init, B_exp, vis_exp)
  for sgn in ((1,1),(1,-1),(-1,1),(-1,-1)):
    phi_init = [modphi_exp[0], sgn[0]*modphi_exp[1],\
        sgn[1]*modphi_exp[2]]
    phi_opt = opt.fmin(dVis, phi_init, args=(B_exp, vis_exp), disp=0)
    if dVis(phi_opt, B_exp, vis_exp) < diff:
      diff = dVis(phi_opt, B_exp, vis_exp)
      sgn_exp = sgn
      phi_exp = phi_opt
  phi_exp = principal(phi_exp)
  if phi_exp[0] < 0:
    phi_exp = -phi_exp
  phi_conj = -phi_exp

### Phases done - find reconstructed matrix and complex conjugate ###

  U_recon = np.array([[math.sqrt(quart[0]), math.sqrt(trit[0])],\
      [math.sqrt(quart[1]), math.sqrt(trit[1])*np.exp(complex(0,phi_exp[0]))],\
      [math.sqrt(quart[2]), math.sqrt(trit[2])*np.exp(complex(0,phi_exp[1]))],\
      [math.sqrt(quart[3]), math.sqrt(trit[3])*np.exp(complex(0,phi_exp[2]))]],\
      dtype=complex)
  U_conj = np.array([[math.sqrt(quart[0]), math.sqrt(trit[0])],\
      [math.sqrt(quart[1]), math.sqrt(trit[1])*np.exp(complex(0,phi_conj[0]))],\
      [math.sqrt(quart[2]), math.sqrt(trit[2])*np.exp(complex(0,phi_conj[1]))],\
      [math.sqrt(quart[3]), math.sqrt(trit[3])*\
      np.exp(complex(0,phi_conj[2]))]], dtype=complex)

### Find some fidelities (of the trace distance variety) ###
  qq = np.vdot(U_recon[:,0], matrix[:,0])
  tt = np.vdot(U_recon[:,1], matrix[:,1])
  qt = np.vdot(U_recon[:,1], U_recon[:,0])
  f_recon = abs2(0.5*(qq+tt))
  f_recon_adj = abs2(0.5*(abs(qq)+abs(tt)))

  tt = np.vdot(U_conj[:,1], matrix[:,1])
  qt = np.vdot(U_conj[:,1], U_conj[:,0])
  f_conj = abs2(0.5*(qq+tt))
  f_conj_adj = abs2(0.5*(abs(qq)+abs(tt)))

### Bar chart fidelities ###
  pairs = ((0,1), (0,2), (0,3), (1,2), (1,3), (2,3))
  eps = np.array([eta[i]*eta[j] for (i,j) in pairs])

### Get ideal coincidence rates
  classical_ide = np.array([abs2(matrix[i,0]*matrix[j,1]) +\
      abs2(matrix[j,0]*matrix[i,1]) for (i,j) in pairs])
  quantum_ide = np.array([abs2(matrix[i,0]*matrix[j,1] +\
      matrix[j,0]*matrix[i,1]) for (i,j) in pairs])

### Normalise so sum of 6 non-bunched coincidences equal to 1
  classical_exp = dips[:,1]*eps/sum(dips[:,1]*eps)
  quantum_exp = dips[:,2]*eps/sum(dips[:,2]*eps)

### Get error bars for coincidences
  quantum_err = np.sqrt(dips[:,2])/sum(dips[:,2]*eps)
  classical_err = np.sqrt(dips[:,1])/sum(dips[:,1]*eps)

### Normalise so sum of 10 coincidences equal to 1
  bunchednorm=True
  if bunchednorm:
    classical_exp = classical_exp*sum(classical_ide)
    classical_err = classical_err*sum(classical_ide)
    quantum_exp = quantum_exp*sum(quantum_ide)
    quantum_err = quantum_err*sum(quantum_ide)
  else:
    classical_ide = classical_ide/sum(classical_ide)
    quantum_ide = quantum_ide/sum(quantum_ide)

  # Format string for coincidence data
  fmt=""
  for i in range(0,16):
    fmt += " {"+"{0:d}".format(i)+":.4f}"
  fmt+="\n"
  # Write quantum coincidences
  fout=open("../data/"+sym+"/quantum.dat",'a')
  fout.write(fmt.format(t,J,gamma,norm,*np.append(quantum_exp,quantum_err)))
  fout.close()
  # Write classical coincidences
  fout=open("../data/"+sym+"/classical.dat",'a')
  fout.write(fmt.format(t,J,gamma,norm,*np.append(classical_exp,classical_err)))
  fout.close()

  # Format string for singles data
  fmt=""
  for i in range(0,12):
    fmt += " {"+"{0:d}".format(i)+":.4f}"
  fmt+="\n"
  # Write quart singles
  fout=open("../data/"+sym+"/quart.dat",'a')
  fout.write(fmt.format(t,J,gamma,norm,*np.append(quart,quart_err)))
  fout.close()
  # Write trit singles
  fout=open("../data/"+sym+"/trit.dat",'a')
  fout.write(fmt.format(t,J,gamma,norm,*np.append(trit,trit_err)))
  fout.close()

  if verbose:
    print "Quantum"
    for x,y in zip(quantum_exp, quantum_err):
      print "{0:.4f}+-{1:.4f} ({2:.2f}%)".format(x,y,100*y/x)
    print "Classical"
    for x,y in zip(classical_exp, classical_err):
      print "{0:.4f}+-{1:.4f} ({2:.2f}%)".format(x,y,100*y/x)

  fout=open(fname+"/coincidences.txt", 'w')
  fout.write("# Coincidence data (corrected for efficiencies) for data in \
'"+fname+"'\n")
  fout.write("# Order: Quantum, errors, Classical, errors\n")
  for x in quantum_exp:
    fout.write("{0:.4f} ".format(x))
  fout.write("\n")
  for x in quantum_err:
    fout.write("{0:.4f} ".format(x))
  fout.write("\n")
  for x in classical_exp:
    fout.write("{0:.4f} ".format(x))
  fout.write("\n")
  for x in classical_err:
    fout.write("{0:.4f} ".format(x))
  fout.write("\n")
  fout.close()

  fout = open(fname+"/reconstructed.dat", 'w')
  for i in range(4):
    fout.write("{0:.5f}{1:+.5f}j {2:.5f}{3:+.5f}j\n".format(U_recon[i,0].real,\
        U_recon[i,0].imag, U_recon[i,1].real, U_recon[i,1].imag))
  fout.close()

  f_quart = 1-0.5*sum(abs(quart-qin))
  f_trit = 1-0.5*sum(abs(trit-tin))
  f_class = 1-0.5*sum(abs(classical_ide-classical_exp))
  f_quantum = 1-0.5*sum(abs(quantum_ide-quantum_exp))

  fout = open(fname+"/fidelities.txt", 'w')
  fout.write("#Fidelities for data in '"+fname+"'\n")
  fout.write("# trace (adjusted) quantum classical quart trit\n")
  fout.write("{0:.4f} {1:.4f} {2:.4f} {3:.4f} {4:.4f} {5:.4f}\n".format(\
max(f_conj,f_recon), max(f_conj_adj,f_recon_adj),f_quantum,f_class,f_quart,
f_trit))
  fout.close()

  # Write fidelities
  fout=open("../data/"+sym+"/fidelities.dat",'a')
  fout.write("{0:02d} {1:.4f} {2:.4f} {3:.4f} {4:.4f}\n".format(num,
max(f_conj,f_recon), max(f_conj_adj, f_recon_adj), f_class, f_quantum))
  fout.close()

  if verbose:
    print "fidelities for data in directory \""+fname+"\":"
    print "Trace distance: ", max(f_conj, f_recon)
    print "    ( adjusted: ", max(f_conj_adj, f_recon_adj), ")"
    print "     Classical: ", f_class
    print "       Quantum: ", f_quantum

  quart = np.append(quart, quart_err)
  trit = np.append(trit, trit_err)
  quantum_exp = np.append(quantum_exp, quantum_err)
  classical_exp = np.append(classical_exp, classical_err)

  qin = np.append(qin, [0 for i in range(4)])
  tin = np.append(tin, [0 for i in range(4)])
  quantum_ide = np.append(quantum_ide, [0 for i in range(6)])
  classical_ide = np.append(classical_ide, [0 for i in range(6)])
  
if __name__=='__main__':
  if "-v" in argv:
    verbose=True
  else:
    verbose=False

  # Symmetric matrices
  fout=open("../data/symmetric/fidelities.dat",'w')
  fout.write("# trace (adjusted) classical quantum\n")
  fout.close()
  fout=open("../data/symmetric/quart.dat",'w')
  fout.write("# t J gamma norm A B C D dA dB dC dD\n")
  fout.close()
  fout=open("../data/symmetric/trit.dat",'w')
  fout.write("# t J gamma norm A B C D dA dB dC dD\n")
  fout.close()
  fout=open("../data/symmetric/quantum.dat",'w')
  fout.write("# t J gamma norm AB AC AD BC BD CD dAB dAC dAD dBC dCD\n")
  fout.close()
  fout=open("../data/symmetric/classical.dat",'w')
  fout.write("# t J gamma norm AB AC AD BC BD CD dAB dAC dAD dBC dCD\n")
  fout.close()
  for i in range(1,10):
    reconstruct("symmetric",i,verbose)

  # Critical matrices
  fout=open("../data/critical/fidelities.dat",'w')
  fout.write("# trace (adjusted) classical quantum\n")
  fout.close()
  fout=open("../data/critical/quart.dat",'w')
  fout.write("# t J gamma norm A B C D dA dB dC dD\n")
  fout.close()
  fout=open("../data/critical/trit.dat",'w')
  fout.write("# t J gamma norm A B C D dA dB dC dD\n")
  fout.close()
  fout=open("../data/critical/quantum.dat",'w')
  fout.write("# t J gamma norm AB AC AD BC BD CD dAB dAC dAD dBC dCD\n")
  fout.close()
  fout=open("../data/critical/classical.dat",'w')
  fout.write("# t J gamma norm AB AC AD BC BD CD dAB dAC dAD dBC dCD\n")
  fout.close()
  for i in range(1,10):
    reconstruct("critical",i,verbose)

  # Broken matrices
  fout=open("../data/broken/fidelities.dat",'w')
  fout.write("# trace (adjusted) classical quantum\n")
  fout.close()
  fout=open("../data/broken/quart.dat",'w')
  fout.write("# t J gamma norm A B C D dA dB dC dD\n")
  fout.close()
  fout=open("../data/broken/trit.dat",'w')
  fout.write("# t J gamma norm A B C D dA dB dC dD\n")
  fout.close()
  fout=open("../data/broken/quantum.dat",'w')
  fout.write("# t J gamma norm AB AC AD BC BD CD dAB dAC dAD dBC dCD\n")
  fout.close()
  fout=open("../data/broken/classical.dat",'w')
  fout.write("# t J gamma norm AB AC AD BC BD CD dAB dAC dAD dBC dCD\n")
  fout.close()
  for i in range(1,10):
    reconstruct("broken",i,verbose)



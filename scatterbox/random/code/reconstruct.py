#!/usr/bin/python

import math
import cmath
import sys

import numpy as np
import scipy.optimize as opt

from os import path

sys.path.append("code")
from scatterbox import Circuit

def time(n):
  if (n < 20):
    return (n-1)/3.0
  else:
    return 30+(n-20)/5.0

def abs2(x):
  return abs(x)**2

def principal(x, base=math.pi):
  return 2*base*(((x+base)/(2*base))%1)-base

def getEfficiencies(num):
  path = "data/{0:02}/".format(num)
  names = ["background", "A", "B", "C", "D"]
  counts = []
  for i in range(5):
    fin = open(path+names[i]+".txt", 'r')
    counts.append([int(x) for x in fin.readline().strip('[] \n\r').split()])
  counts = np.array(counts)
  adjusted = np.array([counts[i]-counts[0] for i in range(1,5)])
  eta = np.array([counts[1,0]/float(counts[i+1,i]) for i in range(4)])
  return eta

def realBorder(U):
  for i in range(4):
    phi = cmath.phase(U[i,0])
    U[i,0] *= np.exp(complex(0,-phi))
    U[i,1] *= np.exp(complex(0,-phi))
  phi = cmath.phase(U[0,1])
  for i in range(4):
    U[i,1] *= np.exp(complex(0,-phi))
  return U

def visibility(U,i,j):
  quantum = abs2(U[i,0]*U[j,1] + U[j,0]*U[i,1])
  classical = abs2(U[i,0]*U[j,1]) + abs2(U[j,0]*U[i,1])
  if (classical==0):
    return 0
  else:
    return (classical-quantum)/classical

def dVis(phi, b_exp, v_exp):
  pairs = ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
  v_exp = np.array([v_exp[i,j] for (i,j) in pairs])
  phi = [0,phi[0],phi[1],phi[2]]
  cosines = np.array([math.cos(phi[i]-phi[j]) for (i,j) in pairs])
  b_mod = np.array([b_exp[i,j] for (i,j) in pairs])
  v_mod = -2*cosines/(b_mod + 1.0/b_mod)
  return sum((v_exp-v_mod)**2)

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

def Reconstruct(num, save=True):
### Get Necessary data from files ###
  folder = "data/{0:02}".format(num)
  if not path.exists(folder+"/mat{0:02}.dat".format(num)):
    print "No file for matrix {0:02}".format(num)
    exit(1)
  if not path.exists(folder+"/dip{0:02}.dat".format(num)):
    print "No dip for matrix {0:02}".format(num)
    exit(1)
  if not (path.exists(folder+"/A.txt") and path.exists(folder+"/C.txt") and \
path.exists(folder+"/B.txt") and path.exists(folder+"/D.txt") and \
path.exists(folder+"/background.txt")):
    print "No efficiency data for matrix {0:02}".format(num)
    exit(1)
  if not path.exists(folder+"/params{0:02}.dat".format(num)):
    fittie = Fittie(num)
    fittie.main()
  dips = np.loadtxt(folder+"/params{0:02}.dat".format(num))

  matrix = np.loadtxt(folder+"/mat{0:02}.dat".format(num),\
      dtype=complex)[0:4,0:2]
  matrix = realBorder(matrix)
  qin = abs2(matrix[:,0])
  tin = abs2(matrix[:,1])

  blocking = np.loadtxt(folder+"/dip{0:02}.dat".format(num),\
      usecols=(1,2,3,4))[0:6]
  background = blocking[0,:]
  quart = blocking[2,:]-background
  trit = blocking[4,:]-background
  for i in range(4):
    quart[i] = max(1,quart[i])
    trit[i] = max(1,trit[i])
### Got data - now start processing ###

  eta = getEfficiencies(num)

  # Adjust quart and trit for efficiencies and normalise to 1
  quart_err = np.sqrt(quart)
  trit_err = np.sqrt(trit)
  quart_err = quart_err*eta/sum(quart*eta)
  quart = quart*eta/sum(quart*eta)
  trit_err = trit_err*eta/sum(trit*eta)
  trit = trit*eta/sum(trit*eta)

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

### Get error bars for coincidences
  quantum_err = np.sqrt(dips[:,2])/sum(dips[:,2]*eps)
  classical_err = np.sqrt(dips[:,1])/sum(dips[:,1]*eps)

### Normalise so sum of 6 coincidences equal to 1
  classical_ide = np.array([abs2(matrix[i,0]*matrix[j,1]) +\
      abs2(matrix[j,0]*matrix[i,1]) for (i,j) in pairs])
  classical_ide = classical_ide/sum(classical_ide)
  classical_exp = dips[:,1]*eps/sum(dips[:,1]*eps)

  quantum_ide = np.array([abs2(matrix[i,0]*matrix[j,1] +\
      matrix[j,0]*matrix[i,1]) for (i,j) in pairs])
  quantum_ide = quantum_ide/sum(quantum_ide)
  quantum_exp = dips[:,2]*eps/sum(dips[:,2]*eps)

### Write reconstructed matrix
  fout = open("data/{0:02}/reconstructed{0:02}.dat".format(num), 'w')
  for i in range(4):
    fout.write("{0:.5f}{1:+.5f}j {2:.5f}{3:+.5f}j\n".format(U_recon[i,0].real,\
        U_recon[i,0].imag, U_recon[i,1].real, U_recon[i,1].imag))
  fout.close()

  f_quart = 1-0.5*sum(abs(quart-qin))
  f_trit = 1-0.5*sum(abs(trit-tin))
  f_class = 1-0.5*sum(abs(classical_ide-classical_exp))
  f_quantum = 1-0.5*sum(abs(quantum_ide-quantum_exp))

  fout=open("data/fidelities.dat",'a')
  fout.write("{0:02d} {1:.5f} {2:.5f} {3:.5f} {4:.5f} {5:.5f}\n".format(\
num, max(f_conj_adj, f_recon_adj), f_class, f_quantum, f_quart, f_trit))
  fout.close()

  quart = np.append(quart, quart_err)
  trit = np.append(trit, trit_err)
  quantum_exp = np.append(quantum_exp, quantum_err)
  classical_exp = np.append(classical_exp, classical_err)

  qin = list(qin)
  tin = list(tin)
  quantum_ide = list(quantum_ide)
  classical_ide = list(classical_ide)

  quantum_dialling,classical_dialling,quart_dialling,trit_dialling=\
 DiallingErrors(matrix,5000)

  if save:
### Experimental
    fstring = "{0:02d} "
    for i in range(1,9):
      fstring += "{" + str(i) + ":.4f} "
    fstring += "\n"
  # Quart
    fout = open("data/quart_experimental.dat", 'a')
    fout.write(fstring.format(num, *quart))
    fout.close()
  # Trit
    fout = open("data/trit_experimental.dat", 'a')
    fout.write(fstring.format(num, *trit))
    fout.close()

### Ideal
    fstring = "{0:02d} "
    for i in range(1,13):
      fstring += "{" + str(i) + ":.4f} "
    fstring += "\n"
  # Quart
    fout = open("data/quart_ideal.dat", 'a')
    fout.write(fstring.format(num,\
 *(qin+[x for y in quart_dialling for x in y])))
    fout.close()
  # Trit 
    fout = open("data/trit_ideal.dat", 'a')
    fout.write(fstring.format(num,\
 *(tin+[x for y in trit_dialling for x in y])))
    fout.close()

### Experimental
    fstring = "{0:02d} "
    for i in range(1,13):
      fstring += "{" + str(i) + ":.4f} "
    fstring += "\n"
  # Quantum
    fout = open("data/quantum_experimental.dat", 'a')
    fout.write(fstring.format(num, *quantum_exp))
    fout.close()
  # Classical
    fout = open("data/classical_experimental.dat", 'a')
    fout.write(fstring.format((num), *classical_exp))
    fout.close()
### Ideal
    fstring = "{0:02d} "
    for i in range(1,19):
      fstring += "{" + str(i) + ":.4f} "
    fstring += "\n"
    fout = open("data/quantum_ideal.dat", 'a')
    fout.write(fstring.format((num),\
 *(quantum_ide+[x for y in quantum_dialling for x in y])))
    fout.close()
  # Classical
    fout = open("data/classical_ideal.dat", 'a')
    fout.write(fstring.format((num),\
 *(classical_ide+[x for y in classical_dialling for x in y])))
    fout.close()

if __name__=='__main__':
  # Write file headers
  # Fidelities
  fout=open("data/fidelities.dat",'w')
  fout.write("# trace classical quantum quart trit\n")
  fout.close()
  # quart ideal
  fout=open("data/quart_ideal.dat",'w')
  fout.write("# A B C D A(-) A(+) B(-) B(+) C(-) C(+) D(-) D(+)\n")
  fout.close()
  # quart experimental
  fout=open("data/quart_experimental.dat",'w')
  fout.write("# A B C D dA dB dC dD\n")
  fout.close()
  # trit ideal
  fout=open("data/trit_ideal.dat",'w')
  fout.write("# A B C D A(-) A(+) B(-) B(+) C(-) C(+) D(-) D(+)\n")
  fout.close()
  # trit experimental
  fout=open("data/trit_experimental.dat",'w')
  fout.write("# A B C D dA dB dC dD\n")
  fout.close()
  # quantum ideal
  fout=open("data/quantum_ideal.dat",'w')
  fout.write("# AB AC AD BC BD CD AB(-) AB(+) AC(-) AC(+) AD(-) AD(+) BC(-)\
 BC(+) BD(-) BD(+) CD(-) CD(+)\n")
  fout.close()
  # quantum experimental
  fout=open("data/quantum_experimental.dat",'w')
  fout.write("# AB AC AD BC BD CD dAB dAC dAD dBC dBD dCD\n")
  fout.close()
  # classical ideal
  fout=open("data/classical_ideal.dat",'w')
  fout.write("# AB AC AD BC BD CD AB(-) AB(+) AC(-) AC(+) AD(-) AD(+) BC(-)\
 BC(+) BD(-) BD(+) CD(-) CD(+)\n")
  fout.close()
  # classical experimental
  fout=open("data/classical_experimental.dat",'w')
  fout.write("# AB AC AD BC BD CD dAB dAC dAD dBC dBD dCD\n")
  fout.close()
  for num in range(12):
    Reconstruct(num)

  # For a single file (0 iteration), produce the data for actually plotting
  num=0 

  # Singles
  qex=np.loadtxt("data/quart_experimental.dat")
  qth=np.loadtxt("data/quart_ideal.dat")
  tex=np.loadtxt("data/trit_experimental.dat")
  tth=np.loadtxt("data/trit_ideal.dat")

  fout=open("data/example_quart.dat",'w')
  fout.write("# th(-) th(=) th(+) ex(=) ex(+-)\n")
  for i in range(4):
    fout.write("{0:d} {1:.4f} {2:.4f} {3:.4f} {4:.4f} {5:.4f}\n".format(i,\
 qth[num,5+2*i],qth[num,1+i],qth[num,6+2*i],qex[num,1+i],qex[num,5+i]))
  fout.close()
  fout=open("data/example_trit.dat",'w')
  fout.write("# th(-) th(=) th(+) ex(=) ex(+-)\n")
  for i in range(4):
    fout.write("{0:d} {1:.4f} {2:.4f} {3:.4f} {4:.4f} {5:.4f}\n".format(i,\
 tth[num,5+2*i],tth[num,1+i],tth[num,6+2*i],tex[num,1+i],tex[num,5+i]))
  fout.close()

  # Coincidences
  qex=np.loadtxt("data/quantum_experimental.dat")
  qth=np.loadtxt("data/quantum_ideal.dat")
  cex=np.loadtxt("data/classical_experimental.dat")
  cth=np.loadtxt("data/classical_ideal.dat")

  fout=open("data/example_quantum.dat",'w')
  fout.write("# th(-) th(=) th(+) ex(=) ex(+-)\n")
  for i in range(6):
    fout.write("{0:d} {1:.4f} {2:.4f} {3:.4f} {4:.4f} {5:.4f}\n".format(i,\
 qth[num,7+2*i],qth[num,1+i],qth[num,8+2*i],qex[num,1+i],qex[num,7+i]))
  fout.close()
  fout=open("data/example_classical.dat",'w')
  fout.write("# th(-) th(=) th(+) ex(=) ex(+-)\n")
  for i in range(6):
    fout.write("{0:d} {1:.4f} {2:.4f} {3:.4f} {4:.4f} {5:.4f}\n".format(i,\
 cth[num,7+2*i],cth[num,1+i],cth[num,8+2*i],cex[num,1+i],cex[num,7+i]))
  fout.close()

  # Summarise the fidelities
  f=np.loadtxt("data/fidelities.dat")
  with open("data/fidelities.dat",'a') as fout:
    fout.write("\n\n# Means :")
    for i in range(1,6):
      fout.write(" {0:.5f}".format(np.mean(f[:,i])))
    fout.write("\n# Stdev :")
    for i in range(1,6):
      fout.write(" {0:.5f}".format(np.std(f[:,i])))

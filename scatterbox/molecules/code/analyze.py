#!/usr/bin/python

from sys import argv, exit

import numpy

def GetEfficiencies(root):
  labels=["A","B","C","D"]
  fin=open(root+"/background.txt")
  bg=[float(x) for x in fin.readline().strip("[] \n\r").split()]
  fin.close()
  singles=[]
  for i in range(4):
    fin=open(root+"/"+labels[i]+".txt")
    singles.append([float(x) for x in fin.readline().strip("[] \n\r").\
      split()][i]-bg[i])
    fin.close()
  eta = [x/float(singles[0]) for x in singles]
  pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
  eps = [eta[i]*eta[j] for i,j in pairs]
  return eta,eps

def GetSingles(root):
  eta,eps=GetEfficiencies(root)
  fin = open(root+"/singles.txt")
  for i in range(8):
    fin.readline()      # skip lines at the top that I don't need
  # Get the raw counts
  qa=[float(x) for x in fin.readline().strip("# \n\r").split()]
  qd=[float(x) for x in fin.readline().strip("# \n\r").split()]
  td=[float(x) for x in fin.readline().strip("# \n\r").split()]
  ta=[float(x) for x in fin.readline().strip("# \n\r").split()]
  qa=[0,qa[0],qa[4],qa[1]]
  ta=[0,ta[0],ta[4],ta[1]]
  qd=[qd[1],qd[5],qd[3],0]
  td=[td[1],td[5],td[3],0]
  qr=(qa[1]+qa[2])/(qd[1]+qd[2])
  tr=(ta[1]+ta[2])/(td[1]+td[2])
  for i in range(4):
    qd[i]*=qr
    td[i]*=tr
  quart=[qd[0],0.5*(qa[1]+qd[1]),0.5*(qa[2]+qd[2]),qa[3]]
  trit=[td[0],0.5*(ta[1]+td[1]),0.5*(ta[2]+td[2]),ta[3]]
  # Get (Poissonian) errors
  qerrs=[numpy.sqrt(x) for x in quart]
  terrs=[numpy.sqrt(x) for x in trit]
  qerrs[1]/=numpy.sqrt(2)
  qerrs[2]/=numpy.sqrt(2)
  terrs[1]/=numpy.sqrt(2)
  terrs[2]/=numpy.sqrt(2)
  # Apply efficiencies
  for i in range(4):
    quart[i]/=eta[i]
    trit[i]/=eta[i]
    qerrs[i]/=eta[i]
    terrs[i]/=eta[i]
  # Normalise to 1
  normq=sum(quart)
  normt=sum(trit)
  for i in range(4):
    quart[i]/=normq
    qerrs[i]/=normq
    trit[i]/=normt
    terrs[i]/=normt
  return quart,trit,qerrs,terrs

def IdealSingles(root):
  u=numpy.loadtxt(root+"/matrix.dat",dtype=complex)
  quart=abs(u[:,0])**2
  trit=abs(u[:,1])**2
  return quart,trit

def IdealPairs(root):
  u=numpy.loadtxt(root+"/matrix.dat", dtype=complex)
  pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
  quantum=numpy.array([abs(u[i,0]*u[j,1]+u[j,0]*u[i,1])**2 for i,j in pairs])
  classical=numpy.array([abs(u[i,0]*u[j,1])**2+abs(u[j,0]*u[i,1])**2\
for i,j in pairs])
  return quantum/sum(quantum),classical/sum(classical)

def TraceDistance(root):
  u=numpy.loadtxt(root+"/matrix.dat", dtype=complex)
  r=numpy.loadtxt(root+"/reconstructed.dat", dtype=complex)
  # Calculate real#bordered unitary
  for i in range(4):
    z=u[0,i]
    phi=z.conjugate()/abs(z)
    for j in range(4):
      u[j,i]*=phi
  for i in range(1,4):
    z=u[i,0]
    phi=z.conjugate()/abs(z)
    for j in range(4):
      u[i,j]*=phi
  u=u[:,0:2]
  return max(abs(sum([0.5*numpy.dot(u.conjugate().T, r)[i,i]\
for i in range(2)])),\
  abs(sum([0.5*numpy.dot(u.T, r)[i,i] for i in range(2)])))

def GetPairs(root):
  eta,eps=GetEfficiencies(root)
  qpairs=[]; cpairs=[]; qerrs=[]; cerrs=[]
  fin=open(root+"/params.dat")
  fin.readline()
  for i in range(6):
    q,c=[float(x) for x in fin.readline().strip().split()[1:3]]
    qpairs.append(q)
    cpairs.append(c)
    qerrs.append(numpy.sqrt(q))
    cerrs.append(numpy.sqrt(c))
  fin.close()
  # Correct for measured efficiencies
  for i in range(6):
    qpairs[i]/=eps[i]
    cpairs[i]/=eps[i]
    qerrs[i]/=eps[i]
    cerrs[i]/=eps[i]
  # Normalise so collision-free pairs sum to 1
  normq=sum(qpairs)
  normc=sum(cpairs)
  for i in range(6):
    qpairs[i]/=normq
    qerrs[i]/=normq
    cpairs[i]/=normc
    cerrs[i]/=normc
  return qpairs,cpairs,qerrs,cerrs

if __name__=='__main__':

  ###########
  ### OCS ###
  ###########
  t=0
  tstep=0.0005
  # Open files
  qout=open("../data/OCS/quantum.dat",'w')
  cout=open("../data/OCS/classical.dat",'w')
  fout=open("../data/OCS/quart.dat",'w')
  tout=open("../data/OCS/trit.dat",'w')
  # Write headers
  qout.write("# AB AC AD BC BD CD dAB dAC dAD dBC dBD dCD\n")
  cout.write("# AB AC AD BC BD CD dAB dAC dAD dBC dBD dCD\n")
  fout.write("# A B C D dA dB dC dD\n")
  tout.write("# A B C D dA dB dC dD\n")
  sfmt=""
  pfmt=""
  for i in range(9):
    sfmt+=("{"+str(i)+":.4g} ")
  for i in range(13):
    pfmt+=("{"+str(i)+":.4g} ")
  sfmt+="\n"
  pfmt+="\n"
  names=["../data/OCS/ocs{0:02d}".format(i) for i in range(21)]
  f_trace=[]
  f_quant=[]
  f_class=[]
  f_quart=[]
  f_trit= []
  for root in names:
    efficiencies=GetEfficiencies(root)
    qpairs,cpairs,dquant,dclass=GetPairs(root)
    quart,trit,dquart,dtrit=GetSingles(root)
    idealquantum, idealclassical=IdealPairs(root)
    idealquart, idealtrit=IdealSingles(root)
    qout.write(pfmt.format(t,*(qpairs+dquant)))
    cout.write(pfmt.format(t,*(cpairs+dclass)))
    fout.write(sfmt.format(t,*(quart+dquart)))
    tout.write(sfmt.format(t,*(trit+dtrit)))
    f_trace.append(TraceDistance(root))
    f_quant.append(1-0.5*sum(abs(qpairs-idealquantum)))
    f_class.append(1-0.5*sum(abs(cpairs-idealclassical)))
    f_quart.append(1-0.5*sum(abs(quart-idealquart)))
    f_trit.append(1-0.5*sum(abs(trit-idealtrit)))
    t+=tstep
  qout.close()
  cout.close()
  fout.close()
  tout.close()

  fout=open("../data/fidelities.dat", 'w')
  fout.write("# tracedistance quantum classical quart trit\n# OCS\n")
  for i,t,q,c,quart,trit in zip(range(len(f_trace)), f_trace, f_quant, f_class,\
f_quart,f_trit):
    fout.write("{0:02d} {1:.4f} {2:.4f} {3:.4f} {4:.4f} {5:.4f}\n".format(\
i,t,q,c,quart,trit))
  fout.write("mean+-stdev {0:.3f}+-{1:.3f} {2:.3f}+-{3:.3f} \
{4:.3f}+-{5:.3f} {6:.3f}+-{7:.3f} {8:.3f}+-{9:.3f}\n\n".format(\
numpy.mean(f_trace), numpy.std(f_trace), numpy.mean(f_quant),\
numpy.std(f_quant), numpy.mean(f_class), numpy.std(f_class),\
numpy.mean(f_quart), numpy.std(f_quart), numpy.mean(f_trit),\
numpy.std(f_trit)))
  fout.close()

  ###########
  ### CO2 ###
  ###########
  t=0
  tstep=0.0005
  # Open files
  qout=open("../data/CO2/quantum.dat",'w')
  cout=open("../data/CO2/classical.dat",'w')
  fout=open("../data/CO2/quart.dat",'w')
  tout=open("../data/CO2/trit.dat",'w')
  # Write headers
  qout.write("# AB AC AD BC BD CD dAB dAC dAD dBC dBD dCD\n")
  cout.write("# AB AC AD BC BD CD dAB dAC dAD dBC dBD dCD\n")
  fout.write("# A B C D dA dB dC dD\n")
  tout.write("# A B C D dA dB dC dD\n")
  sfmt=""
  pfmt=""
  for i in range(9):
    sfmt+=("{"+str(i)+":.4g} ")
  for i in range(13):
    pfmt+=("{"+str(i)+":.4g} ")
  sfmt+="\n"
  pfmt+="\n"
  names=["../data/CO2/co2_{0:02d}".format(i) for i in range(1,22)]
  f_trace=[]
  f_quant=[]
  f_class=[]
  f_quart=[]
  f_trit= []
  for root in names:
    efficiencies=GetEfficiencies(root)
    qpairs,cpairs,dquant,dclass=GetPairs(root)
    quart,trit,dquart,dtrit=GetSingles(root)
    idealquantum, idealclassical=IdealPairs(root)
    idealquart, idealtrit=IdealSingles(root)
    qout.write(pfmt.format(t,*(qpairs+dquant)))
    cout.write(pfmt.format(t,*(cpairs+dclass)))
    fout.write(sfmt.format(t,*(quart+dquart)))
    tout.write(sfmt.format(t,*(trit+dtrit)))
    f_trace.append(TraceDistance(root))
    f_quant.append(1-0.5*sum(abs(qpairs-idealquantum)))
    f_class.append(1-0.5*sum(abs(cpairs-idealclassical)))
    f_quart.append(1-0.5*sum(abs(quart-idealquart)))
    f_trit.append(1-0.5*sum(abs(trit-idealtrit)))
    t+=tstep
  qout.close()
  cout.close()
  fout.close()
  tout.close()

  fout=open("../data/fidelities.dat", 'a')
  fout.write("# tracedistance quantum classical quart trit\n# CO2\n")
  for i,t,q,c,quart,trit in zip(range(len(f_trace)), f_trace, f_quant, f_class,\
f_quart,f_trit):
    fout.write("{0:02d} {1:.4f} {2:.4f} {3:.4f} {4:.4f} {5:.4f}\n".format(\
i,t,q,c,quart,trit))
  fout.write("mean+-stdev {0:.3f}+-{1:.3f} {2:.3f}+-{3:.3f} \
{4:.3f}+-{5:.3f} {6:.3f}+-{7:.3f} {8:.3f}+-{9:.3f}\n\n".format(\
numpy.mean(f_trace), numpy.std(f_trace), numpy.mean(f_quant),\
numpy.std(f_quant), numpy.mean(f_class), numpy.std(f_class),\
numpy.mean(f_quart), numpy.std(f_quart), numpy.mean(f_trit),\
numpy.std(f_trit)))
  fout.close()





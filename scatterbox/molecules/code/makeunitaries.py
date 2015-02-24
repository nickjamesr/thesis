#!/usr/bin/python

import numpy

def RealBorder(M):
  '''pre- and post-multiply M by a diagonal matrix of phases to make
the border elements real.
M      : complex matrix
return : equavalent matrix with real border elements'''
  nrows,ncols=M.shape
  for i in range(nrows):
    phi=(M[i,1]/abs(M[i,1])).conjugate()
    M[i,:]*=phi
  for j in range(ncols):
    phi=(M[0,j]/abs(M[0,j])).conjugate()
    M[:,j]*=phi
  return M

def GetPairs(u):
  #pairs=[(1,3),(1,0),(1,2),(3,0),(3,2),(0,2)]  ## With permutation applied
  pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
  quantum=numpy.array([abs(u[i,0]*u[j,1]+u[i,1]*u[j,0])**2 for i,j in pairs])
  classical=numpy.array([abs(u[i,0]*u[j,1])**2 + abs(u[i,1]*u[j,0])**2 \
for i,j in pairs])
  return quantum/sum(quantum), classical/sum(classical)

def GetSingles(u):
  #quart=numpy.array([abs(u[i,0])**2 for i in (1,3,0,2)])
  #trit=numpy.array([abs(u[i,1])**2 for i in (1,3,0,2)])
  quart=numpy.array([abs(x)**2 for x in u[:,0]])
  trit=numpy.array([abs(x)**2 for x in u[:,1]])
  return quart,trit

if __name__=='__main__':
  # Define OCS and CO2 energy levels
  ocslevels=[520.,520.,859.,2062.]
  co2levels=[667.,667.,1388.,2349.]

  # get preparation and measurement matrices
  prep = numpy.loadtxt("../data/prep.dat", dtype=complex)
  meas = numpy.loadtxt("../data/meas.dat", dtype=complex)
  diag = numpy.zeros((4,4), dtype=complex)

  k=0
  # Write the OCS matrices
  for t in numpy.linspace(0,0.01,21):
    fname = "../data/OCS/ocs{0:02d}/matrix.dat".format(k)
    fout = open(fname, 'w')
    for i,x in zip(range(4),ocslevels):
      diag[i,i]=numpy.exp(-1.0j*x*t)
    unitary = numpy.dot(meas, numpy.dot(diag, prep))
    
    for i in range(4):
      for j in [1,3,0,2]:
        z = unitary[i,j]
        fout.write("{0:+.4f}{1:+.4f}j ".format(z.real,z.imag))
      fout.write("\n")
    fout.close()
    k+=1

  k=1
  # Write the CO2 matrices
  for t in numpy.linspace(0,0.01,21):
    fname = "../data/CO2/co2_{0:02d}/matrix.dat".format(k)
    fout = open(fname, 'w')
    for i,x in zip(range(4),co2levels):
      diag[i,i]=numpy.exp(-1.0j*x*t)
    unitary = RealBorder(numpy.dot(meas, numpy.dot(diag, prep)))
    
    for i in range(4):
      for j in [1,3,0,2]:
        z = unitary[i,j]
        fout.write("{0:+.4f}{1:+.4f}j ".format(z.real,z.imag))
      fout.write("\n")
    fout.close()
    k+=1

  # Output theoretical curves (much closer points)
  # OCS
  fquart=open("../data/OCS/quart_ideal.dat", 'w')
  ftrit=open("../data/OCS/trit_ideal.dat", 'w')
  fquantum=open("../data/OCS/quantum_ideal.dat", 'w')
  fclassical=open("../data/OCS/classical_ideal.dat", 'w')

  fquart.write("# A B C D\n")
  ftrit.write("# A B C D\n")
  fquantum.write("# AB AC AD BC BD CD\n")
  fclassical.write("# AB AC AD BC BD CD\n")

  sfmt=""
  pfmt=""
  for i in range(5):
    sfmt+=("{"+str(i)+":.4g} ")
  for i in range(7):
    pfmt+=("{"+str(i)+":.4g} ")
  sfmt+="\n"
  pfmt+="\n"

  for t in numpy.linspace(0,0.01,201):
  #for t in (0,):
    for i,x in zip(range(4),ocslevels):
      diag[i,i]=numpy.exp(-1.0j*x*t)
    unitary=numpy.dot(meas, numpy.dot(diag, prep))
    permuted=numpy.array([[unitary[i,j] for j in (1,3,0,2)] for i in range(4)])
    quart,trit=GetSingles(permuted)
    quantum,classical=GetPairs(permuted)
    fquart.write(sfmt.format(t,*quart))
    ftrit.write(sfmt.format(t,*trit))
    fquantum.write(pfmt.format(t,*quantum))
    fclassical.write(pfmt.format(t,*classical))

  fquart.close()
  ftrit.close()
  fquantum.close()
  fclassical.close()

  # Output theoretical curves (much closer points)
  # CO2
  fquart=open("../data/CO2/quart_ideal.dat", 'w')
  ftrit=open("../data/CO2/trit_ideal.dat", 'w')
  fquantum=open("../data/CO2/quantum_ideal.dat", 'w')
  fclassical=open("../data/CO2/classical_ideal.dat", 'w')

  fquart.write("# A B C D\n")
  ftrit.write("# A B C D\n")
  fquantum.write("# AB AC AD BC BD CD\n")
  fclassical.write("# AB AC AD BC BD CD\n")

  sfmt=""
  pfmt=""
  for i in range(5):
    sfmt+=("{"+str(i)+":.4g} ")
  for i in range(7):
    pfmt+=("{"+str(i)+":.4g} ")
  sfmt+="\n"
  pfmt+="\n"

  for t in numpy.linspace(0,0.01,201):
    for i,x in zip(range(4),co2levels):
      diag[i,i]=numpy.exp(-1.0j*x*t)
    unitary=numpy.dot(meas, numpy.dot(diag, prep))
    permuted=numpy.array([[unitary[i,j] for j in (1,3,0,2)] for i in range(4)])
    quart,trit=GetSingles(permuted)
    quantum,classical=GetPairs(permuted)
    fquart.write(sfmt.format(t,*quart))
    ftrit.write(sfmt.format(t,*trit))
    fquantum.write(pfmt.format(t,*quantum))
    fclassical.write(pfmt.format(t,*classical))

  fquart.close()
  ftrit.close()
  fquantum.close()
  fclassical.close()


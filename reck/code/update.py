#!/usr/bin/python

from sys import exit

def ternary(l):
  '''Get the ternary number corresponding to the list of ints l'''
  t=0
  l.reverse()
  for i,x in enumerate(l):
    t+=x*3**i
  return t

if __name__=='__main__':
  # Get probability distributions
  datdir="../data"
  dist_quant=[0 for i in range(3**6)]
  dist_class=[0 for i in range(3**6)]

  fin=open(datdir+"/quantum_fock_prob_corrected.csv",'r') # corrected
  for event in fin:
    pattern=[int(x.strip("{}\"")) for x in event.split(',')[:6]]
    prob=float(event.split(',')[6].strip())
    dist_quant[ternary(pattern)]=prob
  fin.close()

  fin=open(datdir+"/classical_fock_prob_corrected.csv",'r') # corrected
  for event in fin:
    pattern=[int(x.strip("{}\"")) for x in event.split(',')[:6]]
    prob=float(event.split(',')[6].strip())
    dist_class[ternary(pattern)]=prob
  fin.close()

  dist_quant=[x/sum(dist_quant) for x in dist_quant]
  dist_class=[x/sum(dist_class) for x in dist_class]

  print sum(dist_quant)
  print sum(dist_class)

  # Update on quantum events
  fout=open(datdir+"/quantum_events.dat",'w')
  fout.write("# Quantum\n")
  print "Quantum"
  fout.write("0.5 0.5\n")
  p_class=p_quant=0.5
  fin=open(datdir+"/quant_exp.csv",'r')
  for event in fin:
    # Do the updating step
    pattern=[int(x.strip("{}\"")) for x in event.split(',')[:6]]
    idx=ternary(pattern)
    print "{0:.6f} {1:.6f}".format(dist_quant[idx],dist_class[idx]),\
dist_quant[idx]>dist_class[idx]
    p_event=dist_quant[idx]*p_quant+dist_class[idx]*p_class
    p_quant*=dist_quant[idx]/p_event
    p_class*=dist_class[idx]/p_event
    fout.write("{0:.5g} {1:.5g}\n".format(p_quant, p_class))
  fin.close()
  fout.close()


  # Update on classical events
  fout=open(datdir+"/classical_events.dat",'w')
  fout.write("# Classical\n")
  print "\n\nClassical"
  fout.write("0.5 0.5\n")
  p_class=p_quant=0.5
  fin=open(datdir+"/class_exp.csv",'r')
  for event in fin:
    # Do the updating step
    pattern=[int(x.strip("{}\"")) for x in event.split(',')[:6]]
    idx=ternary(pattern)
    print "{0:.6f} {1:.6f}".format(dist_quant[idx],dist_class[idx]),\
dist_quant[idx]<dist_class[idx]
    p_event=dist_quant[idx]*p_quant+dist_class[idx]*p_class
    p_quant*=dist_quant[idx]/p_event
    p_class*=dist_class[idx]/p_event
    fout.write("{0:.5g} {1:.5g}\n".format(p_quant, p_class))
  fin.close()
  fout.close()

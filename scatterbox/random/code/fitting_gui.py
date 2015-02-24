#!/usr/bin/python

import math, gtk, os.path

from numpy import array, where, sin, pi, arange, exp, linspace, loadtxt,\
  savetxt, append, reshape, linspace
from sys import argv, exit
from os import path
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as\
  FigureCanvas
from matplotlib.figure import Figure

import scipy.optimize as opt

def abs2(x):
  return abs(x)**2

### Usage message
def usage():
  print '''\
Usage: dips.py <num>
       <num> = number of file to use\
'''

### Define the functions that I'm going to use to fit the dips
def gauss(x):
  return exp(-x**2)

def sinc(x):
  if x==0:
    return 1.0
  else:
    return sin(x)/x

def quad(x, a, b, c):
  return a - (b**2)*(x-c)**2

def g(x, a, b, c, x0, s, V):
  return quad(x, a, b, c)*(1.0-V*gauss((x-x0)/s))

def s(x, a, b, c, x0, k, V):
  return quad(x, a, b, c)*(1.0-V*sinc(k*(x-x0)))

def dip_gaussian(xpos, a, b, c, V, x0, s):
  return quad(xpos, a, b, c)*(1.0-V*gauss((xpos-x0)/s))

def dip_gaussnorm(xpos, V, x0, s):
  return 1.0-V*gauss((xpos-x0)/s)

def dip_fullnorm(xpos, V, x0, s, k, q):
  p = 0.5*(1+math.tanh(q))
  return array([1.0-V*(p*gauss((x-x0)/s) + (1-p)*sinc(k*(x-x0))) for x in xpos])

def dip_sinc(xpos, a, b, c, V, x0, k):
  return array([quad(x, a, b, c)*(1.0-V*sinc(k*(x-x0))) for x in xpos])

def dip_full(xpos, a, b, c, V, x0, s, k, q):
  p = 0.5*(1+math.tanh(q))
  return array([quad(x, a, b, c)*(1.0-V*(p*gauss((x-x0)/s) +\
(1-p)*sinc(k*(x-x0)))) for x in xpos])

def mean(L):
  return sum(L)/len(L)

def sumsq(L):
  return sum([x**2 for x in L])

class Fittie:

  def quitApp(self, widget, data=None):
    savetxt("data/{0:02d}/params{0:02d}.dat".format(self.num), self.dipsdata,\
        fmt="%+.4f")
    gtk.main_quit()
    return False

  def nextFile(self, widget, data=None):
    self.normed = [False for i in range(6)]
    self.num += 1
    self.getData()
    self.dip = self.dips[self.idx]
    self.tag = self.tags[self.idx]
    print "file {0:2d}, {1:s}".format(self.num, self.tag)
    self.plotDip()

  def prevFile(self, widget, data=None):
    self.normed = [False for i in range(6)]
    if (self.num > 1):
      self.num -= 1
    self.getData()
    self.dip = self.dips[self.idx]
    self.tag = self.tags[self.idx]
    print "file {0:2d}, {1:s}".format(self.num, self.tag)
    self.plotDip()

  def nextDip(self, widget, data=None):
    self.idx += 1
    self.idx = self.idx % 6
    self.dip = self.dips[self.idx]
    self.tag = self.tags[self.idx]
    print "file {0:2d}, {1:s}".format(self.num, self.tag)
    self.plotDip()

  def prevDip(self, widget, data=None):
    self.idx -= 1
    self.idx = self.idx % 6
    self.dip = self.dips[self.idx]
    self.tag = self.tags[self.idx]
    print "file {0:2d}, {1:s}".format(self.num, self.tag)
    self.plotDip()

  def fitQuadratic(self, widget, data=None):
    if self.normed[self.idx]:
      a = 1
      b = c = 0
      self.updateParams()
      self.replotDip()
    else:
      popt, pcov = opt.curve_fit(quad, self.xpos, self.dip-self.base,\
        p0=(self.p[0], self.p[1], self.p[2]), maxfev=50000)
      self.p[0] = popt[0]
      self.p[1] = popt[1]
      self.p[2] = popt[2]
      self.updateParams()
      self.replotDip()

  def fitGaussian(self, widget, data=None):
    if self.normed[self.idx]:
      popt, pcov = opt.curve_fit(dip_gaussnorm, self.xpos,\
        self.dip-self.base, p0 = (self.p[3], self.p[4], self.p[5]),\
          maxfev=50000)
      self.p[3:6] = popt
      self.updateParams()
      self.replotDip()
    else:
      popt, pcov = opt.curve_fit(dip_gaussian, self.xpos,\
        self.dip-self.base, p0 = (self.p[0], self.p[1], self.p[2],\
        self.p[3], self.p[4], self.p[5]), maxfev=50000)
      self.p[0:6] = popt
      self.updateParams()
      self.replotDip()

  def fitFull(self, widget, data=None):
    if self.normed[self.idx]:
      popt, pcov = opt.curve_fit(dip_fullnorm, self.xpos, self.dip-self.base,\
        p0 = self.p[3:], maxfev=50000)
      self.p[3:] = popt
      self.updateParams()
      self.replotDip()
      self.replotDip()
    else:
      popt, pcov = opt.curve_fit(dip_full, self.xpos, self.dip-self.base,\
        p0 = self.p, maxfev=50000)
      self.p = popt
      self.updateParams()
      self.replotDip()
      self.replotDip()

  def getParams(self, widget, data=None):
    if self.normed[self.idx]:
      pass
    else:
      self.readParams(self, None)
      x0 = self.p[4]
      for i in range(len(self.xpos)):
        x = self.xpos[i]
        if x < x0:
          ilo = i
      xlo = self.xpos[ilo]
      xhi = self.xpos[ilo+1]
      if abs(xlo-x0) < abs(xhi-x0):
        quantum = self.dip[ilo]
      else:
        quantum = self.dip[ilo+1]
    self.dipsdata[self.idx][0] = self.p[3]
    self.dipsdata[self.idx][2] = quantum
    print "Saved"
      

  def toggleAcc(self, widget, data=None):
    self.accidentalson = not self.accidentalson
    self.replotDip()

  def toggleQuad(self, widget, data=None):
    self.quadraticon = not self.quadraticon
    self.replotDip()

  def toggleGaussian(self, widget, data=None):
    self.gaussianon = not self.gaussianon
    self.replotDip()

  def toggleFull(self, widget, data=None):
    self.fullon = not self.fullon
    self.replotDip()

  def revertParams(self, widget, data=None):
    self.plotDip()

  def readParams(self, widget, data=None):
    a = float(self.avalue.get_text()) 
    b = float(self.bvalue.get_text()) 
    c = float(self.cvalue.get_text()) 
    V = float(self.Vvalue.get_text()) 
    x0 = float(self.x0value.get_text()) 
    q = float(self.pvalue.get_text()) 
    s = float(self.svalue.get_text()) 
    k = float(self.kvalue.get_text()) 
    self.p = [a, b, c, V, x0, s, k, q]
    self.replotDip()

  def saveDips(self, widget, data=None):
    self.readParams(None)
    self.dipsdata[self.idx,0] = self.p[3] # Visibility
    self.dipsdata[self.idx,2] = dip_full([self.p[4]], *self.p)[0]+self.base
    L = len(self.xpos)
    if sum(self.normed) > 5:
      savetxt("data/{0:02d}/normed{0:02d}.dat".format(self.num),\
          reshape(append(linspace(-4,4,L, endpoint=True),self.dips),\
          (7,L)).transpose(), fmt="%+.4f")

  def normalise(self, widget, data=None):
    if not self.normed[self.idx]:
      self.dips[self.idx]/=quad(self.xpos, *self.p[0:3])
      self.coeff[self.idx] = self.eta[self.idx]*self.classical[self.idx]*\
          self.sumclassical/sum(self.eta*self.classical)
      self.dips[self.idx]*=self.coeff[self.idx]
      self.normed[self.idx] = True
      self.replotDip()

  def __init__(self, num):
    self.swapped = False
    self.num = num
    self.accidentalson = False
    self.quadraticon = False
    self.gaussianon = False
    self.fullon = False
    self.getData()
    self.idx = 0
    self.dip = self.dips[self.idx]
    self.tag = self.tags[self.idx]
    self.normed = [False for i in range(6)]

  # Loop over dips here
    self.win = gtk.Window()
    self.win.connect("destroy", lambda x: gtk.main_quit())
    self.win.set_default_size(800, 600)
    self.win.set_title("Dip fitting GUI")

    self.vbox = gtk.VBox()
    self.win.add(self.vbox)

    self.fitting = gtk.HBox()
    self.fitquad = gtk.Button(label="Fit Quadratic")
    self.fitgaus = gtk.Button(label="Fit Gaussian")
    self.fitfull = gtk.Button(label="Fit Full")
    self.fitting.pack_start(self.fitquad)
    self.fitting.pack_start(self.fitgaus)
    self.fitting.pack_start(self.fitfull)

    self.fitquad.connect("clicked", self.fitQuadratic)
    self.fitgaus.connect("clicked", self.fitGaussian)
    self.fitfull.connect("clicked", self.fitFull)

    self.show = gtk.HBox()
    self.showaccs = gtk.CheckButton(label="Show accidentals")
    self.showquad = gtk.CheckButton(label="Show envelope")
    self.showgaus = gtk.CheckButton(label="Show gaussian")
    self.showfull = gtk.CheckButton(label="Show full fit")
    self.show.pack_start(self.showaccs)
    self.show.pack_start(self.showquad)
    self.show.pack_start(self.showgaus)
    self.show.pack_start(self.showfull)

    self.showaccs.connect("toggled", self.toggleAcc)
    self.showquad.connect("toggled", self.toggleQuad)
    self.showgaus.connect("toggled", self.toggleGaussian)
    self.showfull.connect("toggled", self.toggleFull)

    self.params = gtk.VBox()
    self.envelope = gtk.HBox()
    self.curve = gtk.HBox()
    self.alabel = gtk.Label("a")
    self.blabel = gtk.Label("b")
    self.clabel = gtk.Label("c")
    self.Vlabel = gtk.Label("V")
    self.x0label= gtk.Label("x0")
    self.slabel = gtk.Label("sigma")
    self.klabel = gtk.Label("k")
    self.plabel = gtk.Label("p")
    self.avalue = gtk.Entry()
    self.bvalue = gtk.Entry()
    self.cvalue = gtk.Entry()
    self.Vvalue = gtk.Entry()
    self.x0value= gtk.Entry()
    self.svalue = gtk.Entry()
    self.kvalue = gtk.Entry()
    self.pvalue = gtk.Entry()

    self.avalue.connect("activate", self.readParams)
    self.bvalue.connect("activate", self.readParams)
    self.cvalue.connect("activate", self.readParams)
    self.Vvalue.connect("activate", self.readParams)
    self.x0value.connect("activate", self.readParams)
    self.svalue.connect("activate", self.readParams)
    self.kvalue.connect("activate", self.readParams)
    self.pvalue.connect("activate", self.readParams)

    self.envelope.pack_start(self.alabel)
    self.envelope.pack_start(self.avalue)
    self.envelope.pack_start(self.blabel)
    self.envelope.pack_start(self.bvalue)
    self.envelope.pack_start(self.clabel)
    self.envelope.pack_start(self.cvalue)
    self.envelope.pack_start(self.plabel)
    self.envelope.pack_start(self.pvalue)
    self.curve.pack_start(self.Vlabel)
    self.curve.pack_start(self.Vvalue)
    self.curve.pack_start(self.x0label)
    self.curve.pack_start(self.x0value)
    self.curve.pack_start(self.slabel)
    self.curve.pack_start(self.svalue)
    self.curve.pack_start(self.klabel)
    self.curve.pack_start(self.kvalue)
    self.params.pack_start(self.envelope)
    self.params.pack_start(self.curve)

    self.plotting = gtk.HBox()
    self.replot = gtk.Button(label="Replot")
    self.revert = gtk.Button(label="Revert")
    self.save = gtk.Button(label="Save")
    self.norm = gtk.Button(label="Normalise")
    self.quit = gtk.Button(label="Quit")
    self.getparams = gtk.Button(label="Get Params")
    self.plotting.pack_start(self.replot)
    self.plotting.pack_start(self.revert)
    self.plotting.pack_start(self.save)
    self.plotting.pack_start(self.norm)
    self.plotting.pack_start(self.quit)
    self.plotting.pack_start(self.getparams)

    self.replot.connect("clicked", self.readParams)
    self.revert.connect("clicked", self.revertParams)
    self.save.connect("clicked", self.saveDips)
    self.norm.connect("clicked", self.normalise)
    self.quit.connect("clicked", self.quitApp)
    self.getparams.connect("clicked", self.getParams)

    self.navigation = gtk.HBox()
    self.prevfile = gtk.Button(label="Previous file")
    self.prevdip = gtk.Button(label="Previous dip")
    self.nextdip = gtk.Button(label="Next dip")
    self.nextfile = gtk.Button(label="Next file")
    self.navigation.pack_start(self.prevfile)
    self.navigation.pack_start(self.prevdip)
    self.navigation.pack_start(self.nextdip)
    self.navigation.pack_start(self.nextfile)

    self.nextfile.connect("clicked", self.nextFile)
    self.prevfile.connect("clicked", self.prevFile)
    self.nextdip.connect("clicked", self.nextDip)
    self.prevdip.connect("clicked", self.prevDip)

    self.fig = Figure(figsize=(5,4), dpi=100)
    self.ax = self.fig.add_subplot(111)
    self.canvas = FigureCanvas(self.fig)
    
    self.vbox.pack_start(self.canvas)
    self.vbox.pack_start(self.params, expand=False)
    self.vbox.pack_start(self.fitting, expand=False)
    self.vbox.pack_start(self.show, expand=False)
    self.vbox.pack_start(self.navigation, expand=False)
    self.vbox.pack_start(self.plotting, expand=False)

    print "file {0:2d}, {1:s}".format(self.num, self.tag)

    self.plotDip()
    self.showquad.set_active(True)
    self.showgaus.set_active(True)
    self.win.show_all()

  def plotDip(self):
    self.getInitialParams(self.xpos, self.dip)
    if self.accidentalson:
      self.base = self.accs[self.idx]
    else:
      self.base = 0
    xdata = linspace(self.xpos[0], self.xpos[-1], 200)
    self.ax.cla()
    self.ax.plot(self.xpos, self.dip)
    if self.quadraticon:
      self.ax.plot(xdata, quad(xdata, self.p[0], self.p[1], self.p[2])+\
        self.base)
    if self.gaussianon:
      self.ax.plot(xdata, dip_gaussian(xdata,\
        self.p[0], self.p[1], self.p[2], self.p[3], self.p[4], self.p[5])+self.base)
    if self.fullon:
      self.ax.plot(xdata, dip_full(xdata, *self.p)+self.base)
    if self.accidentalson:
      self.ax.plot(xdata, [self.base for x in xdata])
    self.canvas.draw()

  def replotDip(self):
    self.ax.cla()
    if self.accidentalson:
      self.base = self.accs[self.idx]
    else:
      self.base = 0
    xdata = linspace(self.xpos[0], self.xpos[-1], 200)
    self.ax.plot(self.xpos, self.dip)
    if (self.normed[self.idx]):
      if self.gaussianon:
        self.ax.plot(xdata, self.coeff[self.idx]*dip_gaussnorm(xdata,\
            self.p[3], self.p[4], self.p[5])+self.base)
      if self.fullon:
        self.ax.plot(xdata, self.coeff[self.idx]*dip_fullnorm(xdata,\
            *self.p[3:])+self.base)
    else:
      if self.quadraticon:
        self.ax.plot(xdata, quad(xdata, self.p[0], self.p[1], self.p[2])+\
          self.base)
      if self.gaussianon:
        self.ax.plot(xdata, dip_gaussian(xdata,\
          self.p[0], self.p[1], self.p[2], self.p[3], self.p[4], self.p[5])+\
            self.base)
      if self.fullon:
        self.ax.plot(xdata, dip_full(xdata, *self.p)+self.base)
      if self.accidentalson:
        self.ax.plot(xdata, [self.base for x in xdata])
    self.canvas.draw()

  def getData(self):
    # Check whether all the necessary files exist
    folder = "data/{0:02}".format(self.num)
    if not path.exists(folder+"/mat{0:02}.dat".format(self.num)):
      print "No file for matrix {0:02}".format(self.num)
      exit(1)
    if not path.exists(folder+"/dip{0:02}.dat".format(self.num)):
      print "No dip for matrix {0:02}".format(self.num)
      exit(1)
    if not (path.exists(folder+"/A.txt") and path.exists(folder+"/C.txt") and \
path.exists(folder+"/B.txt") and path.exists(folder+"/D.txt") and \
path.exists(folder+"/background.txt")):
      print "No efficiency data for matrix {0:02}".format(self.num)
      exit(1)

    # More preliminary stuff ... definitions of useful things
    fin = "data/{0:02}/dip{0:02d}.dat".format(self.num)
    self.tags = ["AB", "AC", "AD", "BC", "BD", "CD"]
    col = {"AB":9, "AC":13, "AD":10, "BC":11, "BD":14, "CD":12}
    pairs = ((0,1), (0,2), (0,3), (1,2), (1,3), (2,3))

    # Blocking data (not really necessary - but I sometimes use the
    # "accidentals"
    blocking = loadtxt(fin, usecols=(9,13,10,11,14,12))[0:6,:]
    self.accs = blocking[2]+blocking[4]
    self.xpos = loadtxt(fin, skiprows=6, usecols=(0,))
    self.dips = loadtxt(fin, skiprows=6, usecols=(9,13,10,11,14,12),\
      unpack=True)

    self.eta = self.getEfficiencies()
    self.classical = self.dips[:,0].copy()

    # Ideal matrix
    matrix = loadtxt(folder+"/mat{0:02}.dat".format(self.num),\
        dtype=complex)[0:4,0:2]
    classical_ide = array([abs2(matrix[i,0]*matrix[j,1]) +\
        abs2(matrix[j,0]*matrix[i,1]) for (i,j) in pairs])
    self.sumclassical = sum(classical_ide)
    self.dipsdata = array([[1, self.dips[i,0], 0] for i in range(6)])
    self.coeff = [1 for i in range(6)]

  def getEfficiencies(self):
    path = "data/{0:02}/".format(self.num)
    names = ["background", "A", "B", "C", "D"]
    counts = []
    for i in range(5):
      fin = open(path+names[i]+".txt", 'r')
      counts.append([int(x) for x in fin.readline().strip('[] \n\r').split()])
    counts = array(counts)
    adjusted = array([counts[i]-counts[0] for i in range(1,5)])
    eta = array([counts[1,0]/float(counts[i+1,i]) for i in range(4)])
    pairs = ((0,1), (0,2), (0,3), (1,2), (1,3), (2,3))
    eps = array([eta[i]*eta[j] for (i,j) in pairs])
    return eps

  def getInitialParams(self, xpos, dip):
    self.p = [0 for i in range(8)]
    vis = []
    flag = "w"
    x = array(xpos)
    if self.accidentalson:
      self.base = self.accs[self.idx]
    else:
      self.base = 0
    y = array(dip)-self.base
    mu = mean(y)
    var = sum([(z-mu)**2 for z in y])
    if self.normed[self.idx]:
      a = 1
      b = 0
      c = 0
      ynorm = y
    else:
      if (y[0] > y[-1]):
        c = x[0]
        a = y[0]
      else:
        c = x[-1]
        a = y[-1]
      dx = abs(x[-1]-x[0])
      dy = abs(y[-1]-y[0])
      b = math.sqrt(dy)/dx
    
      self.p[0] = a
      self.p[1] = b
      self.p[2] = c
      self.fitQuadratic(None)
      ynorm = y/(self.p[0]-self.p[1]**2*(x-self.p[2])**2)

    ymax = max(ynorm)
    yplus = max(ynorm)-1.0
    imax = where(ynorm==ymax)[0][0]
    xmax = xpos[imax]

    ymin = min(ynorm)
    yminus = 1.0-min(ynorm)
    imin = where(ynorm==ymin)[0][0]
    xmin = xpos[imin]

    if yminus > yplus:
      # Dip
      V = yminus
      x0 = xmin
      yfwhm = 1-0.5*yminus
      ifwhm = where(ynorm<yfwhm)[0]
    else:
      # Antidip
      V = -yplus
      x0 = xmax
      yfwhm = 1+0.5*yplus
      ifwhm = where(ynorm>yfwhm)[0]

    #s = 0.5*(x[ifwhm[-1]] - x[ifwhm[0]])/math.log(2)
    s = 0.12
    k = 2.28/s
    q = 0.1

    self.p[3:] = [V, x0, s, k, q]
    self.updateParams()

  def updateParams(self):
    self.avalue.set_text("{0:.0f}".format(self.p[0]))
    self.bvalue.set_text("{0:.2f}".format(self.p[1]))
    self.cvalue.set_text("{0:.2f}".format(self.p[2]))
    self.pvalue.set_text("{0:.2f}".format(self.p[7]))
    self.Vvalue.set_text("{0:.4f}".format(self.p[3]))
    self.x0value.set_text("{0:.3f}".format(self.p[4]))
    self.svalue.set_text("{0:.2f}".format(self.p[5]))
    self.kvalue.set_text("{0:.2f}".format(self.p[6]))
    
  def main(self):
    gtk.main()

if __name__=='__main__':
  if len(argv)<2:
    usage()
    num = 1
  else:
    num = int(argv[1])

  fittie = Fittie(num)
  fittie.main()




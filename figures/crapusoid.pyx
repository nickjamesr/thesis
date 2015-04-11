set terminal pdf
set output "crapusoid.pdf"

set style 1 colour red pointtype 17 pointsize 0.5
set style 2 colour blue pointtype 17 pointsize 0.5

c(phi,A,d,beta,eps,r)=A*(1+cos(2*(phi-beta-eps*cos((phi-r)*pi/180))*pi/180))+d
s(phi,A,d,beta,eps,r)=A*(1-cos(2*(phi-beta-eps*cos((phi-r)*pi/180))*pi/180))+d

fig_w=11.5
fig_m=fig_w/100.

set multiplot
  set nodisplay

  set width 45*fig_m
  set axis x nomirror
  set axis x2 visible
  set nox2tics
  set xrange [0:360]
  set xtics out 120
  set mxtics 30
  set axis y nomirror
  set axis y2 visible
  set noy2tics
  set yrange [0:2e5]
  set mytics 4e4

  # AB fringe
  fin="../scatterbox/molecules/data/OCS/ocs10/pt2.dat"
  set ytics out ("200k" 2e5)
  set key top left 0,0.2
  set origin 0,0
  plot fin using 1:2 with points style 1 title "A",\
    c(x,72000,3600,73,24,103) with lines style 1 notitle,\
    fin using 1:3 with points style 2 title "B",\
    s(x,86000,3500,73,24,103) with lines style 2 notitle

  # CD fringe
  set ytics out ("" 2e5)
  set key top right
  set origin 55*fig_m,0
  plot fin using 1:4 with points style 1 title "C",\
    c(x,65000,3100,34,-24,103) with lines style 1 notitle,\
    fin using 1:5 with points style 2 title "D",\
    s(x,62000,4300,34,-24,105) with lines style 2 notitle

  text "Angle of waveplate, \(\phi_{1}\)" at 35*fig_m,-10*fig_m
  text "Count rate" at -5*fig_m,5*fig_m rotate 90
  
  set display
  refresh
unset multiplot

# Fit data for fringes, using functions:
# c(x)=A*[1+cos(2*(x-beta-eps*cos(x-r)))]+d
# s(x)=A*[1-cos(2*(x-beta-eps*cos(x-r)))]+d
#
# A (c)
#   A=72000
#   d=3600
#   beta=73'
#   eps=24'
#   r=103'
#
# B (s)
#   A=86000
#   d=3500
#   beta=73'
#   eps=24'
#   r=103'
#
# C (c)
#   A=65000
#   d=3100
#   beta=34'
#   eps=-24'
#   r=103'
# 
# D (s)
#   A=62000
#   d=4300
#   beta=34'
#   eps=-24'
#   r=105'

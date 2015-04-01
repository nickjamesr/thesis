set terminal pdf
set output "crapusoid.pdf"

set style 1 colour red pointtype 17 pointsize 0.5
set style 2 colour blue pointtype 17 pointsize 0.5

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
  plot fin using 1:2 with linespoints style 1 title "A",\
    fin using 1:3 with linespoints style 2 title "B"

  # CD fringe
  set ytics out ("" 2e5)
  set key top right
  set origin 55*fig_m,0
  plot fin using 1:4 with linespoints style 1 title "C",\
    fin using 1:5 with linespoints style 2 title "D"

  text "Angle of waveplate, \(\phi_{1}\)" at 35*fig_m,-10*fig_m
  text "Count rate" at -5*fig_m,5*fig_m rotate 90
  
  set display
  refresh
unset multiplot

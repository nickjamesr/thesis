#!/usr/bin/gnuplot

set style line 1 lw 3
set style line 2 lw 3
set style line 3 lw 3 lc rgb "#00aaff"
set style line 4 lc 1 pt 7              # Experimental symmetric
set style line 5 lc 2 pt 7              # Experimental critical
set style line 6 lc rgb "#00aaff" pt 7  # Experimental broken


set xtics out nomirror 0.8,0.4,1.2
set ytics out nomirror -1,14,13
set mxtics 8
set mytics 14
unset ztics
unset colorbox

set xrange [0.9:1.1]
set yrange [0:11]

set border 15
set view 37,318
set xyplane at 0
set grid

# A manifold
fin = "../pt/data/manifold/manifold_A.dat"
set term eps size 12cm,8cm enhanced solid color
set output "manifold_bare_A.eps"
splot fin u 1:2:(log(1+$3)):(log(1+$3)) w pm3d notitle, \
      fin u 1:2:(log(1+$3)) ev :::25::25 w l ls 1 notitle, \
      fin u 1:2:(log(1+$3)) ev :::50::50 w l ls 2 notitle, \
      fin u 1:2:(log(1+$3)) ev :::75::75 w l ls 3 notitle

set output "manifold_data_A.eps"
set view 61, 110
fin = "../pt/data/manifold/rawmanifold_A.dat"
splot fin u 1:2:3:3 w pm3d notitle, \
      fin u 1:2:3 ev :::25:200:25 w l ls 1 notitle, \
      fin u 1:2:3 ev :::50::50 w l ls 2 notitle, \
      fin u 1:2:3 ev :::75::75 w l ls 3 notitle, \
      "../pt/data/symmetric/quart.dat" u 3:1:5 w p ls 4 notitle, \
      "../pt/data/critical/quart.dat" u 3:1:5 w p ls 5 notitle, \
      "../pt/data/broken/quart.dat" u 3:1:5 w p ls 6 notitle

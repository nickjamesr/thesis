set terminal pdf
set output "timestep.pdf"

fig_w=8
fig_m=fig_w/100.

set width fig_w

fdir="../hamiltomo/data"

set style 1 colour black linewidth 2
set style 2 colour rgb(1.0,0.7,0.7) fillcolor rgb(1.0,0.7,0.7)
set style 3 colour rgb(0.7,0.7,1.0) fillcolour rgb(0.7,0.7,1.0)
set style 4 colour rgb(0.6,0.8,0.6) fillcolour rgb(0.6,0.8,0.8)
set style 5 color red
set style 6 color blue
set style 7 color green

set multiplot
  set nodisplay
  set logscale
  set key bottom right
  set xrange [1e-3:0.5]
  set xlabel "timestep, \(\delta t\)"
  set ylabel "Error in \(H\) (trace distance)"
  plot \
       fdir+"/timestep_1e-04.dat" using 1:($2-$3):($2+$3) with yerrorshaded\
       style 2 notitle,\
       fdir+"/timestep_1e-06.dat" using 1:($2-$3):($2+$3) with yerrorshaded\
       style 3 notitle,\
       fdir+"/timestep_1e-08.dat" using 1:($2-$3):($2+$3) with yerrorshaded\
       style 4 notitle,\
       fdir+"/timestep_1e-04.dat" using 1:2 with lines style 5\
       title "\(\varepsilon = 10^{-4}\)",\
       fdir+"/timestep_1e-06.dat" using 1:2 with lines style 6\
       title "\(\varepsilon = 10^{-6}\)",\
       fdir+"/timestep_1e-08.dat" using 1:2 with lines style 7\
       title "\(\varepsilon = 10^{-8}\)",\
       fdir+"/timestep0.dat" using 1:2 with lines style 1 title "No error"
  set display
  refresh
unset multiplot

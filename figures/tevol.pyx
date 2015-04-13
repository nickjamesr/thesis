set terminal pdf
set output "tevol.pdf"

fig_w=12.
fig_m=fig_w/100.

fdir="../hamiltomo/data/TOpt"

set style 1 color blue
set style 2 color green
set style 3 color red

set width 50*fig_m

set axis x nomirror
set axis y nomirror
set xtics out 6.2,0.8
set mxtics out 0.1
set ytics out 0.2,0.05
set mytics out 0.01
set axis x2 visible
set nox2tics
set axis y2 visible
set noy2tics

set key top left 20*fig_m,0

set multiplot
  set nodisplay
  set xlabel "Evolution time, \(t\)"
  set ylabel "Error (Kolmogorov Distance)"
  plot fdir+"/tevol_774.dat" u 1:3 w l style 1 title "774nm",\
       fdir+"/tevol_776.dat" u 1:3 w l style 2 title "776nm",\
       fdir+"/tevol_778.dat" u 1:3 w l style 3 title "778nm"
  set display
  refresh
unset multiplot

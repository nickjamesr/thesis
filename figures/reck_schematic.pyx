set terminal pdf
set output "reck_schematic.pdf"

fig_w=5.5
fig_m=fig_w/100.

set multiplot
  set nodisplay
  eps "reck_schematic.eps" at 0,0 width fig_w

  # Input labels

  # Component labels
  text "\(\mathrm{R}_{1}\)" at 11*fig_m,2*fig_m
  text "\(\mathrm{R}_{2}\)" at 28*fig_m,7*fig_m
  text "\(\mathrm{R}_{3}\)" at 46*fig_m,12*fig_m
  text "\(\mathrm{R}_{n}\)" at 81*fig_m,22*fig_m

  set display
  refresh
unset multiplot

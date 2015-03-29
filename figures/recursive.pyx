set terminal pdf
set output "recursive.pdf"

set fontsize 0.8

fig_w=5.4
fig_m=fig_w/100.

set multiplot
  set nodisplay
  eps "recursive.eps" at 20*fig_m,0 width fig_w
  
  # Input labels
  text "\(\left|m-1\right\rangle\)" at 0,4*fig_m
  text "\(\left|m-2\right\rangle\)" at 0,14*fig_m
  text "\(\left|m-3\right\rangle\)" at 0,24*fig_m
  text "\(\left|0\right\rangle\)" at 12*fig_m,44*fig_m

  # Block labels
  text "\(\mathrm{R}_{1}\)" at 31*fig_m,3*fig_m
  text "\(\mathrm{R}_{2}\)" at 49*fig_m,8*fig_m
  text "\(\mathrm{R}_{3}\)" at 66*fig_m,13*fig_m
  text "\(\mathrm{R}_{m}\)" at 101*fig_m,23*fig_m

  set display
  refresh
unset multiplot

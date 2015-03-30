set terminal pdf
set output "interferometerAB.pdf"

fig_w=6
fig_m=fig_w/100.

set multiplot
  set nodisplay
  eps "interferometerAB.eps" at 0,0 width fig_w
  set display
  refresh
unset multiplot

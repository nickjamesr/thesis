set terminal pdf
set output "integratedreck.pdf"

fig_w=12.5
fig_m=fig_w/100.

set multiplot
  set nodisplay
  eps "integratedreck.eps" at 0,0 width fig_w
  text "DC" at 8*fig_m,14.5*fig_m
  text "\(\phi\)" at 40*fig_m,15*fig_m
  text "MZI" at 80*fig_m,14.5*fig_m
  set display
  refresh
unset multiplot

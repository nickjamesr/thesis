set terminal pdf
set output "reck_general.pdf"

fig_w=10
fig_m=fig_w/100.

set multiplot
  set nodisplay
  eps "reck_general.eps" at 0,0 width fig_w
  
  # Component labels
  text "Phase shift" at 16*fig_m,52*fig_m
  text "MZI" at 16*fig_m,44*fig_m
  text "Directional Coupler" at 16*fig_m,35*fig_m

  # Input labels
  text "\(\left| 0 \right\rangle\)" at -5*fig_m,28*fig_m
  text "\(\left| 1 \right\rangle\)" at -5*fig_m,21*fig_m
  text "\(\left| N-2 \right\rangle\)" at -12*fig_m,7*fig_m
  text "\(\left| N-1 \right\rangle\)" at -12*fig_m,1*fig_m

  # Output labels
  text "\(\left| 0^{\prime} \right\rangle\)" at 102*fig_m,28*fig_m
  text "\(\left| 1^{\prime} \right\rangle\)" at 102*fig_m,21*fig_m
  text "\(\left| N-2^{\prime} \right\rangle\)" at 102*fig_m,7*fig_m
  text "\(\left| N-1^{\prime} \right\rangle\)" at 102*fig_m,1*fig_m

  set display
  refresh
unset multiplot

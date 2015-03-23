set terminal pdf
set output "reck_original.pdf"

fig_w=10
fig_m=fig_w/100.

set multiplot
  set nodisplay
  eps "reck_original.eps" at 0,0 width fig_w

  # Component labels
  text "Beamsplitter" at 20*fig_m,58*fig_m
  text "Phase shift" at 64*fig_m,58*fig_m

  # Input labels
  text "\(\left| 0 \right\rangle\)" at -4*fig_m,36*fig_m
  text "\(\left| 1 \right\rangle\)" at 4*fig_m,28*fig_m
  text "\(\left| 2 \right\rangle\)" at 12*fig_m,20*fig_m
  text "\(\left| N-1 \right\rangle\)" at 28*fig_m,-2*fig_m

  # Output labels
  text "\(\left| N-1^{\prime} \right\rangle\)" at 100*fig_m,35*fig_m
  text "\(\left| N-2^{\prime} \right\rangle\)" at 92*fig_m,27*fig_m
  text "\(\left| 1^{\prime} \right\rangle\)" at 71*fig_m,6*fig_m
  text "\(\left| 0^{\prime} \right\rangle\)" at 63*fig_m,-2*fig_m

  set display
  refresh
unset multiplot

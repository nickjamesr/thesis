set terminal pdf
set output "opensystem.pdf"

set fontsize 0.8

fig_w=12.8
fig_m=fig_w/100.

set multiplot
  set nodisplay
  eps "opensystem.eps" at 17*fig_m,0 width 66*fig_m

  # Input label
  text "Inject only in" at 15*fig_m,25*fig_m halign right
  text "system modes" at 15*fig_m,22*fig_m halign right
  
  # Output label
  text "Detect in" at 85*fig_m,22*fig_m
  text "all four modes" at 85*fig_m,19*fig_m
  text "(system +" at 85*fig_m,16*fig_m
  text "environment)" at 85*fig_m,13*fig_m

  # Internal labels
  text "Closed system: unitary evolution" at 25*fig_m,37*fig_m
  text "Open system: non-unitary" at 40*fig_m,31*fig_m
  text "\Large \(\mathrm{H}_{\mathcal{PT}}\)" at 49*fig_m,23*fig_m
  text "loss" at 43*fig_m,14*fig_m
  text "gain" at 63*fig_m,14*fig_m
  text "Environment" at 27*fig_m,2*fig_m

  set display
  refresh
unset multiplot
  

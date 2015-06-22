set terminal pdf
set output "simplehom.pdf"

fig_w=8
fig_m=fig_w/100.

set multiplot
  set nodisplay

  eps "hom.eps" at 0,0 width fig_w

  text "A" at -8*fig_m,39*fig_m
  text "B" at -8*fig_m,0*fig_m
  text "A\(^{\prime}\)" at 42*fig_m,39*fig_m
  text "B\(^{\prime}\)" at 42*fig_m,0*fig_m

  text "(a)" at 53*fig_m,50*fig_m
  text "(b)" at 72*fig_m,50*fig_m
  text "(c)" at 92*fig_m,50*fig_m

  set display
  refresh
unset multiplot

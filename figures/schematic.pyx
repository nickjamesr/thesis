set terminal pdf
set output "schematic.pdf"

fig_w=12.5
fig_m=fig_w/100.

set multiplot
  set nodisplay
  eps "schematic.eps" at 0,0 width fig_w
  # Input labels
  text "\(\left|H\right\rangle\)" at 0*fig_m,23*fig_m
  text "\(\left|V\right\rangle\)" at 0*fig_m,4*fig_m
  # Component labels (amplitudes)
  text "\(at_0\)" at 13*fig_m,23*fig_m
  text "\(at_1\)" at 51.5*fig_m,23*fig_m
  text "\(aq_2\)" at 90*fig_m,23*fig_m
  text "\(aq_0\)" at 51.5*fig_m,9*fig_m
  text "\(aq_1\)" at 90*fig_m,9*fig_m
  # Component labels (phases)
  text "\(+\phi_{0}\)" at 25*fig_m,23*fig_m
  text "\(-\phi_{0}\)" at 25*fig_m,16*fig_m
  text "\(\delta\left(\phi_{1}\right)+\phi_{1}\)" at 62*fig_m,23*fig_m
  text "\(\delta\left(\phi_{1}\right)-\phi_{1}\)" at 62*fig_m,16*fig_m
  # Output labels
  text "\textbf{A}" at 102*fig_m,0*fig_m
  text "\textbf{B}" at 102*fig_m,6.5*fig_m
  text "\textbf{C}" at 102*fig_m,13*fig_m
  text "\textbf{D}" at 102*fig_m,19.5*fig_m
  set display
  refresh
unset multiplot

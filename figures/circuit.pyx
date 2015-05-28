set terminal pdf
set output "circuit.pdf"

fig_w=12
fig_m=fig_w/100.

set multiplot
  set nodisplay
  image "circuit.png" at 0,0 width fig_w
  # Label components
  text "PBD" at 7*fig_m,48*fig_m
  text "HWP" at 7*fig_m,40*fig_m
  text "HWP (with hole)" at 7*fig_m,32*fig_m
  text "QWP(\(45^{\circ}\))" at 30*fig_m,48*fig_m
  text "X" at 30*fig_m,40*fig_m
  text "PBS" at 57*fig_m,48*fig_m
  text "prism" at 57*fig_m,40*fig_m
  # Label inputs
  text "\textbf{V}" at 5*fig_m,15*fig_m
  text "\textbf{H}" at 0*fig_m,2*fig_m
  # Label detectors
  text "\textbf{A}" at 93*fig_m,13*fig_m
  text "\textbf{B}" at 102*fig_m,22*fig_m
  text "\textbf{C}" at 92*fig_m,40*fig_m
  text "\textbf{D}" at 82*fig_m,49*fig_m
  # Label elements
  text "\(at_0\)" at 19*fig_m,20*fig_m
  text "\(\phi_0\)" at 26*fig_m,20*fig_m
  text "\(at_1\)" at 40*fig_m,28*fig_m
  text "\(\phi_1\)" at 47*fig_m,28*fig_m
  text "\(aq_0\)" at 54*fig_m,28*fig_m
  text "\(aq_1\)" at 88*fig_m,28*fig_m
  text "\(aq_2\)" at 89*fig_m,36*fig_m
  set display
  refresh
unset multiplot

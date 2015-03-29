set terminal pdf
set output "qubits.pdf"

fontscale=0.65
fig_w = 12.8
fig_m = fig_w/100.
fig_h = 70*fig_m # Empirical
offset=42*fig_m

set fontsize fontscale

set multiplot
  set nodisplay
  eps "threequbit.eps" at 5*fig_m,0 width 95*fig_m
  eps "twoqubit.eps" at 5*fig_m,offset width 95*fig_m

  # Rail labels
  text "\(\left|00\right\rangle\)" at 0,offset+22.5*fig_m
  text "\(\left|01\right\rangle\)" at 0,offset+19.5*fig_m
  text "\(\left|10\right\rangle\)" at 0,offset+16.5*fig_m
  text "\(\left|11\right\rangle\)" at 0,offset+13.5*fig_m
 
  text "\(\left|000\right\rangle\)" at 0,34*fig_m
  text "\(\left|001\right\rangle\)" at 0,31.64*fig_m
  text "\(\left|010\right\rangle\)" at 0,29.29*fig_m
  text "\(\left|011\right\rangle\)" at 0,26.93*fig_m
  text "\(\left|100\right\rangle\)" at 0,24.57*fig_m
  text "\(\left|101\right\rangle\)" at 0,22.21*fig_m
  text "\(\left|110\right\rangle\)" at 0,19.86*fig_m
  text "\(\left|111\right\rangle\)" at 0,17.5*fig_m

  # Gate labels
  text "\(\Phi\)" at 6.5*fig_m,2.8*fig_m
  text "\(\overline{\Phi}\)" at 9.6*fig_m,2.8*fig_m
  text "\(\Phi\)" at 13.0*fig_m,2.8*fig_m
  text "\(\overline{\Phi}\)" at 16.2*fig_m,2.8*fig_m
  text "\(\Phi\)" at 19.5*fig_m,2.8*fig_m
  text "\(\overline{\Phi}\)" at 22.8*fig_m,2.8*fig_m
  text "\(\Phi\)" at 26.0*fig_m,2.8*fig_m
  text "\(\overline{\Phi}\)" at 29.4*fig_m,2.8*fig_m

  text "H" at 36.7*fig_m,2.8*fig_m
  text "\(\Phi\)" at 41.7*fig_m,2.8*fig_m
  text "\(\Phi\)" at 46.6*fig_m,2.8*fig_m
  text "\(\Phi\)" at 51.5*fig_m,2.8*fig_m
  text "\(\Phi\)" at 56.4*fig_m,2.8*fig_m
  text "H" at 61.3*fig_m,2.8*fig_m

  text "H" at 75.2*fig_m,2.8*fig_m
  text "\(\Phi\)" at 79.3*fig_m,2.8*fig_m
  text "\(\Phi\)" at 83.4*fig_m,2.8*fig_m
  text "\(\Phi\)" at 87.5*fig_m,2.8*fig_m
  text "H" at 91.6*fig_m,2.8*fig_m

  text "\(\Phi\)" at 6.5*fig_m,offset+2.7*fig_m
  text "\(\overline{\Phi}\)" at 9.6*fig_m,offset+2.7*fig_m
  text "\(\Phi\)" at 12.7*fig_m,offset+2.7*fig_m
  text "\(\overline{\Phi}\)" at 15.7*fig_m,offset+2.7*fig_m
  text "H" at 19.5*fig_m,offset+2.7*fig_m
  text "\(\Phi\)" at 22.6*fig_m,offset+2.7*fig_m
  text "H" at 25.6*fig_m,offset+2.7*fig_m
  text "\(\overline{\Phi}\)" at 29.4*fig_m,offset+2.7*fig_m
  text "H" at 34.7*fig_m,offset+2.7*fig_m
  text "\(\Phi\)" at 37.8*fig_m,offset+2.7*fig_m
  text "H" at 41.0*fig_m,offset+2.7*fig_m
  text "\(\Phi\)" at 46.3*fig_m,offset+2.7*fig_m
  text "H" at 50.1*fig_m,offset+2.7*fig_m
  text "\(\Phi\)" at 53.2*fig_m,offset+2.7*fig_m
  text "\(\Phi\)" at 56.4*fig_m,offset+2.7*fig_m
  text "H" at 59.5*fig_m,offset+2.7*fig_m
  text "\(\overline{\Phi}\)" at 63.3*fig_m,offset+2.7*fig_m
  text "\(\overline{\Phi}\)" at 66.4*fig_m,offset+2.7*fig_m
  text "H" at 71.7*fig_m,offset+2.7*fig_m
  text "\(\Phi\)" at 74.8*fig_m,offset+2.7*fig_m
  text "H" at 77.9*fig_m,offset+2.7*fig_m
  text "\(\Phi\)" at 83.4*fig_m,offset+2.7*fig_m
  text "H" at 87.2*fig_m,offset+2.7*fig_m
  text "\(\Phi\)" at 90.3*fig_m,offset+2.7*fig_m
  text "H" at 93.4*fig_m,offset+2.7*fig_m
  text "\(\overline{\Phi}\)" at 97.2*fig_m,offset+2.7*fig_m

  # Subfigure labels

  set axis x invisible
  set axis y invisible
  set xrange [0:1]
  set yrange [0:1]
  set size fig_w
  set size ratio fig_h/fig_w
  set label 1 "(a)" at 0.48,0.98 with fontsize 1
  set label 2 "(b)" at 0.15,0.53 with fontsize 1
  set label 3 "(c)" at 0.48,0.53 with fontsize 1
  set label 4 "(d)" at 0.82,0.53 with fontsize 1
  plot

  set display
  refresh
unset multiplot

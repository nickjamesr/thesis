set terminal pdf
set output "vibrations.pdf"

fig_w=12.
fig_m=fig_w/100.
fig_h=26*fig_m # Empirical

set multiplot
  set nodisplay
  image "vibrations.png" at 0,0 width fig_w
  text "(a)" at fig_w/6.,fig_h halign centre
  text "(b)" at fig_w/2.,fig_h halign centre
  text "(c)" at 85*fig_m,fig_h halign centre
  set display
  refresh
unset multiplot

set terminal pdf
set output "cascade.pdf"
set fontsize 0.8

fig_w=5.6
fig_m=fig_w/100.

dy=6.4*fig_m

set multiplot
  set nodisplay
  line from 0,0 to fig_w,0 with color white
  eps "cascade.eps" at 0,dy width fig_w

  # Physical labels
  text "\(r_{0}\)" at 0,43*fig_m+dy
  text "\(r_{1}\)" at 15*fig_m,43*fig_m+dy
  text "\(r_{2}\)" at 35*fig_m,33*fig_m+dy
  text "\(r_{m-1}\)" at 72*fig_m,13*fig_m+dy

  text "\(\phi_{0}\)" at 86*fig_m,45*fig_m+dy
  text "\(\phi_{1}\)" at 86*fig_m,35*fig_m+dy
  text "\(\phi_{m-2}\)" at 85*fig_m,15*fig_m+dy
  text "\(\phi_{m-1}\)" at 85*fig_m,5*fig_m+dy

  # Cartesian labels
  text "\(x_{0}\)" at 100*fig_m,43*fig_m+dy
  text "\(x_{1}\)" at 100*fig_m,33*fig_m+dy
  text "\(x_{m-2}\)" at 100*fig_m,13*fig_m+dy
  text "\(x_{m-1}\)" at 100*fig_m,3*fig_m+dy

  set display
  refresh
unset multiplot

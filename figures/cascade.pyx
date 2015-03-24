set terminal pdf
set output "cascade.pdf"

fig_w=5.5
fig_m=fig_w/100.
dy=6*fig_m

set multiplot
  set nodisplay
  eps "cascade.eps" at 0,dy width fig_w

  # Hack to shift image up
  line from 0*fig_m,0*fig_m to 100*fig_m,0*fig_m with colour white

  # Cartesian labels
  text "\(x_{0}\)" at 102*fig_m,40*fig_m+dy
  text "\(x_{1}\)" at 102*fig_m,30*fig_m+dy
  text "\(x_{n-2}\)" at 102*fig_m,10*fig_m+dy
  text "\(x_{n-1}\)" at 102*fig_m,0*fig_m+dy

  # Physical labels
  text "\(r_{0}\)" at 0*fig_m,45*fig_m+dy
  text "\(r_{1}\)" at 15*fig_m,45*fig_m+dy
  text "\(r_{2}\)" at 35*fig_m,35*fig_m+dy
  text "\(r_{n-1}\)" at 70*fig_m,15*fig_m+dy

  set display
  refresh
unset multiplot

set terminal png dpi 240
set output "manifolds.png"

fig_w=12.
fig_m=fig_w/100.

set multiplot
  set nodisplay
  eps "manifold_bare_A.eps" at 0,0 width 55*fig_m
  eps "manifold_data_A.eps" at 50*fig_m,0 width 55*fig_m
   
  # Axis labels
  text "\(t\)" at 14*fig_m,3*fig_m
  text "\(\gamma\)" at 40*fig_m,4*fig_m
  text "\(t\)" at 73*fig_m,3*fig_m
  text "\(\gamma\)" at 95*fig_m,8*fig_m
  
  # Axis scale
  text "\(0\)" at 23*fig_m,1*fig_m
  text "\(11\)" at 5*fig_m,10*fig_m
  text "\(0.90\)" at 28*fig_m,1*fig_m
  text "\(1.10\)" at 48*fig_m,9*fig_m
  text "\(0\)" at 58*fig_m,5*fig_m
  text "\(11\)" at 83*fig_m,2*fig_m
  text "\(1.10\)" at 89*fig_m,4*fig_m
  text "\(0.90\)" at 98*fig_m,11*fig_m

  set display
  refresh
unset multiplot

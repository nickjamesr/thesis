set terminal pdf
set output "clouds.pdf"

fig_w=12
fig_m=fig_w/100.
plot_w=52*fig_m

set multiplot
  set nodisplay
  image "walk_ex_q.png" at 0,0 width 55*fig_m
  image "walk_ex_c.png" at fig_w-plot_w,0 width plot_w
  image "walk_th_q.png" at 0,38*fig_m width 55*fig_m
  image "walk_th_c.png" at fig_w-plot_w,38*fig_m width plot_w

  # Axis labels
  text "\small \(0\)" at 22*fig_m,37*fig_m
  text "\small \(0\)" at 18*fig_m,39*fig_m
  text "\small \(0\)" at 43*fig_m,49*fig_m
  text "\small \(20\)" at 11*fig_m,53*fig_m
  text "\small \(20\)" at 42*fig_m,46*fig_m
  text "\small \(20\)" at 49*fig_m,69*fig_m

  text "\small \(0\)" at 69*fig_m,37*fig_m
  text "\small \(0\)" at 65*fig_m,39*fig_m
  text "\small \(0\)" at 89*fig_m,49*fig_m
  text "\small \(20\)" at 58*fig_m,53*fig_m
  text "\small \(20\)" at 89*fig_m,46*fig_m
  text "\small \(20\)" at 94*fig_m,67*fig_m

  text "\small \(0\)" at 22*fig_m,-1*fig_m
  text "\small \(0\)" at 18*fig_m,1*fig_m
  text "\small \(0\)" at 43*fig_m,11*fig_m
  text "\small \(20\)" at 11*fig_m,15*fig_m
  text "\small \(20\)" at 42*fig_m,8*fig_m
  text "\small \(20\)" at 49*fig_m,31*fig_m

  text "\small \(0\)" at 69*fig_m,-1*fig_m
  text "\small \(0\)" at 65*fig_m,1*fig_m
  text "\small \(0\)" at 89*fig_m,11*fig_m
  text "\small \(20\)" at 58*fig_m,15*fig_m
  text "\small \(20\)" at 89*fig_m,8*fig_m
  text "\small \(20\)" at 94*fig_m,29*fig_m

  # Subfigure labels
  text "(a)" at 5*fig_m,74*fig_m
  text "(b)" at plot_w,74*fig_m
  text "(c)" at 5*fig_m,36*fig_m
  text "(d)" at plot_w,36*fig_m
  set display
  refresh
unset multiplot

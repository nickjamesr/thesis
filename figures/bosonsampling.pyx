set terminal pdf
set output "bosonsampling.pdf"

set style 1 linewidth 2 colour black
set style 2 colour white fillcolour rgb(1.0,0.8,0.8)
set style 3 colour white fillcolour rgb(0.8,1.0,0.8)
set style 4 colour white fillcolour rgb(1.0,1.0,0.8)

fig_w=12
fig_m=fig_w/100.

set multiplot
  set nodisplay

  # Unitary figure
  eps "BSunitary.eps" at 3*fig_m,0 width 40*fig_m

  # Labels on unitary
  text "\(p\) photons" at 0*fig_m,37*fig_m
  text "\(m\) modes" at 0,11*fig_m
  text "\Large \(\mathrm{U}\)" at 23*fig_m,15*fig_m
  text "\(p\) \textit{distinct}" at 43*fig_m,-3*fig_m halign right
  text "detection events" at 43*fig_m,-7*fig_m halign right

  # Shaded boxes
    # Columns
  box at 52*fig_m,14*fig_m width 8.5*fig_m height 19*fig_m with style 2
  box at 63*fig_m,14*fig_m width 8.5*fig_m height 19*fig_m with style 2
  box at 74*fig_m,14*fig_m width 8.5*fig_m height 19*fig_m with style 2
    # Rows 
  box at 51*fig_m,15*fig_m width 53*fig_m height 2*fig_m with style 3
  box at 51*fig_m,23.5*fig_m width 53*fig_m height 2*fig_m with style 3
  box at 51*fig_m,30*fig_m width 53*fig_m height 2*fig_m with style 3
    # Intersections
  box at 52*fig_m,15*fig_m width 8.5*fig_m height 2*fig_m with style 4
  box at 52*fig_m,23.5*fig_m width 8.5*fig_m height 2*fig_m with style 4
  box at 52*fig_m,30*fig_m width 8.5*fig_m height 2*fig_m with style 4
  box at 63*fig_m,15*fig_m width 8.5*fig_m height 2*fig_m with style 4
  box at 63*fig_m,23.5*fig_m width 8.5*fig_m height 2*fig_m with style 4
  box at 63*fig_m,30*fig_m width 8.5*fig_m height 2*fig_m with style 4
  box at 74*fig_m,15*fig_m width 8.5*fig_m height 2*fig_m with style 4
  box at 74*fig_m,23.5*fig_m width 8.5*fig_m height 2*fig_m with style 4
  box at 74*fig_m,30*fig_m width 8.5*fig_m height 2*fig_m with style 4

  # Big unitary
  text "\small \(\left(\begin{array}{lllcl}\
u_{0,0} & u_{0,1} & u_{0,2} & \cdots & u_{0,m-1} \\\\\
u_{1,0} & u_{1,1} & u_{1,2} & \cdots & u_{1,m-1} \\\\\
u_{2,0} & u_{2,1} & u_{2,2} & \cdots & u_{2,m-1} \\\\\
\vdots & \vdots & \vdots & & \vdots \\\\\
u_{m-1,0} & u_{m-1,1} & u_{m-1,2} & \cdots & u_{m-1,m-1} \
\end{array}\right)\)" at 48*fig_m,15*fig_m

  # Submatrix
  text "\small \(\left|\mathrm{Per}\left(\begin{array}{lll}\
u_{0,0} & u_{0,1} & u_{0,2} \\\\\
u_{2,0} & u_{2,1} & u_{2,2} \\\\\
u_{m-1,0} & u_{m-1,1} & u_{m-1,2} \
\end{array}\right)\right|^{2}\)" at 60*fig_m,-7*fig_m

  arrow from 77*fig_m,12*fig_m to 77*fig_m,5*fig_m with style 1

  # Subfigure labels
  text "(a)" at 23*fig_m,39*fig_m
  text "(b)" at 76*fig_m,37*fig_m
  text "(c)" at 60*fig_m, 6*fig_m
  set display
  refresh
unset multiplot


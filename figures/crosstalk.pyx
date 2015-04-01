set terminal pdf
set output "crosstalk.pdf"

R(theta,phi)=0.25*(sin(0.5*theta)-1)**2+sin(0.5*theta)*cos(0.5*phi+0.25*(theta-\
            pi))**2
T(theta,phi)=0.25*(sin(0.5*theta)-1)**2+sin(0.5*theta)*sin(0.5*phi+0.25*(theta-\
            pi))**2

set style 1 colour black
set style 2 colour red
set style 3 colour blue
set style 4 colour green

fig_w=12
fig_m=fig_w/100.

set multiplot
  set nodisplay
  eps "crosstalk.eps" at 0*fig_m,-5*fig_m width 50*fig_m

  # Labels
  text "\(\theta\)" at 25*fig_m,29*fig_m
  text "\(\phi\)" at 35*fig_m,26*fig_m
  text "\(R\)" at 48*fig_m,25*fig_m
  text "\(T\)" at 48*fig_m,15*fig_m

  text "\(\eta\)" at 19*fig_m,2*fig_m
  text "\(\delta\)" at 26*fig_m,2*fig_m
  text "\(\phi\)" at 35*fig_m,2*fig_m
  text "\(R\)" at 48*fig_m,2*fig_m
  text "\(T\)" at 48*fig_m,-8*fig_m

  # Subfigure labels
  text "(a)" at 1*fig_m,35*fig_m
  text "(b)" at 1*fig_m,6*fig_m
  text "(c)" at 80*fig_m,35*fig_m

  set xrange [0:pi]
  set yrange [0:1.1]
  set width 40*fig_m
  set origin 60*fig_m,0
  set xlabel "\(\phi\)"
  set axis x nomirror
  set axis y arrow nomirror
  set xtics out ("" 0.25*pi, "\(\pi/2\)" 0.5*pi, "" 0.75*pi, "\(\pi\)" pi)
  set ytics out 0.5
  set mytics 0.25
  set size ratio 0.85 # empirical
  set key top right 0.5,-0.2
  plot R(0.2*pi,x) with lines style 1 title "\(\theta=0.2\pi\)",\
       R(0.4*pi,x) with lines style 2 title "\(\theta=0.4\pi\)",\
       R(0.6*pi,x) with lines style 3 title "\(\theta=0.6\pi\)",\
       R(0.8*pi,x) with lines style 4 title "\(\theta=0.8\pi\)"

  text "\(R\)" at 55*fig_m,35*fig_m

  set display
  refresh
unset multiplot


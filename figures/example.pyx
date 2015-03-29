set terminal pdf
set output "example.pdf"

set fontsize 0.8

set style 1 colour cyan
set style 2 colour yellow
set style 3 colour blue
set style 4 colour green
set style 5 colour red

fig_w=12.8
fig_m=fig_w/100.
fig_h=60*fig_m # Empirical
plot_w=28*fig_m
plot_h=20*fig_m
dy=8*fig_m


set multiplot
  set nodisplay
  eps "example.eps" at 0*fig_m,plot_h+dy width fig_w
  eps "beamsplitter.eps" at 15*fig_m,plot_h-7*fig_m width 8*fig_m
  eps "bsmzi.eps" at 37*fig_m,plot_h-7*fig_m width 15*fig_m
  eps "dcmzi.eps" at 82*fig_m,plot_h-7*fig_m width 18*fig_m

  # Beamsplitter reflectivities
  set size plot_w
  set size ratio plot_h/plot_w
  set axis x arrow nomirror
  set axis y arrow nomirror
  set xrange [0:1.1]
  set yrange [0:6.0]
  set xtics out 1
  set ytics out 0,5
  set mytics 1
  set origin 3*fig_m,0
  plot
  set axis x invisible
  set axis y invisible
  set xrange [0:1]
  set yrange [0:5]
  set size plot_w*11/12.
  set size ratio (plot_h*5/6.)/(plot_w*11/12.)
  plot 1 notitle with style 1,\
    2*(1-x) notitle with style 2,\
    3*(1-x)**2 notitle with style 3,\
    4*(1-x)**3 notitle with style 4,\
    5*(1-x)**4 notitle with style 5

  # BS-MZI phases
  set size plot_w
  set size ratio plot_h/plot_w
  set axis x visible arrow nomirror
  set axis y visible arrow nomirror
  set xrange [0:1.1*pi]
  set yrange [0:1.2]
  set xtics out ("\(\pi\)" pi)
  set ytics out 0,1,5
  set mytics 0.2
  set origin 36*fig_m,0
  plot
  set axis x invisible
  set axis y invisible
  set xrange [0:pi]
  set yrange [0:1]
  set size plot_w*11/12.
  set size ratio (plot_h*5/6.)/(plot_w*11/12.)
  plot sin(0.5*x)*cos(0.5*x) notitle with style 1,\
    2*sin(0.5*x)**3*cos(0.5*x) notitle with style 2,\
    3*sin(0.5*x)**5*cos(0.5*x) notitle with style 3,\
    4*sin(0.5*x)**7*cos(0.5*x) notitle with style 4,\
    5*sin(0.5*x)**9*cos(0.5*x) notitle with style 5

  # DC-MZI phases
  set size plot_w
  set size ratio plot_h/plot_w
  set axis x visible arrow nomirror
  set axis y visible arrow nomirror
  set xrange [0:1.1*pi]
  set yrange [0:1.2]
  set xtics out ("\(\pi\)" pi)
  set ytics out 0,1,5
  set mytics 0.2
  set origin 71*fig_m,0
  plot
  set axis x invisible
  set axis y invisible
  set xrange [0:pi]
  set yrange [0:1]
  set size plot_w*11/12.
  set size ratio (plot_h*5/6.)/(plot_w*11/12.)
  plot cos(0.5*x)*sin(0.5*x) notitle with style 1,\
    2*cos(0.5*x)**3*sin(0.5*x) notitle with style 2,\
    3*cos(0.5*x)**5*sin(0.5*x) notitle with style 3,\
    4*cos(0.5*x)**7*sin(0.5*x) notitle with style 4,\
    5*cos(0.5*x)**9*sin(0.5*x) notitle with style 5

  # Axis labels
  text "\(r\)" at 31*fig_m,-3*fig_m
  text "\(\theta\)" at 64*fig_m,-3*fig_m
  text "\(\xi\)" at 99*fig_m,-3*fig_m
  text "\(\mathcal{P}\left(r\right)\)" at 4*fig_m,plot_h-1*fig_m
  text "\(\mathcal{P}\left(\theta\right)\)" at 37*fig_m,plot_h-1*fig_m
  text "\(\mathcal{P}\left(\xi\right)\)" at 72*fig_m,plot_h-1*fig_m

  # Component labels
  # In graphs
  text "\(r\)" at 19*fig_m,plot_h-2*fig_m
  text "\(\theta\)" at 45*fig_m,plot_h-2*fig_m
  text "\(\xi\)" at 91*fig_m,plot_h-2*fig_m
  # In Reck scheme
  text "\(r_{6,1}\)" at 53*fig_m,45*fig_m+dy
  text "\(r_{6,2}\)" at 64*fig_m,40*fig_m+dy
  text "\(r_{6,3}\)" at 75*fig_m,34*fig_m+dy
  text "\(r_{6,4}\)" at 86*fig_m,29*fig_m+dy
  text "\(r_{6,5}\)" at 97*fig_m,23*fig_m+dy

  text "\(r_{5,1}\)" at 42*fig_m,40*fig_m+dy
  text "\(r_{5,2}\)" at 53*fig_m,34*fig_m+dy
  text "\(r_{5,3}\)" at 64*fig_m,29*fig_m+dy
  text "\(r_{5,4}\)" at 75*fig_m,23*fig_m+dy

  text "\(r_{4,1}\)" at 31*fig_m,34*fig_m+dy
  text "\(r_{4,2}\)" at 42*fig_m,29*fig_m+dy
  text "\(r_{4,3}\)" at 53*fig_m,23*fig_m+dy

  text "\(r_{3,1}\)" at 20*fig_m,29*fig_m+dy
  text "\(r_{3,2}\)" at 31*fig_m,23*fig_m+dy

  text "\(r_{2,1}\)" at 9*fig_m,23*fig_m+dy

  set xrange [0:1]
  set yrange [0:1]
  set size fig_w
  set size ratio fig_h/fig_w
  set origin 0,0
  set axis x invisible
  set axis y invisible
  set label 1 "(a)" at 0,1 with fontsize 1
  set label 2 "(b)" at 0,0.39 with fontsize 1
  set label 3 "(c)" at 0.33,0.39 with fontsize 1
  set label 4 "(d)" at 0.67,0.39 with fontsize 1
  plot

  set display
  refresh
unset multiplot

set terminal pdf
set output "integrated.pdf"

set style 1 colour cyan
set style 2 colour yellow
set style 3 colour blue
set style 4 colour green
set style 5 colour red

fig_w=8
fig_m=fig_w/100.
plot_w=fig_w
plot_h=60*fig_m

set multiplot
  set nodisplay
  eps "dcmzi.eps" at 40*fig_m,plot_h-15*fig_m width 40*fig_m

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
  set origin 0,0
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
  text "\(\xi\)" at 98*fig_m,-6*fig_m
  text "\(\mathcal{P}_{\xi}\left(\xi\right)\)" at 2*fig_m,58*fig_m

  # Phase shift label
  text "\(\xi\)" at 59*fig_m,57*fig_m

  set display
  refresh
unset multiplot


set terminal pdf
set output "sixphoton.pdf"

quant_col=rgb(0.0,0.0,1.0)
class_col=rgb(1.0,0.0,0.0)

set style 1 colour quant_col
set style 2 colour class_col
set style 3 linetype 2 colour black

fig_w=11
fig_m=fig_w/100.
plot_w=45*fig_m
h_pad=10*fig_m

set key top right 0.4,-1

set axis x nomirror
set axis y nomirror

set axis x2 visible
set axis y2 visible

set nox2tics
set noy2tics

set ylabel "Confidence"

set xrange [0:14]
set yrange [0:1.05]

set multiplot
  set nodisplay

  # Quantum
  set xtics out 4
  set mxtics 1
  set width plot_w
  set origin 0,0
  set xlabel "(a) Quantum events"
  fin="../reck/data/quantum_events.dat"
  plot 1 with lines style 3 notitle,\
       fin using 0:1 with lines style 1\
       title "\(\mathcal{P}\left(\mathrm{Quantum}\right)\)",\
       fin using 0:2 with lines style 2\
       title "\(\mathcal{P}\left(\mathrm{Classical}\right)\)"

  # Classical
  set width plot_w
  set origin plot_w+h_pad,0
  set xlabel "(b) Classical events"
  unset ylabel
  fin="../reck/data/classical_events.dat"
  plot 1 with lines style 3 notitle,\
       fin using 0:1 with lines style 1 notitle,\
       fin using 0:2 with lines style 2 notitle

  set display

  # Subfigure labels
  set xrange [0:1]
  set yrange [0:1]
  set origin 0,0
  set width fig_w
  set axis x invisible
  set axis y invisible
  set axis x2 invisible
  set axis y2 invisible
  set label 1 "(a)" at 0.20,0.5 with fontsize 1
  set label 2 "(b)" at 0.75,0.5 with fontsize 1
  plot

  refresh

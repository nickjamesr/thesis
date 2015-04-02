set terminal pdf
set output "benchmarking.pdf"

fig_w=13.0
fig_m=fig_w/100.

pair_w=48*fig_m
sing_w=32*fig_m
plot_h=25*fig_m
h_pad=5*fig_m
v_pad=5*fig_m
text_dx=3*fig_m
text_dy=-5*fig_m

prefix="../scatterbox/random/data"

bw=0.8
set boxwidth bw

single_col=rgb(0.0,0.5,0.0)
quant_col=rgb(0.0,0.0,0.8)
class_col=rgb(0.8,0.0,0.0)

single_fill=rgb(0.6,0.8,0.6)
quant_fill=rgb(0.7,0.7,1.0)
class_fill=rgb(1.0,0.7,0.7)

set style 1 color black linewidth 0.5 fillcolor quant_fill
set style 2 color black linewidth 0.5 fillcolor class_fill
set style 3 color black linewidth 0.5 fillcolor single_fill

set style 4 color quant_col pointtype 17 pointsize 0.8
set style 5 color class_col pointtype 17 pointsize 0.8
set style 6 color single_col pointtype 17 pointsize 0.8

set axis x nomirror
set axis x2 visible
set nox2tics
set axis y nomirror
set yrange [0:0.5]
set y2range [0:0.5]
set axis y2 visible nomirror

set multiplot
  set nodisplay
### Coincidences
  set xrange [-0.5:5.5]
  set width pair_w
  set size ratio plot_h/pair_w
  set ytics out 0.5
  set mytics 0.1
  set noy2tics
  # Quantum
  set xtics out ("" 0, "" 1, "" 2, "" 3, "" 4, "" 5)
  set origin 0,1*(plot_h+v_pad)
  plot prefix+"/example_quantum.dat" using 1:4 with boxes style 1 notitle,\
       prefix+"/example_quantum.dat" using 1:3 with boxes style 1 notitle,\
       prefix+"/example_quantum.dat" using 1:2 with boxes style 1 notitle,\
       prefix+"/example_quantum.dat" using 1:5 with points style 4 notitle

  # Classical
  set xtics out ("AB" 0, "AC" 1, "AD" 2, "BC" 3, "BD" 4, "CD" 5)
  set origin 0,0*(plot_h+v_pad)
  plot prefix+"/example_classical.dat" using 1:4 with boxes style 2 notitle,\
       prefix+"/example_classical.dat" using 1:3 with boxes style 2 notitle,\
       prefix+"/example_classical.dat" using 1:2 with boxes style 2 notitle,\
       prefix+"/example_classical.dat" using 1:5 with points style 5 notitle

### Singles
  set xrange [-0.5:3.5]
  set width sing_w
  set size ratio plot_h/sing_w
  set noytics
  set y2tics out 0.5
  set my2tics 0.1
  # Quart
  set xtics out ("" 0, "" 1, "" 2, "" 3)
  set origin pair_w+h_pad,1*(plot_h+v_pad)
  plot prefix+"/example_quart.dat" using 1:4 with boxes style 3 notitle,\
       prefix+"/example_quart.dat" using 1:3 with boxes style 3 notitle,\
       prefix+"/example_quart.dat" using 1:2 with boxes style 3 notitle,\
       prefix+"/example_quart.dat" using 1:5 with points style 6 notitle

  # Trit
  set xtics out ("A" 0, "B" 1, "C" 2, "D" 3)
  set origin pair_w+h_pad,0*(plot_h+v_pad)
  plot prefix+"/example_trit.dat" using 1:4 with boxes style 3 notitle,\
       prefix+"/example_trit.dat" using 1:3 with boxes style 3 notitle,\
       prefix+"/example_trit.dat" using 1:2 with boxes style 3 notitle,\
       prefix+"/example_trit.dat" using 1:5 with points style 6 notitle

  # Subfigure labels
  text "(a)" at text_dx,2*plot_h+v_pad+text_dy
  text "(b)" at text_dx,plot_h+text_dy
  text "(c)" at pair_w+h_pad+text_dx,2*plot_h+v_pad+text_dy
  text "(d)" at pair_w+h_pad+text_dx,plot_h+text_dy

  set display
  refresh

unset multiplot


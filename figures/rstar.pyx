set terminal pdf
set output "rstar.pdf"

quant_col=rgb(0.0,0.0,1.0)
quant_fill=rgb(0.7,0.7,1.0)
uniform_col=rgb(0.0,0.0,0.0)

set style 1 colour quant_col
set style 2 colour uniform_col
set style 3 colour black fillcolour quant_fill
set style 4 linetype 2 colour black

fig_w=11
fig_m=fig_w/100.
plot_w=42*fig_m
h_pad=16*fig_m

set width plot_w

set axis x nomirror
set axis y nomirror

set axis x2 visible
set axis y2 visible

set nox2tics
set noy2tics

fdir="../verification/data"

set multiplot
  set nodisplay

  # Histograms
  set xrange [0:4]
  set yrange [0:1.2]
  set xtics out 2
  set mxtics 0.5
  set ytics out 1.2
  set mytics out 0.2
  set xlabel "R*"
  set ylabel "\(\mathcal{P}\left(R*\right)\)"
  set key top right
  set origin 0,0
  plot fdir+"/RStarData.dat" using 1:2 with boxes style 3 notitle,\
       fdir+"/histogram.dat" using 1:3 with lines style 1 title "Quantum",\
       fdir+"/histogram.dat" using 1:2 with lines style 2 title "Uniform"
  
  # Updating
  set xrange [0:25]
  set yrange [0:1.05]
  set xtics out 25
  set mxtics 5
  set ytics out 1.0
  set mytics 0.2
  set xlabel "Detection events"
  set ylabel "Confidence"
  set key top right 0.4,-0.8
  set origin plot_w+h_pad,0
  plot 1 with lines style 4 notitle,\
       fdir+"/updating.dat" using 4:2 with lines style 1 \
       title "\(\mathcal{P}\left(\mathrm{Quantum}\right)\)",\
       fdir+"/updating.dat" using 4:3 with lines style 2\
       title "\(\mathcal{P}\left(\mathrm{Uniform}\right)\)"

  # Subfigure labels
  set xrange [0:1]
  set yrange [0:1]
  set axis x invisible
  set axis y invisible
  set axis x2 invisible
  set axis y2 invisible
  set origin 0,0
  set size fig_w
  set label 1 "(a)" at 0.20,0.48 with fontsize 1
  set label 2 "(b)" at 0.75,0.48 with fontsize 1
  plot
  
  set display
  refresh

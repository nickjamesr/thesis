set terminal pdf
set output "bigclouds.pdf"
set fontsize 0.9

fig_w=11.0
fig_m=fig_w/100.

h_pad=12*fig_m
v_pad=5*fig_m
plot_w=fig_w-2*h_pad
plot_h=25*fig_m

line_w=5*fig_m
line_dx=25*fig_m
line_dy=5*fig_m
key_dx=7*fig_m
key_dy=4*fig_m
text_dx=fig_m
text_dy=-4*fig_m

fdir="../verification/data/clouds"

quant_col=rgb(0.0,0.0,1.0)
class_col=rgb(1.0,0.0,0.0)

set style 1 colour quant_col pointtype 15
set style 2 colour class_col pointtype 15
set style 3 colour black pointtype 15

set multiplot
  set nodisplay

  set axis x nomirror
  set xtics out 2
  set mxtics out 1
  set axis x2 visible
  set nox2tics

  set axis y nomirror
  set ytics out 0.1
  set axis y2 visible
  set noy2tics
  
  set key top left

  set logscale y
  # 14x196
  set width 7*plot_w/15.
  set size ratio 15/7.*plot_h/plot_w
  set xformat auto horizontal
  set yrange [1e-5:1]
  set ytics out 1e-4,100
  set mytics out 10
  set ylabel "\(P \left(n_{\mathrm{left}}\right)\)"
  set origin 0,0
  plot fdir+"/14x196quantum.dat" using 1:3 with lines style 1 notitle,\
       fdir+"/14x196classical.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/14x196quantum.dat" using 1:3:4 with yerrorbars style 1 notitle,\
       fdir+"/14x196classical.dat" using 1:3:4 with yerrorbars style 2 notitle

  # 10x100
  set width plot_w/3.
  set size ratio 3*plot_h/plot_w
  set xformat auto horizontal
  set yrange [1e-4:1]
  set noylabel
  set origin 7*plot_w/15.+h_pad,0
  plot fdir+"/10x100quantum.dat" using 1:3 with lines style 1 notitle,\
       fdir+"/10x100classical.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/10x100quantum.dat" using 1:3:4 with yerrorbars style 1 notitle,\
       fdir+"/10x100classical.dat" using 1:3:4 with yerrorbars style 2 notitle

  # 6x36
  set width plot_w/5.
  set size ratio 5*plot_h/plot_w
  set xformat auto horizontal
  set noxlabel
  set yrange [1e-3:1]
  set ytics out 1e-2,100
  set mytics out 10
  set origin 4*plot_w/5.+2*h_pad,0
  plot fdir+"/6x36quantum.dat" using 1:3 with lines style 1 notitle,\
       fdir+"/6x36classical.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/6x36quantum.dat" using 1:3:4 with yerrorbars style 1 notitle,\
       fdir+"/6x36classical.dat" using 1:3:4 with yerrorbars style 2 notitle

  unset logscale y
  set noxlabel
  # 14x196
  set width 7*plot_w/15.
  set size ratio 15/7.*plot_h/plot_w
  set xformat ""
  set yrange [0:0.25]
  set ytics out 0.25
  set mytics out 0.05
  set ylabel "\(P \left(n_{\mathrm{left}}\right)\)"
  set origin 0,plot_h+v_pad
  plot fdir+"/14x196quantum.dat" using 1:3 with lines style 1 notitle,\
       fdir+"/14x196classical.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/14x196quantum.dat" using 1:3:4 with yerrorbars style 1 notitle,\
       fdir+"/14x196classical.dat" using 1:3:4 with yerrorbars style 2 notitle

  # 10x100
  set width plot_w/3.
  set size ratio 3*plot_h/plot_w
  set xformat ""
  set yrange [0:0.3+1e-5]
  set ytics out 0.1
  set mytics out 0.05
  set noylabel
  set origin 7*plot_w/15.+h_pad,plot_h+v_pad
  plot fdir+"/10x100quantum.dat" using 1:3 with lines style 1 notitle,\
       fdir+"/10x100classical.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/10x100quantum.dat" using 1:3:4 with yerrorbars style 1 notitle,\
       fdir+"/10x100classical.dat" using 1:3:4 with yerrorbars style 2 notitle

  # 6x36
  set width plot_w/5.
  set size ratio 5*plot_h/plot_w
  set xformat ""
  set yrange [0:0.4]
  set ytics out 0.2
  set mytics out 0.05
  set origin 4*plot_w/5.+2*h_pad,plot_h+v_pad
  plot fdir+"/6x36quantum.dat" using 1:3 with lines style 1 notitle,\
       fdir+"/6x36classical.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/6x36quantum.dat" using 1:3:4 with yerrorbars style 1 notitle,\
       fdir+"/6x36classical.dat" using 1:3:4 with yerrorbars style 2 notitle

  # Labels
  line from 0,2*plot_h+v_pad+line_dy to line_w,2*plot_h+v_pad+line_dy\
   with style 1
  text "Quantum" at key_dx,2*plot_h+v_pad+key_dy
  line from line_dx,2*plot_h+v_pad+line_dy to\
   line_dx+line_w,2*plot_h+v_pad+line_dy with style 2
  text "Classical" at line_dx+key_dx,2*plot_h+v_pad+key_dy
  
  text "(a)" at text_dx,2*plot_h+v_pad+text_dy
  text "(b)" at 7*plot_w/15.+h_pad+text_dx,2*plot_h+v_pad+text_dy
  text "(c)" at 4*plot_w/5.+2*h_pad+text_dx,2*plot_h+v_pad+text_dy
  text "(d)" at text_dx,plot_h+text_dy
  text "(e)" at 7*plot_w/15.+h_pad+text_dx,plot_h+text_dy
  text "(f)" at 4*plot_w/5.+2*h_pad+text_dx,plot_h+text_dy

  text "Number of photons detected in left half, \(n_{\mathrm{left}}\)"\
   at fig_w/2,-2*v_pad halign centre

  set display
  refresh
unset multiplot

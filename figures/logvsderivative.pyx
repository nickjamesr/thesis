set terminal pdf
set output "logvsderivative.pdf"

set fontsize 1.0

fig_w=10.2
fig_m=fig_w/100
plot_h=55*fig_m
left_w=66*fig_m
right_w=27.5*fig_m
h_pad=6.5*fig_m

set style 1 color red fillcolor rgb(1.0,0.7,0.7)
set style 2 color blue fillcolor rgb(0.7,0.7,1.0)
set style 3 color green fillcolor rgb(0.6,0.8,0.6)

set style 4 color red pointtype 17 pointsize 0.5
set style 5 color blue pointtype 17 pointsize 0.5
set style 6 color green pointtype 17 pointsize 0.5

prefix="../hamiltomo/data"

set multiplot
  set nodisplay

  # Large timestep
  set origin 0,0
  set width left_w
  set size ratio plot_h/left_w
  set ylabel "Fidelity (trace distance)"
  set xtics 1,4
  set mxtics 1
  set logscale y
  set yrange [1e-2:50]
  plot prefix+"/comparison00.dat" u 1:($4-$5):($4+$5) with yerrorshaded\
        style 1 notitle,\
       prefix+"/comparison01.dat" u 1:($4-$5):($4+$5) with yerrorshaded\
        style 2 notitle,\
       prefix+"/comparison02.dat" u 1:($4-$5):($4+$5) with yerrorshaded\
        style 3 notitle,\
       prefix+"/comparison00.dat" u 1:2:3 with yerrorbars style 4\
        title "\(10^{-3}\)",\
       prefix+"/comparison00.dat" u 1:2 with points style 4 notitle,\
       prefix+"/comparison00.dat" u 1:2 with lines style 4 notitle,\
       prefix+"/comparison01.dat" u 1:2:3 with yerrorbars style 5\
        title "\(10^{-2}\)",\
       prefix+"/comparison01.dat" u 1:2 with points style 5 notitle,\
       prefix+"/comparison01.dat" u 1:2 with lines style 5 notitle,\
       prefix+"/comparison03.dat" u 1:2:3 with yerrorbars style 6\
        title "\(10^{-1}\)",\
       prefix+"/comparison03.dat" u 1:2 with points style 6 notitle,\
       prefix+"/comparison03.dat" u 1:2 with lines style 6 notitle
 
  # Small timestep
  set origin left_w+h_pad,0
  set width right_w
  set size ratio plot_h/right_w
  set axis y right
  set yrange [1e-4:0.5]
  set noxlabel
  set noylabel
  plot prefix+"/comparison04.dat" u 1:($4-$5):($4+$5) with yerrorshaded\
        style 1 notitle,\
       prefix+"/comparison05.dat" u 1:($4-$5):($4+$5) with yerrorshaded\
        style 2 notitle,\
       prefix+"/comparison06.dat" u 1:($4-$5):($4+$5) with yerrorshaded\
        style 3 notitle,\
       prefix+"/comparison04.dat" u 1:2:3 with yerrorbars style 4\
        title "\(10^{-6}\)",\
       prefix+"/comparison04.dat" u 1:2 with points style 4 notitle,\
       prefix+"/comparison04.dat" u 1:2 with lines style 4 notitle,\
       prefix+"/comparison05.dat" u 1:2:3 with yerrorbars style 5\
        title "\(10^{-5}\)",\
       prefix+"/comparison05.dat" u 1:2 with points style 5 notitle,\
       prefix+"/comparison05.dat" u 1:2 with lines style 5 notitle,\
       prefix+"/comparison06.dat" u 1:2:3 with yerrorbars style 6\
        title "\(10^{-4}\)",\
       prefix+"/comparison06.dat" u 1:2 with points style 6 notitle,\
       prefix+"/comparison06.dat" u 1:2 with lines style 6 notitle,\
       prefix+"/comparison06.dat" u 1:2 with lines style 6 notitle

  # x axis label
  text "Number of terms, \(n\)" at 50*fig_m,-10*fig_m halign centre
  
  # subfigure labels
  text "(a) \(\delta t=0.5\)" at left_w/2,plot_h+3*fig_m halign centre
  text "(b) \(\delta t=0.05\)" at left_w+h_pad+right_w/2,plot_h+3*fig_m \
   halign centre
  
  set display
  refresh
unset multiplot

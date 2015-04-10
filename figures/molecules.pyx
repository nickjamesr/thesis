set terminal pdf
set output "molecules.pdf"

set fontsize 0.8

fig_w=11.3
fig_m=fig_w/100.
plot_h=20*fig_m
v_pad=5*fig_m
offset=10*fig_m
fig_h=4*plot_h+2*offset+2*v_pad
text_dx=1*fig_m
text_dy=-3*fig_m

set grid x

set style 1 linewidth 0.1 colour rgb(0.6,0.8,0.6) fillcolour rgb(0.7,0.8,0.6)
set style 2 pointtype 15 pointsize 0.6 linewidth 0.8 colour green
set style 3 linewidth 0.1 colour rgb(0.7,0.7,1.0) fillcolour rgb(0.7,0.7,1.0)
set style 4 pointtype 15 pointsize 0.6 linewidth 0.8 colour blue

ocs="../scatterbox/molecules/data/OCS"
co2="../scatterbox/molecules/data/CO2"

set axis x nomirror
set xrange [0:0.01]
set xtics out 0.01
set mxtics out 0.002
set axis y nomirror
set yrange [0:0.6]
set ytics out 0.6
set mytics out 0.2
set axis x2 visible
set nox2tics
set axis y2 visible
set noy2tics

set multiplot
  set nodisplay

##### COINCIDENCES
  pair_w=30*fig_m
  h_pad=5*fig_m
  set width pair_w
  set size ratio plot_h/pair_w

  ### AB
  set origin 0,plot_h+v_pad
  set xformat ""
  set yformat auto horizontal
  plot ocs+"/quantum_ideal.dat" using 1:8:9 with yerrorshaded style 1 notitle,\
       co2+"/quantum_ideal.dat" using 1:8:9 with yerrorshaded style 3 notitle,\
       ocs+"/quantum_ideal.dat" using 1:2 with lines style 2 notitle,\
       co2+"/quantum_ideal.dat" using 1:2 with lines style 4 notitle,\
       ocs+"/quantum.dat" using 1:2 with points style 2 notitle,\
       co2+"/quantum.dat" using 1:2 with points style 4 notitle
  
  ### AC
  set origin pair_w+h_pad,plot_h+v_pad
  set xformat ""
  set yformat ""
  plot ocs+"/quantum_ideal.dat" using 1:10:11 with yerrorshaded style 1\
       notitle,\
       co2+"/quantum_ideal.dat" using 1:10:11 with yerrorshaded style 3\
       notitle,\
       ocs+"/quantum_ideal.dat" using 1:3 with lines style 2 notitle,\
       co2+"/quantum_ideal.dat" using 1:3 with lines style 4 notitle,\
       ocs+"/quantum.dat" using 1:3 with points style 2 notitle,\
       co2+"/quantum.dat" using 1:3 with points style 4 notitle
  
  ### AD
  set origin 2*(pair_w+h_pad),plot_h+v_pad
  set xformat ""
  set yformat ""
  plot ocs+"/quantum_ideal.dat" using 1:12:13 with yerrorshaded style 1\
       notitle,\
       co2+"/quantum_ideal.dat" using 1:12:13 with yerrorshaded style 3\
       notitle,\
       ocs+"/quantum_ideal.dat" using 1:4 with lines style 2 notitle,\
       co2+"/quantum_ideal.dat" using 1:4 with lines style 4 notitle,\
       ocs+"/quantum.dat" using 1:4 with points style 2 notitle,\
       co2+"/quantum.dat" using 1:4 with points style 4 notitle
  
  ### BC
  set origin 0,0
  set xformat auto horizontal
  set yformat auto horizontal
  plot ocs+"/quantum_ideal.dat" using 1:14:15 with yerrorshaded style 1\
       notitle,\
       co2+"/quantum_ideal.dat" using 1:14:15 with yerrorshaded style 3\
       notitle,\
       ocs+"/quantum_ideal.dat" using 1:5 with lines style 2 notitle,\
       co2+"/quantum_ideal.dat" using 1:5 with lines style 4 notitle,\
       ocs+"/quantum.dat" using 1:5 with points style 2 notitle,\
       co2+"/quantum.dat" using 1:5 with points style 4 notitle
  
  ### BD
  set origin pair_w+h_pad,0
  set xformat auto horizontal
  set yformat ""
  plot ocs+"/quantum_ideal.dat" using 1:16:17 with yerrorshaded style 1\
       notitle,\
       co2+"/quantum_ideal.dat" using 1:16:17 with yerrorshaded style 3\
       notitle,\
       ocs+"/quantum_ideal.dat" using 1:6 with lines style 2 notitle,\
       co2+"/quantum_ideal.dat" using 1:6 with lines style 4 notitle,\
       ocs+"/quantum.dat" using 1:6 with points style 2 notitle,\
       co2+"/quantum.dat" using 1:6 with points style 4 notitle
  
  ### CD
  set origin 2*(pair_w+h_pad),0
  set xformat auto horizontal
  set yformat ""
  plot ocs+"/quantum_ideal.dat" using 1:18:19 with yerrorshaded style 1\
       notitle,\
       co2+"/quantum_ideal.dat" using 1:18:19 with yerrorshaded style 3\
       notitle,\
       ocs+"/quantum_ideal.dat" using 1:7 with lines style 2 notitle,\
       co2+"/quantum_ideal.dat" using 1:7 with lines style 4 notitle,\
       ocs+"/quantum.dat" using 1:7 with points style 2 notitle,\
       co2+"/quantum.dat" using 1:7 with points style 4 notitle

##### SINGLES
  plot_w=21.25*fig_m
  h_pad=5*fig_m
  plot_h=20*fig_m
  set width plot_w
  set size ratio plot_h/plot_w

  ### trit A
  set origin 0,2*plot_h+v_pad+offset
  set xformat auto horizontal
  set yformat auto horizontal
  plot ocs+"/trit_ideal.dat" using 1:6:7 with yerrorshaded style 1 notitle,\
       co2+"/trit_ideal.dat" using 1:6:7 with yerrorshaded style 3 notitle,\
       ocs+"/trit_ideal.dat" using 1:2 with lines style 2 notitle,\
       co2+"/trit_ideal.dat" using 1:2 with lines style 4 notitle,\
       ocs+"/trit.dat" using 1:2 with points style 2 notitle,\
       co2+"/trit.dat" using 1:2 with points style 4 notitle
  
  ### trit B
  set origin plot_w+h_pad,2*plot_h+v_pad+offset
  set xformat auto horizontal
  set yformat ""
  plot ocs+"/trit_ideal.dat" using 1:8:9 with yerrorshaded style 1 notitle,\
       co2+"/trit_ideal.dat" using 1:8:9 with yerrorshaded style 3 notitle,\
       ocs+"/trit_ideal.dat" using 1:3 with lines style 2 notitle,\
       co2+"/trit_ideal.dat" using 1:3 with lines style 4 notitle,\
       ocs+"/trit.dat" using 1:3 with points style 2 notitle,\
       co2+"/trit.dat" using 1:3 with points style 4 notitle
  
  ### trit C
  set origin 2*(plot_w+h_pad),2*plot_h+v_pad+offset
  set xformat auto horizontal
  set yformat ""
  plot ocs+"/trit_ideal.dat" using 1:10:11 with yerrorshaded style 1 notitle,\
       co2+"/trit_ideal.dat" using 1:10:11 with yerrorshaded style 3 notitle,\
       ocs+"/trit_ideal.dat" using 1:4 with lines style 2 notitle,\
       co2+"/trit_ideal.dat" using 1:4 with lines style 4 notitle,\
       ocs+"/trit.dat" using 1:4 with points style 2 notitle,\
       co2+"/trit.dat" using 1:4 with points style 4 notitle
  
  ### trit D
  set origin 3*(plot_w+h_pad),2*plot_h+v_pad+offset
  set xformat auto horizontal
  set yformat ""
  plot ocs+"/trit_ideal.dat" using 1:12:13 with yerrorshaded style 1 notitle,\
       co2+"/trit_ideal.dat" using 1:12:13 with yerrorshaded style 3 notitle,\
       ocs+"/trit_ideal.dat" using 1:5 with lines style 2 notitle,\
       co2+"/trit_ideal.dat" using 1:5 with lines style 4 notitle,\
       ocs+"/trit.dat" using 1:5 with points style 2 notitle,\
       co2+"/trit.dat" using 1:5 with points style 4 notitle
 
  set yrange [0:0.8]
  set ytics out 0.8
  ### quart A
  set origin 0,3*plot_h+2*offset+v_pad
  set xformat auto horizontal
  set yformat auto horizontal
  plot ocs+"/quart_ideal.dat" using 1:6:7 with yerrorshaded style 1 notitle,\
       co2+"/quart_ideal.dat" using 1:6:7 with yerrorshaded style 3 notitle,\
       ocs+"/quart_ideal.dat" using 1:2 with lines style 2 notitle,\
       co2+"/quart_ideal.dat" using 1:2 with lines style 4 notitle,\
       ocs+"/quart.dat" using 1:2 with points style 2 notitle,\
       co2+"/quart.dat" using 1:2 with points style 4 notitle
  
  ### quart B
  set origin plot_w+h_pad,3*plot_h+2*offset+v_pad
  set xformat auto horizontal
  set yformat ""
  plot ocs+"/quart_ideal.dat" using 1:8:9 with yerrorshaded style 1 notitle,\
       co2+"/quart_ideal.dat" using 1:8:9 with yerrorshaded style 3 notitle,\
       ocs+"/quart_ideal.dat" using 1:3 with lines style 2 notitle,\
       co2+"/quart_ideal.dat" using 1:3 with lines style 4 notitle,\
       ocs+"/quart.dat" using 1:3 with points style 2 notitle,\
       co2+"/quart.dat" using 1:3 with points style 4 notitle
  
  ### quart C
  set origin 2*(plot_w+h_pad),3*plot_h+2*offset+v_pad
  set xformat auto horizontal
  set yformat ""
  plot ocs+"/quart_ideal.dat" using 1:10:11 with yerrorshaded style 1 notitle,\
       co2+"/quart_ideal.dat" using 1:10:11 with yerrorshaded style 3 notitle,\
       ocs+"/quart_ideal.dat" using 1:4 with lines style 2 notitle,\
       co2+"/quart_ideal.dat" using 1:4 with lines style 4 notitle,\
       ocs+"/quart.dat" using 1:4 with points style 2 notitle,\
       co2+"/quart.dat" using 1:4 with points style 4 notitle
  
  ### quart D
  set origin 3*(plot_w+h_pad),3*plot_h+2*offset+v_pad
  set xformat auto horizontal
  set yformat ""
  plot ocs+"/quart_ideal.dat" using 1:12:13 with yerrorshaded style 1 notitle,\
       co2+"/quart_ideal.dat" using 1:12:13 with yerrorshaded style 3 notitle,\
       ocs+"/quart_ideal.dat" using 1:5 with lines style 2 notitle,\
       co2+"/quart_ideal.dat" using 1:5 with lines style 4 notitle,\
       ocs+"/quart.dat" using 1:5 with points style 2 notitle,\
       co2+"/quart.dat" using 1:5 with points style 4 notitle

##### SUBFIGURE LABELS
  set origin -2*h_pad,0
  set width fig_w
  set size ratio fig_h/fig_w
  set xrange [0:1]
  set yrange [0:1]
  set axis x invisible
  set axis x2 invisible
  set axis y invisible
  set axis y2 invisible
  set label 1 "(a)" at 0,0.98 with fontsize 1.0
  set label 2 "(b)" at 0,0.71 with fontsize 1.0
  set label 3 "(c)" at 0,0.43 with fontsize 1.0
  plot

##### AXIS LABELS
  text "time /(cm/\(c\))" at pair_w/2,-v_pad halign centre
  text "time /(cm/\(c\))" at pair_w+h_pad+pair_w/2,-v_pad halign centre
  text "time /(cm/\(c\))" at 2*(pair_w+h_pad)+pair_w/2,-v_pad halign centre
  text "\(t\)" at plot_w/2,2*plot_h+offset halign centre
  text "\(t\)" at plot_w/2+plot_w+h_pad,2*plot_h+offset halign centre
  text "\(t\)" at plot_w/2+2*(plot_w+h_pad),2*plot_h+offset halign centre
  text "\(t\)" at plot_w/2+3*(plot_w+h_pad),2*plot_h+offset halign centre
  text "\(t\)" at plot_w/2,3*plot_h+2*offset halign centre
  text "\(t\)" at plot_w/2+plot_w+h_pad,3*plot_h+2*offset halign centre
  text "\(t\)" at plot_w/2+2*(plot_w+h_pad),3*plot_h+2*offset halign centre
  text "\(t\)" at plot_w/2+3*(plot_w+h_pad),3*plot_h+2*offset halign centre
  text "\(P\)" at -h_pad,plot_h/2 valign centre
  text "\(P\)" at -h_pad,plot_h+h_pad+plot_h/2 valign centre
  text "\(P\)" at -h_pad,2*plot_h+h_pad+offset+plot_h/2 valign centre
  text "\(P\)" at -h_pad,3*plot_h+h_pad+2*offset+plot_h/2 valign centre

##### MODE LABELS
  text "AB" at text_dx,2*plot_h+v_pad+text_dy
  text "AC" at pair_w+h_pad+text_dx,2*plot_h+v_pad+text_dy
  text "AD" at 2*(pair_w+h_pad)+text_dx,2*plot_h+v_pad+text_dy
  text "BC" at text_dx,plot_h+text_dy
  text "AC" at pair_w+h_pad+text_dx,plot_h+text_dy
  text "AD" at 2*(pair_w+h_pad)+text_dx,plot_h+text_dy
  text "A" at text_dx,4*plot_h+v_pad+2*offset+text_dy
  text "B" at plot_w+h_pad+text_dx,4*plot_h+v_pad+2*offset+text_dy
  text "C" at 2*(plot_w+h_pad)+text_dx,4*plot_h+v_pad+2*offset+text_dy
  text "D" at 3.2*plot_w+3*h_pad+text_dx,4*plot_h+v_pad+2*offset+text_dy
  text "A" at text_dx,3*plot_h+v_pad+offset+text_dy
  text "B" at 1.2*plot_w+h_pad+text_dx,3*plot_h+v_pad+offset+text_dy
  text "C" at 2*(plot_w+h_pad)+text_dx,3*plot_h+v_pad+offset+text_dy
  text "D" at 3*(plot_w+h_pad)+text_dx,3*plot_h+v_pad+offset+text_dy
  set display
  refresh
unset multiplot

#!/usr/local/bin/pyxplot

set fontsize 0.8

set style 1 points colour red pointtype 15 pointsize 0.5
set style 2 points colour green pointtype 15 pointsize 0.5
set style 3 points colour blue pointtype 15 pointsize 0.5
set style 4 points colour purple pointtype 15 pointsize 0.5
set style 5 lines colour red
set style 6 lines colour green
set style 7 lines colour blue
set style 8 lines colour purple
set style 9 lines linetype 2 colour black

set terminal pdf
set output "twosite.pdf"

set axis y1 nomirror
set axis y2 nomirror
set axis x2 nomirror
set nox2tics

plot_w=3.6
plot_h=3.
h_pad=0.5   # space between columns
v_pad=1.3   # space between rows
fig_w=3*plot_w+2*h_pad
fig_m=fig_w/100
fig_h=2*plot_h+v_pad

text_dx=0.5
text_dy=0.5
line_w=0.5
line_dx=1.8
line_dy=0.5
key_dx=0.7
key_dy=0.35

set y2range [0:*]
set yrange [0:1]
set noy2tics

set multiplot
  set nodisplay
  set size ratio plot_h/plot_w
  set width plot_w

### SINGLES 
  set xtics out 5
  set mxtics out 1
  set xformat ""
  set ytics out 0.5
  set mytics out 0.25

  fdir="../pt/data/symmetric"
  set origin 0,plot_h+v_pad
  set xrange [0:10.0611]
  plot fdir+"/quart.dat" using 1:5:9 with style 1 notitle, \
       fdir+"/quart.dat" using 1:6:10 with style 2 notitle, \
       fdir+"/quart.dat" using 1:7:11 with style 3 notitle, \
       fdir+"/quart.dat" using 1:8:12 with style 4 notitle, \
       fdir+"/theory.dat" using 1:5 with style 5 notitle, \
       fdir+"/theory.dat" using 1:6 with style 6 notitle, \
       fdir+"/theory.dat" using 1:7 with style 7 notitle, \
       fdir+"/theory.dat" using 1:8 with style 8 notitle, \
       fdir+"/theory.dat" using 1:4 with style 9 notitle axes x1y2

  set yformat ""

  fdir="../pt/data/critical"
  set origin plot_w+h_pad,plot_h+v_pad
  set xrange [0:10]
  plot fdir+"/quart.dat" using 1:5:9 with style 1 notitle, \
       fdir+"/quart.dat" using 1:6:10 with style 2 notitle, \
       fdir+"/quart.dat" using 1:7:11 with style 3 notitle, \
       fdir+"/quart.dat" using 1:8:12 with style 4 notitle, \
       fdir+"/theory.dat" using 1:5 with style 5 notitle, \
       fdir+"/theory.dat" using 1:6 with style 6 notitle, \
       fdir+"/theory.dat" using 1:7 with style 7 notitle, \
       fdir+"/theory.dat" using 1:8 with style 8 notitle, \
       fdir+"/theory.dat" using 1:4 with style 9 notitle axes x1y2

  fdir="../pt/data/broken"
  set origin 2*(plot_w+h_pad),plot_h+v_pad
  set xrange [0:10.0]
  set key outside
  plot fdir+"/quart.dat" using 1:5:9 with style 1 notitle, \
       fdir+"/quart.dat" using 1:6:10 with style 2 notitle, \
       fdir+"/quart.dat" using 1:7:11 with style 3 notitle, \
       fdir+"/quart.dat" using 1:8:12 with style 4 notitle, \
       fdir+"/theory.dat" using 1:5 with style 5 notitle, \
       fdir+"/theory.dat" using 1:6 with style 6 notitle, \
       fdir+"/theory.dat" using 1:7 with style 7 notitle, \
       fdir+"/theory.dat" using 1:8 with style 8 notitle, \
       fdir+"/theory.dat" using 1:4 with style 9 notitle axes x1y2

### COINCIDENCES
  set xtics out 5
  set xformat auto horizontal
  set ytics out 0.25
  set yformat auto horizontal
  set yrange [0:0.75]

  fdir="../pt/data/symmetric"
  set origin 0,0
  set xrange [0:10.0611]
  plot fdir+"/quantum.dat" using 1:5:11 with style 1 notitle, \
       fdir+"/quantum.dat" using 1:6:12 with style 2 notitle, \
       fdir+"/quantum.dat" using 1:7:13 with style 3 notitle, \
       fdir+"/theory.dat" using 1:9 with style 5 notitle, \
       fdir+"/theory.dat" using 1:10 with style 6 notitle, \
       fdir+"/theory.dat" using 1:11 with style 7 notitle, \
       fdir+"/theory.dat" using 1:4 with style 9 notitle axes x1y2

  set yformat ""

  fdir="../pt/data/critical"
  set origin plot_w+h_pad,0
  set xrange [0:10.0]
  plot fdir+"/quantum.dat" using 1:5:11 with style 1 notitle, \
       fdir+"/quantum.dat" using 1:6:12 with style 2 notitle, \
       fdir+"/quantum.dat" using 1:7:13 with style 3 notitle, \
       fdir+"/theory.dat" using 1:9 with style 5 notitle, \
       fdir+"/theory.dat" using 1:10 with style 6 notitle, \
       fdir+"/theory.dat" using 1:11 with style 7 notitle, \
       fdir+"/theory.dat" using 1:4 with style 9 notitle axes x1y2

  set origin 2*(plot_w+h_pad),0
  set xrange [0:10.0]
  plot fdir+"/quantum.dat" using 1:5:11 with style 1 notitle, \
       fdir+"/quantum.dat" using 1:6:12 with style 2 notitle, \
       fdir+"/quantum.dat" using 1:7:13 with style 3 notitle, \
       fdir+"/theory.dat" using 1:9 with style 5 notitle, \
       fdir+"/theory.dat" using 1:10 with style 6 notitle,\
       fdir+"/theory.dat" using 1:11 with style 7 notitle,\
       fdir+"/theory.dat" using 1:4 with style 9 notitle axes x1y2

  # Key
  line from 0,fig_h+line_dy to line_w,fig_h+line_dy with style 5
  text "\(S_{1}\)" at key_dx,fig_h+key_dy
  line from line_dx,fig_h+line_dy to line_dx+line_w,fig_h+line_dy with style 6
  text "\(S_{2}\)" at line_dx+key_dx,fig_h+key_dy
  line from 2*line_dx,fig_h+line_dy to 2*line_dx+line_w,fig_h+line_dy\
    with style 7
  text "\(E_{1}\)" at 2*line_dx+key_dx,fig_h+key_dy
  line from 3*line_dx,fig_h+line_dy to 3*line_dx+line_w,fig_h+line_dy\
    with style 8
  text "\(E_{2}\)" at 3*line_dx+key_dx,fig_h+key_dy
  line from 4*line_dx,fig_h+line_dy to 4*line_dx+line_w,fig_h+line_dy\
    with style 9
  text "scale" at 4*line_dx+key_dx,fig_h+key_dy

  line from 0*line_dx,plot_h+line_dy to 0*line_dx+line_w,plot_h+line_dy\
    with style 5
  text "\(S_{1}S_{2}\)" at 0*line_dx+key_dx,plot_h+key_dy
  line from 1*line_dx,plot_h+line_dy to 1*line_dx+line_w,plot_h+line_dy\
    with style 6
  text "\(S_{1}E_{1}\)" at 1*line_dx+key_dx,plot_h+key_dy
  line from 2*line_dx,plot_h+line_dy to 2*line_dx+line_w,plot_h+line_dy\
    with style 7
  text "\(S_{1}E_{2}\)" at 2*line_dx+key_dx,plot_h+key_dy
  line from 3*line_dx,plot_h+line_dy to 3*line_dx+line_w,plot_h+line_dy\
    with style 9
  text "scale" at 3*line_dx+key_dx,plot_h+key_dy

  # Subfigure labels
  set origin 0,0
  set width fig_w
  set size ratio fig_h/fig_w
  set xrange [0:fig_w]
  set yrange [0:fig_h]
  set axis x invisible
  set axis y invisible
  set axis x2 invisible
  set axis y2 invisible
  set label 1 "(a)" at text_dx,2*plot_h+v_pad-text_dy with fontsize 1
  set label 2 "(b)" at plot_w+h_pad+text_dx,2*plot_h+v_pad-text_dy\
    with fontsize 1
  set label 3 "(c)" at 2*(plot_w+h_pad)+text_dx,2*plot_h+v_pad-text_dy\
    with fontsize 1
  set label 4 "(d)" at text_dx,plot_h-text_dy with fontsize 1
  set label 5 "(e)" at plot_w+h_pad+text_dx,plot_h-text_dy\
    with fontsize 1
  set label 6 "(f)" at 2*(plot_w+h_pad)+text_dx,plot_h-text_dy\
    with fontsize 1
  plot

  set display
  refresh
unset multiplot

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
plot_h=3
h_pad=0.5   # space between columns
v_pad=0.5   # space between rows

text_dx=0.5
text_dy=0.5

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
       fdir+"/theory.dat" using 1:5 with style 5 title "\(S_1\)", \
       fdir+"/theory.dat" using 1:6 with style 6 title "\(S_2\)", \
       fdir+"/theory.dat" using 1:7 with style 7 title "\(E_1\)", \
       fdir+"/theory.dat" using 1:8 with style 8 title "\(E_2\)", \
       fdir+"/theory.dat" using 1:4 with style 9 title "scale" axes x1y2

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
       fdir+"/theory.dat" using 1:9 with style 5 title "\(S_{1}S_{2}\)", \
       fdir+"/theory.dat" using 1:10 with style 6 title "\(S_{1}E_{1}\)",\
       fdir+"/theory.dat" using 1:11 with style 7 title "\(S_{1}E_{2}\)",\
       fdir+"/theory.dat" using 1:4 with style 9 title "scale" axes x1y2

  text "\textbf{(a)}" at text_dx,2*plot_h+v_pad-text_dy
  text "\textbf{(b)}" at plot_w+h_pad+text_dx,2*plot_h+v_pad-text_dy
  text "\textbf{(c)}" at 2*(plot_w+h_pad)+text_dx,2*plot_h+v_pad-text_dy
  text "\textbf{(d)}" at text_dx,plot_h-text_dy
  text "\textbf{(e)}" at plot_w+h_pad+text_dx,plot_h-text_dy
  text "\textbf{(f)}" at 2*(plot_w+h_pad)+text_dx,plot_h-text_dy

  set display
  refresh
unset multiplot

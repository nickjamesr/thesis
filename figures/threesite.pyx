set terminal pdf
set output "threesite_singles.pdf"

fig_w=10.5
fig_m=fig_w/100.

plot_w=30*fig_m
plot_h=20*fig_m
h_pad=5*fig_m
v_pad=10*fig_m
v_gap=25*fig_m
sub_h=2*plot_h+v_pad

line_dy=3*fig_m
line_dx=20*fig_m
line_w=5*fig_m
key_dx=line_w+2*fig_m
key_dy=line_dy-fig_m

set width plot_w
set size ratio plot_h/plot_w

set style 1 colour black linetype 2
set style 2 colour red pointtype 15 pointsize 0.5
set style 3 colour blue pointtype 15 pointsize 0.5
set style 4 colour green pointtype 15 pointsize 0.5
set style 5 colour red linetype 2
set style 6 colour blue linetype 2
set style 7 colour green linetype 2

set axis x nomirror
set axis y nomirror
set axis x2 visible
set nox2tics
set axis y2 nomirror

###-------------------------------SINGLES------------------------------------###

set multiplot
  set nodisplay

### SYMMETRIC
  fdir="../pt/data/threesite/symmetric"
  set xrange [0:5.135]
  set xtics out 5
  set mxtics out 1
  set yrange [0:1]
  set ytics out 1
  set mytics out 0.2
  set y2range [0:4]
  set y2tics out 4
  set my2tics out 1
  
  # SYSTEM
  # Symmetric, inject 0
  set xformat ""
  set yformat auto horizontal
  set y2format ""
  set origin 0,sub_h+v_gap+plot_h+v_pad
  plot fdir+"/theory/singles0.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\ 
       fdir+"/theory/singles0.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/theory/singles0.dat" using 1:4 with lines style 3 notitle,\
       fdir+"/theory/singles0.dat" using 1:5 with lines style 4 notitle,\
       fdir+"/experimental/singles0.dat" using 1:2 with point style 2 notitle,\
       fdir+"/experimental/singles0.dat" using 1:3 with point style 3 notitle,\
       fdir+"/experimental/singles0.dat" using 1:4 with point style 4 notitle

  # Symmetric, inject 1
  set xformat ""
  set yformat ""
  set y2format ""
  set origin plot_w+h_pad,sub_h+v_gap+plot_h+v_pad
  plot fdir+"/theory/singles1.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/singles1.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/theory/singles1.dat" using 1:4 with lines style 3 notitle,\
       fdir+"/theory/singles1.dat" using 1:5 with lines style 4 notitle,\
       fdir+"/experimental/singles1.dat" using 1:2 with point style 2 notitle,\
       fdir+"/experimental/singles1.dat" using 1:3 with point style 3 notitle,\
       fdir+"/experimental/singles1.dat" using 1:4 with point style 4 notitle

  # Symmetric, inject 2
  set xformat ""
  set yformat ""
  set y2format auto horizontal
  set origin 2*(plot_w+h_pad),sub_h+v_gap+plot_h+v_pad
  plot fdir+"/theory/singles2.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/singles2.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/theory/singles2.dat" using 1:4 with lines style 3 notitle,\
       fdir+"/theory/singles2.dat" using 1:5 with lines style 4 notitle,\
       fdir+"/experimental/singles2.dat" using 1:2 with point style 2 notitle,\
       fdir+"/experimental/singles2.dat" using 1:3 with point style 3 notitle,\
       fdir+"/experimental/singles2.dat" using 1:4 with point style 4 notitle

  # Key
  line from 0,sub_h+v_gap+2*plot_h+v_pad+line_dy to\
            line_w,sub_h+v_gap+2*plot_h+v_pad+line_dy with style 1
  line from line_dx,sub_h+v_gap+2*plot_h+v_pad+line_dy to\
            line_dx+line_w,sub_h+v_gap+2*plot_h+v_pad+line_dy with style 2
  line from 2*line_dx,sub_h+v_gap+2*plot_h+v_pad+line_dy to\
            2*line_dx+line_w,sub_h+v_gap+2*plot_h+v_pad+line_dy with style 3
  line from 3*line_dx,sub_h+v_gap+2*plot_h+v_pad+line_dy to\
            3*line_dx+line_w,sub_h+v_gap+2*plot_h+v_pad+line_dy with style 4
  text "scale" at key_dx,sub_h+v_gap+2*plot_h+v_pad+key_dy
  text "\(S_{0}\)" at line_dx+key_dx,sub_h+v_gap+2*plot_h+v_pad+key_dy
  text "\(S_{1}\)" at 2*line_dx+key_dx,sub_h+v_gap+2*plot_h+v_pad+key_dy
  text "\(S_{2}\)" at 3*line_dx+key_dx,sub_h+v_gap+2*plot_h+v_pad+key_dy
  
  # ENVIRONMENT
  # Symmetric, inject 0
  set xformat auto horizontal
  set yformat auto horizontal
  set y2format ""
  set origin 0,sub_h+v_gap+0
  plot fdir+"/theory/singles0.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\ 
       fdir+"/theory/singles0.dat" using 1:6 with lines style 5 notitle,\
       fdir+"/theory/singles0.dat" using 1:7 with lines style 6 notitle,\
       fdir+"/theory/singles0.dat" using 1:8 with lines style 7 notitle,\
       fdir+"/experimental/singles0.dat" using 1:5 with point style 2 notitle,\
       fdir+"/experimental/singles0.dat" using 1:6 with point style 3 notitle,\
       fdir+"/experimental/singles0.dat" using 1:7 with point style 4 notitle

  # Symmetric, inject 1
  set xformat auto horizontal
  set yformat ""
  set y2format ""
  set origin plot_w+h_pad,sub_h+v_gap+0
  plot fdir+"/theory/singles1.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/singles1.dat" using 1:6 with lines style 5 notitle,\
       fdir+"/theory/singles1.dat" using 1:7 with lines style 6 notitle,\
       fdir+"/theory/singles1.dat" using 1:8 with lines style 7 notitle,\
       fdir+"/experimental/singles1.dat" using 1:5 with point style 2 notitle,\
       fdir+"/experimental/singles1.dat" using 1:6 with point style 3 notitle,\
       fdir+"/experimental/singles1.dat" using 1:7 with point style 4 notitle

  # Symmetric, inject 2
  set xformat auto horizontal
  set yformat ""
  set y2format auto horizontal
  set origin 2*(plot_w+h_pad),sub_h+v_gap+0
  plot fdir+"/theory/singles2.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/singles2.dat" using 1:6 with lines style 5 notitle,\
       fdir+"/theory/singles2.dat" using 1:7 with lines style 6 notitle,\
       fdir+"/theory/singles2.dat" using 1:8 with lines style 7 notitle,\
       fdir+"/experimental/singles2.dat" using 1:5 with point style 2 notitle,\
       fdir+"/experimental/singles2.dat" using 1:6 with point style 3 notitle,\
       fdir+"/experimental/singles2.dat" using 1:7 with point style 4 notitle
 
  # Key
  line from 0,sub_h+v_gap+plot_h+line_dy to\
            line_w,sub_h+v_gap+plot_h+line_dy with style 1
  line from line_dx,sub_h+v_gap+plot_h+line_dy to\
            line_dx+line_w,sub_h+v_gap+plot_h+line_dy with style 5
  line from 2*line_dx,sub_h+v_gap+plot_h+line_dy to\
            2*line_dx+line_w,sub_h+v_gap+plot_h+line_dy with style 6
  line from 3*line_dx,sub_h+v_gap+plot_h+line_dy to\
            3*line_dx+line_w,sub_h+v_gap+plot_h+line_dy with style 7
  text "scale" at key_dx,sub_h+v_gap+plot_h+key_dy
  text "\(E_{0}\)" at line_dx+key_dx,sub_h+v_gap+plot_h+key_dy
  text "\(E_{1}\)" at 2*line_dx+key_dx,sub_h+v_gap+plot_h+key_dy
  text "\(E_{2}\)" at 3*line_dx+key_dx,sub_h+v_gap+plot_h+key_dy

### BROKEN
  fdir="../pt/data/threesite/broken"
  set xrange [0:6]
  set xtics out 6
  set mxtics out 1
  set yrange [0:1]
  set ytics out 1
  set mytics out 0.2
  set logscale y2
  set y2range [1:200]
  set y2tics out 100
  set my2tics out 10
  
  # SYSTEM
  # Broken, inject 0
  set xformat ""
  set yformat auto horizontal
  set y2format ""
  set origin 0,plot_h+v_pad
  plot fdir+"/theory/singles0.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\ 
       fdir+"/theory/singles0.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/theory/singles0.dat" using 1:4 with lines style 3 notitle,\
       fdir+"/theory/singles0.dat" using 1:5 with lines style 4 notitle,\
       fdir+"/experimental/singles0.dat" using 1:2 with point style 2 notitle,\
       fdir+"/experimental/singles0.dat" using 1:3 with point style 3 notitle,\
       fdir+"/experimental/singles0.dat" using 1:4 with point style 4 notitle

  # Broken, inject 1
  set xformat ""
  set yformat ""
  set y2format ""
  set origin plot_w+h_pad,plot_h+v_pad
  plot fdir+"/theory/singles1.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/singles1.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/theory/singles1.dat" using 1:4 with lines style 3 notitle,\
       fdir+"/theory/singles1.dat" using 1:5 with lines style 4 notitle,\
       fdir+"/experimental/singles1.dat" using 1:2 with point style 2 notitle,\
       fdir+"/experimental/singles1.dat" using 1:3 with point style 3 notitle,\
       fdir+"/experimental/singles1.dat" using 1:4 with point style 4 notitle

  # Broken, inject 2
  set xformat ""
  set yformat ""
  set y2format auto horizontal
  set origin 2*(plot_w+h_pad),plot_h+v_pad
  plot fdir+"/theory/singles2.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/singles2.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/theory/singles2.dat" using 1:4 with lines style 3 notitle,\
       fdir+"/theory/singles2.dat" using 1:5 with lines style 4 notitle,\
       fdir+"/experimental/singles2.dat" using 1:2 with point style 2 notitle,\
       fdir+"/experimental/singles2.dat" using 1:3 with point style 3 notitle,\
       fdir+"/experimental/singles2.dat" using 1:4 with point style 4 notitle
     
  # Key
  line from 0,2*plot_h+v_pad+line_dy to\
            line_w,2*plot_h+v_pad+line_dy with style 1
  line from line_dx,2*plot_h+v_pad+line_dy to\
            line_dx+line_w,2*plot_h+v_pad+line_dy with style 2
  line from 2*line_dx,2*plot_h+v_pad+line_dy to\
            2*line_dx+line_w,2*plot_h+v_pad+line_dy with style 3
  line from 3*line_dx,2*plot_h+v_pad+line_dy to\
            3*line_dx+line_w,2*plot_h+v_pad+line_dy with style 4
  text "scale" at key_dx,2*plot_h+v_pad+key_dy
  text "\(S_{0}\)" at line_dx+key_dx,2*plot_h+v_pad+key_dy
  text "\(S_{1}\)" at 2*line_dx+key_dx,2*plot_h+v_pad+key_dy
  text "\(S_{2}\)" at 3*line_dx+key_dx,2*plot_h+v_pad+key_dy
  
  # ENVIRONMENT
  # Broken, inject 0
  set xformat auto horizontal
  set yformat auto horizontal
  set y2format ""
  set origin 0,0
  plot fdir+"/theory/singles0.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\ 
       fdir+"/theory/singles0.dat" using 1:6 with lines style 5 notitle,\
       fdir+"/theory/singles0.dat" using 1:7 with lines style 6 notitle,\
       fdir+"/theory/singles0.dat" using 1:8 with lines style 7 notitle,\
       fdir+"/experimental/singles0.dat" using 1:5 with point style 2 notitle,\
       fdir+"/experimental/singles0.dat" using 1:6 with point style 3 notitle,\
       fdir+"/experimental/singles0.dat" using 1:7 with point style 4 notitle

  # Broken, inject 1
  set xformat auto horizontal
  set yformat ""
  set y2format ""
  set origin plot_w+h_pad,0
  plot fdir+"/theory/singles1.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/singles1.dat" using 1:6 with lines style 5 notitle,\
       fdir+"/theory/singles1.dat" using 1:7 with lines style 6 notitle,\
       fdir+"/theory/singles1.dat" using 1:8 with lines style 7 notitle,\
       fdir+"/experimental/singles1.dat" using 1:5 with point style 2 notitle,\
       fdir+"/experimental/singles1.dat" using 1:6 with point style 3 notitle,\
       fdir+"/experimental/singles1.dat" using 1:7 with point style 4 notitle

  # Broken, inject 2
  set xformat auto horizontal
  set yformat ""
  set y2format auto horizontal
  set origin 2*(plot_w+h_pad),0
  plot fdir+"/theory/singles2.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/singles2.dat" using 1:6 with lines style 5 notitle,\
       fdir+"/theory/singles2.dat" using 1:7 with lines style 6 notitle,\
       fdir+"/theory/singles2.dat" using 1:8 with lines style 7 notitle,\
       fdir+"/experimental/singles2.dat" using 1:5 with point style 2 notitle,\
       fdir+"/experimental/singles2.dat" using 1:6 with point style 3 notitle,\
       fdir+"/experimental/singles2.dat" using 1:7 with point style 4 notitle

  unset logscale

  # Key
  line from 0,plot_h+line_dy to\
            line_w,plot_h+line_dy with style 1
  line from line_dx,plot_h+line_dy to\
            line_dx+line_w,plot_h+line_dy with style 5
  line from 2*line_dx,plot_h+line_dy to\
            2*line_dx+line_w,plot_h+line_dy with style 6
  line from 3*line_dx,plot_h+line_dy to\
            3*line_dx+line_w,plot_h+line_dy with style 7
  text "scale" at key_dx,plot_h+key_dy
  text "\(E_{0}\)" at line_dx+key_dx,plot_h+key_dy
  text "\(E_{1}\)" at 2*line_dx+key_dx,plot_h+key_dy
  text "\(E_{2}\)" at 3*line_dx+key_dx,plot_h+key_dy

  # Axis labels
  text "Occupation Probability" at -2*h_pad,sub_h+v_gap+sub_h/2 rotate 90\
   halign centre
  text "Occupation Probability" at -2*h_pad,sub_h/2 rotate 90\
   halign centre
  text "Scale" at fig_w+2*h_pad,sub_h+v_gap+sub_h/2 rotate 90\
   halign centre
  text "Scale" at fig_w+2*h_pad,sub_h/2 rotate 90\
   halign centre
  text "time, \(t\)" at fig_w/2,-v_pad halign centre
  text "time, \(t\)" at fig_w/2,sub_h+v_gap-v_pad halign centre
  
  # Subfigure labels
  text "(a)" at -2.5*h_pad,2*sub_h+v_gap+0.5*v_pad
  text "(b)" at -2.5*h_pad,sub_h+0.5*v_pad

  set display
  refresh
unset multiplot

###-------------------------------------PAIRS--------------------------------###

set output "threesite_pairs.pdf"
set multiplot
  set nodisplay

### SYMMETRIC
  fdir="../pt/data/threesite/symmetric"
  set xrange [0:5.135]
  set xtics out 5
  set mxtics out 1
  set yrange [0:0.6]
  set ytics out 0.6
  set mytics out 0.2
  set y2range [0:4]
  set y2tics out 4
  set my2tics out 1
  
  # SYSTEM
  # Symmetric, inject 0,1
  set xformat ""
  set yformat auto horizontal
  set y2format ""
  set origin 0,sub_h+v_gap+plot_h+v_pad
  plot fdir+"/theory/pairs01.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\ 
       fdir+"/theory/pairs01.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/theory/pairs01.dat" using 1:4 with lines style 3 notitle,\
       fdir+"/theory/pairs01.dat" using 1:8 with lines style 4 notitle,\
       fdir+"/experimental/pairs01.dat" using 1:2 with point style 2 notitle,\
       fdir+"/experimental/pairs01.dat" using 1:3 with point style 3 notitle,\
       fdir+"/experimental/pairs01.dat" using 1:7 with point style 4 notitle

  # Symmetric, inject 0,2
  set xformat ""
  set yformat ""
  set y2format ""
  set origin plot_w+h_pad,sub_h+v_gap+plot_h+v_pad
  plot fdir+"/theory/pairs02.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/pairs02.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/theory/pairs02.dat" using 1:4 with lines style 3 notitle,\
       fdir+"/theory/pairs02.dat" using 1:8 with lines style 4 notitle,\
       fdir+"/experimental/pairs02.dat" using 1:2 with point style 2 notitle,\
       fdir+"/experimental/pairs02.dat" using 1:3 with point style 3 notitle,\
       fdir+"/experimental/pairs02.dat" using 1:7 with point style 4 notitle

  # Symmetric, inject 1,2
  set xformat ""
  set yformat ""
  set y2format auto horizontal
  set origin 2*(plot_w+h_pad),sub_h+v_gap+plot_h+v_pad
  plot fdir+"/theory/pairs12.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/pairs12.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/theory/pairs12.dat" using 1:4 with lines style 3 notitle,\
       fdir+"/theory/pairs12.dat" using 1:8 with lines style 4 notitle,\
       fdir+"/experimental/pairs12.dat" using 1:2 with point style 2 notitle,\
       fdir+"/experimental/pairs12.dat" using 1:3 with point style 3 notitle,\
       fdir+"/experimental/pairs12.dat" using 1:7 with point style 4 notitle

  # Key
  line from 0,sub_h+v_gap+2*plot_h+v_pad+line_dy to\
            line_w,sub_h+v_gap+2*plot_h+v_pad+line_dy with style 1
  line from line_dx,sub_h+v_gap+2*plot_h+v_pad+line_dy to\
            line_dx+line_w,sub_h+v_gap+2*plot_h+v_pad+line_dy with style 2
  line from 2*line_dx,sub_h+v_gap+2*plot_h+v_pad+line_dy to\
            2*line_dx+line_w,sub_h+v_gap+2*plot_h+v_pad+line_dy with style 3
  line from 3*line_dx,sub_h+v_gap+2*plot_h+v_pad+line_dy to\
            3*line_dx+line_w,sub_h+v_gap+2*plot_h+v_pad+line_dy with style 4
  text "scale" at key_dx,sub_h+v_gap+2*plot_h+v_pad+key_dy
  text "\(S_{0}S_{1}\)" at line_dx+key_dx,sub_h+v_gap+2*plot_h+v_pad+key_dy
  text "\(S_{0}S_{2}\)" at 2*line_dx+key_dx,sub_h+v_gap+2*plot_h+v_pad+key_dy
  text "\(S_{1}S_{2}\)" at 3*line_dx+key_dx,sub_h+v_gap+2*plot_h+v_pad+key_dy
  
  # ENVIRONMENT
  # Symmetric, inject 0,1
  set xformat auto horizontal
  set yformat auto horizontal
  set y2format ""
  set origin 0,sub_h+v_gap+0
  plot fdir+"/theory/pairs01.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\ 
       fdir+"/theory/pairs01.dat" using 1:5 with lines style 5 notitle,\
       fdir+"/theory/pairs01.dat" using 1:6 with lines style 6 notitle,\
       fdir+"/theory/pairs01.dat" using 1:7 with lines style 7 notitle,\
       fdir+"/experimental/pairs01.dat" using 1:4 with point style 2 notitle,\
       fdir+"/experimental/pairs01.dat" using 1:5 with point style 3 notitle,\
       fdir+"/experimental/pairs01.dat" using 1:6 with point style 4 notitle

  # Symmetric, inject 0,2
  set xformat auto horizontal
  set yformat ""
  set y2format ""
  set origin plot_w+h_pad,sub_h+v_gap+0
  plot fdir+"/theory/pairs02.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/pairs02.dat" using 1:5 with lines style 5 notitle,\
       fdir+"/theory/pairs02.dat" using 1:6 with lines style 6 notitle,\
       fdir+"/theory/pairs02.dat" using 1:7 with lines style 7 notitle,\
       fdir+"/experimental/pairs02.dat" using 1:4 with point style 2 notitle,\
       fdir+"/experimental/pairs02.dat" using 1:5 with point style 3 notitle,\
       fdir+"/experimental/pairs02.dat" using 1:6 with point style 4 notitle

  # Symmetric, inject 1,2
  set xformat auto horizontal
  set yformat ""
  set y2format auto horizontal
  set origin 2*(plot_w+h_pad),sub_h+v_gap+0
  plot fdir+"/theory/pairs12.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/pairs12.dat" using 1:5 with lines style 5 notitle,\
       fdir+"/theory/pairs12.dat" using 1:6 with lines style 6 notitle,\
       fdir+"/theory/pairs12.dat" using 1:7 with lines style 7 notitle,\
       fdir+"/experimental/pairs12.dat" using 1:4 with point style 2 notitle,\
       fdir+"/experimental/pairs12.dat" using 1:5 with point style 3 notitle,\
       fdir+"/experimental/pairs12.dat" using 1:6 with point style 4 notitle
 
  # Key
  line from 0,sub_h+v_gap+plot_h+line_dy to\
            line_w,sub_h+v_gap+plot_h+line_dy with style 1
  line from line_dx,sub_h+v_gap+plot_h+line_dy to\
            line_dx+line_w,sub_h+v_gap+plot_h+line_dy with style 5
  line from 2*line_dx,sub_h+v_gap+plot_h+line_dy to\
            2*line_dx+line_w,sub_h+v_gap+plot_h+line_dy with style 6
  line from 3*line_dx,sub_h+v_gap+plot_h+line_dy to\
            3*line_dx+line_w,sub_h+v_gap+plot_h+line_dy with style 7
  text "scale" at key_dx,sub_h+v_gap+plot_h+key_dy
  text "\(S_{0}E_{0}\)" at line_dx+key_dx,sub_h+v_gap+plot_h+key_dy
  text "\(S_{0}E_{1}\)" at 2*line_dx+key_dx,sub_h+v_gap+plot_h+key_dy
  text "\(S_{0}E_{2}\)" at 3*line_dx+key_dx,sub_h+v_gap+plot_h+key_dy

### BROKEN
  fdir="../pt/data/threesite/broken"
  set xrange [0:6]
  set xtics out 6
  set mxtics out 1
  set yrange [0:0.6]
  set ytics out 0.6
  set mytics out 0.2
  set logscale y2
  set y2range [1:200]
  set y2tics out 100
  set my2tics out 10
  
  # SYSTEM
  # Broken, inject 0,1
  set xformat ""
  set yformat auto horizontal
  set y2format ""
  set origin 0,plot_h+v_pad
  plot fdir+"/theory/pairs01.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\ 
       fdir+"/theory/pairs01.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/theory/pairs01.dat" using 1:4 with lines style 3 notitle,\
       fdir+"/theory/pairs01.dat" using 1:8 with lines style 4 notitle,\
       fdir+"/experimental/pairs01.dat" using 1:2 with point style 2 notitle,\
       fdir+"/experimental/pairs01.dat" using 1:3 with point style 3 notitle,\
       fdir+"/experimental/pairs01.dat" using 1:7 with point style 4 notitle

  # Broken, inject 0,2
  set xformat ""
  set yformat ""
  set y2format ""
  set origin plot_w+h_pad,plot_h+v_pad
  plot fdir+"/theory/pairs02.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/pairs02.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/theory/pairs02.dat" using 1:4 with lines style 3 notitle,\
       fdir+"/theory/pairs02.dat" using 1:8 with lines style 4 notitle,\
       fdir+"/experimental/pairs02.dat" using 1:2 with point style 2 notitle,\
       fdir+"/experimental/pairs02.dat" using 1:3 with point style 3 notitle,\
       fdir+"/experimental/pairs02.dat" using 1:7 with point style 4 notitle

  # Broken, inject 1,2
  set xformat ""
  set yformat ""
  set y2format auto horizontal
  set origin 2*(plot_w+h_pad),plot_h+v_pad
  plot fdir+"/theory/pairs12.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/pairs12.dat" using 1:3 with lines style 2 notitle,\
       fdir+"/theory/pairs12.dat" using 1:4 with lines style 3 notitle,\
       fdir+"/theory/pairs12.dat" using 1:8 with lines style 4 notitle,\
       fdir+"/experimental/pairs12.dat" using 1:2 with point style 2 notitle,\
       fdir+"/experimental/pairs12.dat" using 1:3 with point style 3 notitle,\
       fdir+"/experimental/pairs12.dat" using 1:7 with point style 4 notitle
     
  # Key
  line from 0,2*plot_h+v_pad+line_dy to\
            line_w,2*plot_h+v_pad+line_dy with style 1
  line from line_dx,2*plot_h+v_pad+line_dy to\
            line_dx+line_w,2*plot_h+v_pad+line_dy with style 2
  line from 2*line_dx,2*plot_h+v_pad+line_dy to\
            2*line_dx+line_w,2*plot_h+v_pad+line_dy with style 3
  line from 3*line_dx,2*plot_h+v_pad+line_dy to\
            3*line_dx+line_w,2*plot_h+v_pad+line_dy with style 4
  text "scale" at key_dx,2*plot_h+v_pad+key_dy
  text "\(S_{0}S_{1}\)" at line_dx+key_dx,2*plot_h+v_pad+key_dy
  text "\(S_{0}S_{2}\)" at 2*line_dx+key_dx,2*plot_h+v_pad+key_dy
  text "\(S_{1}S_{2}\)" at 3*line_dx+key_dx,2*plot_h+v_pad+key_dy
  
  # ENVIRONMENT
  # Broken, inject 0,1
  set xformat auto horizontal
  set yformat auto horizontal
  set y2format ""
  set origin 0,0
  plot fdir+"/theory/pairs01.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\ 
       fdir+"/theory/pairs01.dat" using 1:5 with lines style 5 notitle,\
       fdir+"/theory/pairs01.dat" using 1:6 with lines style 6 notitle,\
       fdir+"/theory/pairs01.dat" using 1:7 with lines style 7 notitle,\
       fdir+"/experimental/pairs01.dat" using 1:4 with point style 2 notitle,\
       fdir+"/experimental/pairs01.dat" using 1:5 with point style 3 notitle,\
       fdir+"/experimental/pairs01.dat" using 1:6 with point style 4 notitle

  # Broken, inject 0,2
  set xformat auto horizontal
  set yformat ""
  set y2format ""
  set origin plot_w+h_pad,0
  plot fdir+"/theory/pairs02.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/pairs02.dat" using 1:5 with lines style 5 notitle,\
       fdir+"/theory/pairs02.dat" using 1:6 with lines style 6 notitle,\
       fdir+"/theory/pairs02.dat" using 1:7 with lines style 7 notitle,\
       fdir+"/experimental/pairs02.dat" using 1:4 with point style 2 notitle,\
       fdir+"/experimental/pairs02.dat" using 1:5 with point style 3 notitle,\
       fdir+"/experimental/pairs02.dat" using 1:6 with point style 4 notitle

  # Broken, inject 1,2
  set xformat auto horizontal
  set yformat ""
  set y2format auto horizontal
  set origin 2*(plot_w+h_pad),0
  plot fdir+"/theory/pairs12.dat" using 1:2 with lines style 1 notitle\
       axes x1y2,\
       fdir+"/theory/pairs12.dat" using 1:5 with lines style 5 notitle,\
       fdir+"/theory/pairs12.dat" using 1:6 with lines style 6 notitle,\
       fdir+"/theory/pairs12.dat" using 1:7 with lines style 7 notitle,\
       fdir+"/experimental/pairs12.dat" using 1:4 with point style 2 notitle,\
       fdir+"/experimental/pairs12.dat" using 1:5 with point style 3 notitle,\
       fdir+"/experimental/pairs12.dat" using 1:6 with point style 4 notitle

  # Key
  line from 0,plot_h+line_dy to\
            line_w,plot_h+line_dy with style 1
  line from line_dx,plot_h+line_dy to\
            line_dx+line_w,plot_h+line_dy with style 5
  line from 2*line_dx,plot_h+line_dy to\
            2*line_dx+line_w,plot_h+line_dy with style 6
  line from 3*line_dx,plot_h+line_dy to\
            3*line_dx+line_w,plot_h+line_dy with style 7
  text "scale" at key_dx,plot_h+key_dy
  text "\(S_{0}E_{0}\)" at line_dx+key_dx,plot_h+key_dy
  text "\(S_{0}E_{1}\)" at 2*line_dx+key_dx,plot_h+key_dy
  text "\(S_{0}E_{2}\)" at 3*line_dx+key_dx,plot_h+key_dy

  # Axis labels
  text "Occupation Probability" at -2*h_pad,sub_h+v_gap+sub_h/2 rotate 90\
   halign centre
  text "Occupation Probability" at -2*h_pad,sub_h/2 rotate 90\
   halign centre
  text "Scale" at fig_w+2*h_pad,sub_h+v_gap+sub_h/2 rotate 90\
   halign centre
  text "Scale" at fig_w+2*h_pad,sub_h/2 rotate 90\
   halign centre
  text "time, \(t\)" at fig_w/2,-v_pad halign centre
  text "time, \(t\)" at fig_w/2,sub_h+v_gap-v_pad halign centre
  
  # Subfigure labels
  text "(a)" at -2.5*h_pad,2*sub_h+v_gap+0.5*v_pad
  text "(b)" at -2.5*h_pad,sub_h+0.5*v_pad

  set display
  refresh
unset multiplot

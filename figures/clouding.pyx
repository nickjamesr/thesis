#!/usr/bin/pyxplot

set term pdf 
set output "clouding.pdf"
set fontsize 1.0

fig_w=12.0
fig_m=fig_w/100.

plot_w = 45*fig_m
plot_h = 25*fig_m

v_pad = 4*fig_m
h_pad = 8*fig_m

fig_h=2*plot_h+v_pad

text_dx=1*fig_m
text_dy=-3*fig_m

rgbquantum=rgb(0.0,0.0,1.0)
rgbclassical=rgb(1.0,0.0,0.0)
rgbmixed=rgb(0.0,1.0,0.0)

fdir="../verification/data/clouds"

set xtics outward -0.4,0.2
set ytics outward

set axis x nomirror
set axis y nomirror

set axis x2
set axis y2

set noytics
set nomytics

set nox2tics
set noy2tics

set width plot_w
set size ratio plot_h/plot_w

set xrange [-0.4:0.2+1e-5]
set xtics out 0.2
set mxtics out 0.1

set multiplot
  set nodisplay

### 3 photon BS
  set origin plot_w+h_pad,0
  set yrange [0:35]
  plot fdir+"/bs_ideal_3photons_histogram.dat" using 1:2\
    with lines color rgbquantum notitle,\
    fdir+"/bs_ideal_3photons_histogram.dat" using 3:4\
    with lines color rgbclassical notitle,\
    fdir+"/experimentalclouding.dat" every ::6::6 using 1:(0.95*21):2\
    with xerrorbars pointsize 0.4 colour rgbquantum notitle,\
    fdir+"/experimentalclouding.dat" every ::6::6 using 1:(0.95*21)\
    with pointtype 17 colour rgbquantum pointsize 0.5 notitle,\
    fdir+"/experimentalclouding.dat" every ::7::7 using 1:(21):2\
    with xerrorbars pointsize 0.4 colour rgbclassical notitle,\
    fdir+"/experimentalclouding.dat" every ::7::7 using 1:(21)\
    with pointtype 17 colour rgbclassical pointsize 0.5 notitle

### 5 photon QW
  set origin 0,0
  set yrange [0:25]
  unset xlabel
  plot fdir+"/qw_ideal_5in4_histogram.dat" using 1:2\
    with lines color rgbquantum notitle,\
    fdir+"/qw_ideal_5in4_histogram.dat" using 3:4\
    with lines color rgbclassical notitle,\
    fdir+"/qw_ideal_4+1in4_histogram.dat" using 1:2\
    with lines color rgbquantum linetype 2 notitle,\
    fdir+"/experimentalclouding.dat" every ::4::4 using 1:(0.95*15):2\
    with xerrorbars pointsize 0.4 colour rgbquantum notitle,\
    fdir+"/experimentalclouding.dat" every ::4::4 using 1:(0.95*15)\
    with pointtype 17 colour rgbquantum pointsize 0.5 notitle,\
    fdir+"/experimentalclouding.dat" every ::5::5 using 1:(15):2\
    with xerrorbars pointsize 0.4 colour rgbclassical notitle,\
    fdir+"/experimentalclouding.dat" every ::5::5 using 1:(15)\
    with pointtype 17 colour rgbclassical pointsize 0.5 notitle

### 4 photon QW
  set origin plot_w+h_pad,plot_h+v_pad
  set xformat ""
  set yrange [0:120]
  plot fdir+"/qw_ideal_4photons_histogram.dat" using 1:2\
    with lines color rgbquantum notitle,\
    fdir+"/qw_ideal_4photons_histogram.dat" using 3:4\
    with lines color rgbclassical notitle,\
    fdir+"/experimentalclouding.dat" every ::2::2 using 1:(0.95*60):2\
    with xerrorbars pointsize 0.4 colour rgbquantum notitle,\
    fdir+"/experimentalclouding.dat" every ::2::2 using 1:(0.95*60)\
    with pointtype 17 colour rgbquantum pointsize 0.5 notitle,\
    fdir+"/experimentalclouding.dat" every ::3::3 using 1:(60):2\
    with xerrorbars pointsize 0.4 colour rgbclassical notitle,\
    fdir+"/experimentalclouding.dat" every ::3::3 using 1:(60)\
    with pointtype 17 colour rgbclassical pointsize 0.5 notitle

### 3 photon QW
  set origin 0,plot_h+v_pad
  set xformat ""
  set yrange [0:70]
  plot fdir+"/qw_ideal_3photons_histogram.dat" using 1:2\
    with lines color rgbquantum notitle,\
    fdir+"/qw_ideal_3photons_histogram.dat" using 3:4\
    with lines color rgbclassical notitle,\
    fdir+"/experimentalclouding.dat" every ::0::0 using 1:(0.95*36):2\
    with xerrorbars pointsize 0.4 colour rgbquantum notitle,\
    fdir+"/experimentalclouding.dat" every ::0::0 using 1:(0.95*36)\
    with pointtype 17 colour rgbquantum pointsize 0.5 notitle,\
    fdir+"/experimentalclouding.dat" every ::1::1 using 1:(36):2\
    with xerrorbars pointsize 0.4 colour rgbclassical notitle,\
    fdir+"/experimentalclouding.dat" every ::1::1 using 1:(36)\
    with pointtype 17 colour rgbclassical pointsize 0.5 notitle

### Text labels
  text "(a) 3-photon quantum walk" at text_dx,fig_h+text_dy
  text "(b) 4-photon quantum walk" at plot_w+h_pad+text_dx,fig_h+text_dy
  text "(c) 5-photon quantum walk" at text_dx,plot_h+text_dy
  text "(d) 3-photon random unitary" at plot_w+h_pad+text_dx,plot_h+text_dy
  text "Degree of clouding, \(\mathcal{C}\)" at fig_w/2,-2*v_pad halign centre
  text "Probability density" at -v_pad,fig_h/2 rotate 90 halign centre

  set display
  refresh
unset multiplot



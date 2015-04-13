set terminal pdf
set output "tevol.pdf"

fig_w=11.0
fig_m=fig_w/100.
left_w=52*fig_m
right_w=35*fig_m
h_pad=fig_w-left_w-right_w
plot_h=30*fig_m

text_dy=plot_h+4*fig_m

fdir="../hamiltomo/data/TOpt"

set style 1 colour blue pointtype 15
set style 2 colour green
set style 3 colour red
set style 4 colour rgb(0.7,0.7,1.0) linewidth 0.1 fillcolor rgb(0.7,0.7,1.0)
set style 5 colour black linetype 2


set axis x nomirror
set axis y nomirror
set xtics out 6.2,0.8
set mxtics out 0.1
set ytics out 0.2,0.05
set mytics out 0.01
set axis x2 visible
set nox2tics
set axis y2 visible
set noy2tics

set key top left 20*fig_m,0

set multiplot
  set nodisplay

  set width left_w
  set size ratio plot_h/left_w
  set xlabel "Evolution time, \(t\)"
  set ylabel "Error"
  set origin 0,0
  plot fdir+"/tevol_774.dat" using 1:3 with lines style 1 title "774nm",\
       fdir+"/tevol_776.dat" using 1:3 with lines style 2 title "776nm",\
       fdir+"/tevol_778.dat" using 1:3 with lines style 3 title "778nm"

  dt=log(0.06)/log(2)
  set arrow 1 from dt,-0.5 to dt,2.0 with style 5 nohead
  set xtics out -6,2
  set mxtics out 1
  set yrange [-0.5:2.0]
  set ytics out 0,1
  set mytics out 0,0.5
  set width right_w
  set size ratio plot_h/right_w
  set xlabel "\(\log_{2} \left( \delta t \right)\)"
  set ylabel "log(Error)"
  set origin left_w+h_pad,0
  plot fdir+"/ErrorVsTime.dat" using (log($1)/log(2)):(log($3)):(log($4))\
       with yerrorshaded style 4 notitle,\
       fdir+"/ErrorVsTime.dat" using (log($1)/log(2)):(log($2))\
       with lines style 1 notitle

  # Subplot labels
  text "(a)" at 0.5*left_w,text_dy halign centre
  text "(b)" at left_w+h_pad+0.5*right_w,text_dy halign centre
  
  set display
  refresh
unset multiplot

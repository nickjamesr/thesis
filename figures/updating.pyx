set terminal pdf
set output "updating.pdf"

quant_col=rgb(0.0,0.0,1.0)
class_col=rgb(1.0,0.0,0.0)

set style 1 colour quant_col
set style 2 colour class_col
set style 3 linetype 2 colour black

fig_w=8
fig_m=fig_w/100.

set width fig_w
set key top left

set axis x nomirror
set axis y nomirror

set axis x2 visible
set axis y2 visible

set nox2tics
set noy2tics

set xlabel "Detection events"
set ylabel "Confidence"

set xrange [0:25]
set yrange [0:1.05]

fin="../verification/data/updating.dat"

plot 1 with lines style 3 notitle,\
     fin using 4:2 with lines style 1 \
     title "\(\mathcal{P}\left(\mathrm{Quantum}\right)\)",\
     fin using 4:3 with lines style 2\
     title "\(\mathcal{P}\left(\mathrm{Classical}\right)\)"


fdir="../background"

set terminal pngcairo size 9cm,7cm fontscale 0.8
set output "QuantumWalk.png"
set xrange [-0.5:15.5]
set xtics out nomirror 3
set yrange [0:0.15]
set ytics out 0.05
set style fill solid 0.5
set xlabel "Output mode, i"
plot fdir."/singles.dat" with boxes ls 3 notitle


set size ratio -1
set xrange [-0.5:15.5]
set x2range [-0.5:15.5]
set yrange [15.5:-0.5]
set cbrange [0:0.05]
set cbtics 0.05
set mcbtics 5
set noxtics
set x2tics out nomirror 15
set mx2tics 15
set ytics out nomirror 15
set mytics 15
set palette defined (0 "white", 1 "blue")
set noxlabel

set terminal pngcairo size 10cm,8cm fontscale 0.8
set output "BosonWalk.png"
plot fdir."/bosons.dat" matrix w image notitle,\
     x with lines linestyle -1 notitle

set output "FermionWalk.png"
plot fdir."/fermions.dat" matrix w image notitle,\
     x with lines linestyle -1 notitle

set output "ClassicalWalk.png"
plot fdir."/classical.dat" matrix w image notitle,\
     x with lines linestyle -1 notitle

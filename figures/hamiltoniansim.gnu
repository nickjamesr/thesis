set terminal pngcairo size 10cm,8cm fontscale 0.8

fdir="../hamiltomo/data/TOpt"

set size ratio -1
set xrange [-0.5:20.5]
set x2range [-0.5:20.5]
set yrange [20.5:-0.5]
set cbrange [0:1.0]
set noxtics
set x2tics out nomirror 20
set mx2tics 20
set ytics out nomirror 20
set mytics 20
unset colorbox
set palette defined (0 "white", 1 "blue")

set arrow 1 from 7.5,7.5 to 7.5,11.5 nohead linewidth 2 front
set arrow 2 from 7.5,11.5 to 11.5,11.5 nohead linewidth 2 front
set arrow 3 from 11.5,7.5 to 11.5,11.5 nohead linewidth 2 front
set arrow 4 from 7.5,7.5 to 11.5,7.5 nohead linewidth 2 front

set output "idealhamiltonian.png"
plot fdir."/ideal.dat" matrix w image notitle

set colorbox
set terminal pngcairo size 12cm,8cm fontscale 0.8
set output "experimentalhamiltonian.png"
plot fdir."/experimental.dat" matrix w image notitle

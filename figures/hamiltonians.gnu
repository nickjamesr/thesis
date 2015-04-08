set terminal pngcairo size 18cm,12cm fontscale 0.8
set output "hamiltonians.png"

fdir="../hamiltomo/data/Hamiltonians"

set size ratio -1
set xrange [-0.5:3.5]
set x2range [-0.5:3.5]
set yrange [3.5:-0.5]
set cbrange [0:0.4]
set noxtics
set x2tics out nomirror 1
set ytics out nomirror 1
unset colorbox
set palette defined (0 "white", 1 "blue")

set multiplot layout 2,3
  set x2label "(8,3)"
  plot fdir."/refs0803.dat" matrix w image notitle
  set x2label "(8,4)"
  plot fdir."/refs0804.dat" matrix w image notitle
  set x2label "(8,6)"
  plot fdir."/refs0806.dat" matrix w image notitle
  set x2label "(9,3)"
  plot fdir."/refs0903.dat" matrix w image notitle
  set x2label "(9,4)"
  plot fdir."/refs0904.dat" matrix w image notitle
  set x2label "(9,6)"
  plot fdir."/refs0906.dat" matrix w image notitle
unset multiplot

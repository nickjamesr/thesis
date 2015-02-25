set terminal pdf
set output "circuit.pdf"

set multiplot
  image "circuit.png" at 0,0
unset multiplot

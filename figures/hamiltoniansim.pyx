set terminal pdf
set output "hamiltoniansim.pdf"

fig_w=14.
fig_m=fig_w/100.

set multiplot
  set nodisplay
  image "idealhamiltonian.png" at 0,0 width fig_w*10/22.
  image "experimentalhamiltonian.png" at fig_w*10/22.,0 width fig_w*12/22.
  set display
  refresh
unset multiplot

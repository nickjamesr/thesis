set terminal pdf
set output "hamiltoniansim.pdf"

fig_w=14.
fig_m=fig_w/100.
left_w=fig_w*10/22.
right_w=fig_w*12/22.
text_dy=-3*fig_m

set multiplot
  set nodisplay
  image "idealhamiltonian.png" at 0,0 width left_w
  image "experimentalhamiltonian.png" at fig_w*10/22.,0 width right_w

  # subfigure labels
  text "(a)" at 0.5*left_w,text_dy halign centre
  text "(b)" at left_w+0.5*right_w,text_dy halign centre
  
  set display
  refresh
unset multiplot

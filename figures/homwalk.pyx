set terminal pdf
set output "homwalk.pdf"

fig_w=13.
fig_m=fig_w/100.
image_w=50*fig_m
image_h=45*fig_m
text_dx=25*fig_m
text_dy=-5*fig_m

set multiplot
  set nodisplay
  image "BosonWalk.png" at image_w,image_h width image_w
  image "QuantumWalk.png" at 0,image_h width 0.9*image_w
  image "FermionWalk.png" at image_w,0 width image_w
  image "ClassicalWalk.png" at 0,0 width image_w

  # subfigure labels
  text "(a) Single particle" at text_dx,2*image_h+text_dy\
    halign centre
  text "(b) Bosonic interference" at image_w+text_dx,2*image_h+text_dy\
    halign centre
  text "(c) No interference" at text_dx,image_h+text_dy\
    halign centre
  text "(d) Fermionic interference" at image_w+text_dx,image_h+text_dy\
    halign centre
  
  set display
  refresh
unset multiplot

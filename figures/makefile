ifeq (Darwin, $(shell uname -s))
inkscape=/Applications/Inkscape.app/Contents/Resources/bin/inkscape
else
inkscape=inkscape
endif

all = benchmarking.pdf\
 bosonsampling.pdf\
 cascade.pdf\
 circuit.pdf\
 clouds.pdf\
 crapusoid.pdf\
 crosstalk.pdf\
 example.pdf\
 interferometerAB.pdf\
 interferometerCD.pdf\
 logvsderivative.pdf\
 manifolds.png\
 opensystem.pdf\
 qubits.pdf\
 reck_original.pdf\
 reck_general.pdf\
 recursive.pdf\
 rstar.pdf\
 schematic.pdf\
 sixphoton.pdf\
 twosite.pdf

default : $(all)

# Generate data if required
../pt/% :
	cd ../pt && $(MAKE) $*

../scatterbox/random/%:
	cd ../scatterbox/random && $(MAKE) $*

../hamiltomo/%:
	cd ../hamiltomo && $(MAKE) $*

# Rule to generate eps from svg
%.eps : %.svg
	$(inkscape) -E $*.eps $<

# png files may have different resolution
circuit.png : circuit.svg
	$(inkscape) -d 360 -e circuit.png circuit.svg

# Manifold eps
manifold_data=$(addprefix ../pt/data/,manifold/manifold_A.dat\
 manifold/rawmanifold_A.dat\
 broken/quantum.dat\
 critical/quantum.dat\
 symmetric/quantum.dat)
manifold_bare_A.eps manifold_data_A.eps : manifolds.gnu $(manifold_data)
	gnuplot manifolds.gnu

# Manifold png (raster to save on size)
manifolds.png : manifold_bare_A.eps manifold_data_A.eps manifolds.pyx
	pyxplot manifolds.pyx

# Clouding
%.png : %.pov
	povray +A $*.pov

# pdf files may have different/multiple dependencies
benchmarking_data=$(addprefix ../scatterbox/random/data/,\
 example_quart.dat\
 example_trit.dat\
 example_quantum.dat\
 example_classical.dat)
benchmarking.pdf : $(benchmarking_data) benchmarking.pyx
	pyxplot benchmarking.pyx

bosonsampling.pdf : BSunitary.eps bosonsampling.pyx
	pyxplot bosonsampling.pyx

cascade.pdf : cascade.eps cascade.pyx
	pyxplot cascade.pyx

circuit.pdf : circuit.png circuit.pyx
	pyxplot circuit.pyx

clouds.pdf : walk_ex_c.png walk_ex_q.png walk_th_c.png walk_th_q.png clouds.pyx
	pyxplot clouds.pyx

crapusoid.pdf : crapusoid.pyx
	pyxplot crapusoid.pyx

crosstalk.pdf : crosstalk.eps crosstalk.pyx
	pyxplot crosstalk.pyx

example.pdf : example.eps beamsplitter.eps bsmzi.eps dcmzi.eps example.pyx
	pyxplot example.pyx

interferometerAB.pdf : interferometerAB.eps interferometerAB.pyx
	pyxplot interferometerAB.pyx

interferometerCD.pdf : interferometerCD.eps interferometerCD.pyx
	pyxplot interferometerCD.pyx

logvsderivative_data=$(addprefix ../hamiltomo/data/,\
 comparison00.dat\
 comparison01.dat\
 comparison02.dat\
 comparison03.dat\
 comparison04.dat\
 comparison05.dat\
 comparison06.dat)
logvsderivative.pdf : $(logvsderivative_data) logvsderivative.pyx
	pyxplot logvsderivative.pyx

opensystem.pdf : opensystem.eps opensystem.pyx
	pyxplot opensystem.pyx

qubits.pdf : twoqubit.eps threequbit.eps qubits.pyx
	pyxplot qubits.pyx

reck_general.pdf : reck_general.eps reck_general.pyx
	pyxplot reck_general.pyx

reck_original.pdf : reck_original.eps reck_original.pyx
	pyxplot reck_original.pyx

recursive.pdf : recursive.eps recursive.pyx
	pyxplot recursive.pyx

rstar.pdf : rstar.pyx ../verification/data/updating.dat\
 ../verification/data/RStarData.dat\
 ../verification/data/histogram.dat
	pyxplot rstar.pyx

schematic.pdf : schematic.eps schematic.pyx
	pyxplot schematic.pyx

sixphoton.pdf : sixphoton.pyx ../reck/data/classical_events.dat\
 ../reck/data/quantum_events.dat
	pyxplot sixphoton.pyx

twosite_data=$(addprefix ../pt/data/,broken/quantum.dat\
 broken/quart.dat\
 broken/theory.dat\
 critical/quantum.dat\
 critical/quart.dat\
 critical/theory.dat\
 symmetric/quantum.dat\
 symmetric/quart.dat\
 symmetric/theory.dat)
twosite.pdf : twosite.pyx $(twosite_data)
	pyxplot twosite.pyx

clean : 
	for f in *.pdf; do if [ -e $$f ]; then rm $$f; fi; done
	for f in *.eps; do if [ -e $$f ]; then rm $$f; fi; done
	for f in *.png; do if [ -e $$f ]; then rm $$f; fi; done


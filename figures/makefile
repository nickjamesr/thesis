ifeq (Darwin, $(shell uname -s))
inkscape=/Applications/Inkscape.app/Contents/Resources/bin/inkscape
else
inkscape=inkscape
endif

all = cascade.pdf\
 example.pdf\
 circuit.pdf\
 interferometerAB.pdf\
 interferometerCD.pdf\
 opensystem.pdf\
 qubits.pdf\
 reck_original.pdf\
 reck_general.pdf\
 recursive.pdf\
 rstar.pdf\
 schematic.pdf\
 sixphoton.pdf

default : $(all)

# All eps files have the same rule
%.eps : %.svg
	$(inkscape) -E $*.eps $<

# png files may have different resolution
circuit.png : circuit.svg
	$(inkscape) -d 360 -e circuit.png circuit.svg

# pdf files may have different/multiple dependencies

cascade.pdf : cascade.eps cascade.pyx
	pyxplot cascade.pyx

circuit.pdf : circuit.png circuit.pyx
	pyxplot circuit.pyx

example.pdf : example.eps beamsplitter.eps bsmzi.eps dcmzi.eps example.pyx
	pyxplot example.pyx

interferometerAB.pdf : interferometerAB.eps interferometerAB.pyx
	pyxplot interferometerAB.pyx

interferometerCD.pdf : interferometerCD.eps interferometerCD.pyx
	pyxplot interferometerCD.pyx

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

schematic.pdf : schematic.eps schematic.pyx
	pyxplot schematic.pyx

sixphoton.pdf : sixphoton.pyx ../reck/data/classical_events.dat\
 ../reck/data/quantum_events.dat
	pyxplot sixphoton.pyx

rstar.pdf : rstar.pyx ../verification/data/updating.dat\
 ../verification/data/RStarData.dat\
 ../verification/data/histogram.dat
	pyxplot rstar.pyx

clean : 
	for f in *.pdf; do if [ -e $$f ]; then rm $$f; fi; done
	for f in *.eps; do if [ -e $$f ]; then rm $$f; fi; done
	for f in *.png; do if [ -e $$f ]; then rm $$f; fi; done


circuit.pdf : circuit.png circuit.pyx
	pyxplot circuit.pyx

circuit.png : circuit.svg
	inkscape -d 360 -e circuit.png circuit.svg

clean : 
	@ if [ -e circuit.pdf ]; then rm circuit.pdf; fi
	@ if [ -e circuit.png ]; then rm circuit.png; fi

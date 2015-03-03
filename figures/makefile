ifeq (Darwin, $(shell uname -s))
inkscape=/Applications/Inkscape.app/Contents/Resources/bin/inkscape
else
inkscape=inkscape
endif

default : circuit.pdf interferometerAB.pdf interferometerCD.pdf schematic.pdf

circuit.pdf : circuit.png circuit.pyx
	pyxplot circuit.pyx

circuit.png : circuit.svg
	$(inkscape) -d 360 -e circuit.png circuit.svg

interferometerAB.png : interferometerAB.svg
	$(inkscape) -d 90 -e interferometerAB.png interferometerAB.svg

interferometerAB.pdf : interferometerAB.png
	pyxplot interferometerAB.pyx

interferometerCD.png : interferometerCD.svg
	$(inkscape) -d 90 -e interferometerCD.png interferometerCD.svg

interferometerCD.pdf : interferometerCD.png
	pyxplot interferometerCD.pyx

schematic.pdf : schematic.png schematic.pyx
	pyxplot schematic.pyx

schematic.png : schematic.svg
	$(inkscape) -d 180 -e schematic.png schematic.svg

clean : 
	@ if [ -e circuit.pdf ]; then rm circuit.pdf; fi
	@ if [ -e circuit.png ]; then rm circuit.png; fi
	@ if [ -e interferometerAB.pdf ]; then rm interferometerAB.pdf; fi
	@ if [ -e interferometerAB.png ]; then rm interferometerAB.png; fi
	@ if [ -e interferometerCD.pdf ]; then rm interferometerCD.pdf; fi
	@ if [ -e interferometerCD.png ]; then rm interferometerCD.png; fi
	@ if [ -e schematic.pdf ]; then rm schematic.pdf; fi
	@ if [ -e schematic.png ]; then rm schematic.png; fi

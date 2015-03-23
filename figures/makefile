ifeq (Darwin, $(shell uname -s))
inkscape=/Applications/Inkscape.app/Contents/Resources/bin/inkscape
else
inkscape=inkscape
endif

all = circuit.pdf interferometerAB.pdf interferometerCD.pdf schematic.pdf \
reck_original.pdf reck_general.pdf

default : $(all)

circuit.pdf : circuit.png circuit.pyx
	pyxplot circuit.pyx

circuit.png : circuit.svg
	$(inkscape) -d 360 -e circuit.png circuit.svg

interferometerAB.png : interferometerAB.svg
	$(inkscape) -d 90 -e interferometerAB.png interferometerAB.svg

interferometerAB.pdf : interferometerAB.png interferometerAB.pyx
	pyxplot interferometerAB.pyx

interferometerCD.png : interferometerCD.svg
	$(inkscape) -d 90 -e interferometerCD.png interferometerCD.svg

interferometerCD.pdf : interferometerCD.png interferometerCD.pyx
	pyxplot interferometerCD.pyx

reck_original.eps : reck_original.svg
	$(inkscape) -E reck_original.eps reck_original.svg

reck_original.pdf : reck_original.eps reck_original.pyx
	pyxplot reck_original.pyx

reck_general.eps : reck_general.svg
	$(inkscape) -E reck_general.eps reck_general.svg

reck_general.pdf : reck_general.eps reck_general.pyx
	pyxplot reck_general.pyx

schematic.png : schematic.svg
	$(inkscape) -d 180 -e schematic.png schematic.svg

schematic.pdf : schematic.png schematic.pyx
	pyxplot schematic.pyx

clean : 
	@ if [ -e circuit.pdf ]; then rm circuit.pdf; fi
	@ if [ -e circuit.png ]; then rm circuit.png; fi
	@ if [ -e interferometerAB.pdf ]; then rm interferometerAB.pdf; fi
	@ if [ -e interferometerAB.png ]; then rm interferometerAB.png; fi
	@ if [ -e interferometerCD.pdf ]; then rm interferometerCD.pdf; fi
	@ if [ -e interferometerCD.png ]; then rm interferometerCD.png; fi
	@ if [ -e schematic.pdf ]; then rm schematic.pdf; fi
	@ if [ -e schematic.png ]; then rm schematic.png; fi

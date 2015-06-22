ifeq (Darwin, $(shell uname -s))
inkscape=/Applications/Inkscape.app/Contents/Resources/bin/inkscape
else
inkscape=inkscape
endif

all = benchmarking.pdf\
 bigclouds.pdf\
 bosonsampling.pdf\
 cascade.pdf\
 circuit.pdf\
 clouding.pdf\
 clouds3d.pdf\
 crapusoid.pdf\
 crosstalk.pdf\
 example.pdf\
 hamiltonians.png\
 hamiltoniansim.pdf\
 homwalk.pdf\
 integratedreck.pdf\
 interferometerAB.pdf\
 interferometerCD.pdf\
 logvsderivative.pdf\
 manifolds.png\
 molecules.pdf\
 opensystem.pdf\
 qubits.pdf\
 reck_original.pdf\
 reck_general.pdf\
 recursive.pdf\
 rstar.pdf\
 schematic.pdf\
 simplehom.pdf\
 sixphoton.pdf\
 tevol.pdf\
 threesite_singles.pdf\
 threesite_pairs.pdf\
 timestep.pdf\
 twosite.pdf\
 vibrations.pdf

default : $(all)

# Generate data if required
../background/% :
	cd ../background $(MAKE) $*

../pt/% :
	cd ../pt && $(MAKE) $*

../scatterbox/random/%:
	cd ../scatterbox/random && $(MAKE) $*

../scatterbox/molecules/%:
	cd ../scatterbox/molecules && $(MAKE) $*

../hamiltomo/%:
	cd ../hamiltomo && $(MAKE) $*

../verification/data/bigclouds/% ../verification/data/clouds/%:
	cd ../verification/data &&\
 wget http://www.mostlydowntime.co.uk/physics/thesis/data/clouds.tar.gz &&\
 tar xvzf clouds.tar.gz &&\
 rm clouds.tar.gz

# Rule to generate eps from svg
%.eps : %.svg
	$(inkscape) -E $*.eps $<

# png files may have different resolution
circuit.png : circuit.svg
	$(inkscape) -d 360 -e circuit.png circuit.svg

hamiltonians_data=$(addprefix ../hamiltomo/data/Hamiltonians/,\
 refs0803.dat\
 refs0804.dat\
 refs0806.dat\
 refs0903.dat\
 refs0904.dat\
 refs0906.dat)
hamiltonians.png : $(hamiltonians_data) hamiltonians.gnu
	gnuplot hamiltonians.gnu

hamiltoniansim_data=$(addprefix ../hamiltomo/data/TOpt/,ideal.dat\
 experimental.dat\
 ErrorVsTime.dat)
idealhamiltonian.png experimentalhamiltonian.png : $(hamiltoniansim_data)\
 hamiltoniansim.gnu
	gnuplot hamiltoniansim.gnu

homwalk_data=$(addprefix ../background/,bosons.dat\
 fermions.dat\
 classical.dat)
BosonWalk.png FermionWalk.png ClassicalWalk.png QuantumWalk.png : hom.gnu
	gnuplot hom.gnu

vibrations.png : vibrations.svg
	$(inkscape) -d 120 -e vibrations.png vibrations.svg

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

bigclouds_data=$(addprefix ../verification/data/bigclouds/,\
 14x196classical.dat\
 14x196quantum.dat\
 10x100classical.dat\
 10x100quantum.dat\
 6x36classical.dat\
 6x36quantum.dat\
 6x36exactclassical.dat\
 6x36exactquantum.dat)
bigclouds.pdf : $(bigclouds_data) bigclouds.pyx
	pyxplot bigclouds.pyx

bosonsampling.pdf : BSunitary.eps bosonsampling.pyx
	pyxplot bosonsampling.pyx

cascade.pdf : cascade.eps cascade.pyx
	pyxplot cascade.pyx

circuit.pdf : circuit.png circuit.pyx
	pyxplot circuit.pyx

clouding_data=$(addprefix ../verification/data/clouds/,\
 bs_experimental_3photons_histogram.dat)
clouding.pdf : $(clouding_data) clouding.pyx
	pyxplot clouding.pyx

clouds3d.pdf : walk_ex_c.png walk_ex_q.png walk_th_c.png walk_th_q.png\
 clouds3d.pyx
	pyxplot clouds3d.pyx

crapusoid.pdf : crapusoid.pyx
	pyxplot crapusoid.pyx

crosstalk.pdf : crosstalk.eps crosstalk.pyx
	pyxplot crosstalk.pyx

example.pdf : example.eps beamsplitter.eps bsmzi.eps dcmzi.eps example.pyx
	pyxplot example.pyx

hamiltoniansim.pdf : idealhamiltonian.png experimentalhamiltonian.png\
 hamiltoniansim.pyx
	pyxplot hamiltoniansim.pyx

homwalk.pdf : BosonWalk.png FermionWalk.png ClassicalWalk.png QuantumWalk.png\
 homwalk.pyx
	pyxplot homwalk.pyx

integratedreck.pdf : integratedreck.eps integratedreck.pyx
	pyxplot integratedreck.pyx

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

molecules_data=$(addprefix ../scatterbox/molecules/data/,\
 OCS/quantum.dat\
 OCS/quantum_ideal.dat\
 OCS/quart.dat\
 OCS/quart_ideal.dat\
 OCS/trit.dat\
 OCS/trit_ideal.dat\
 CO2/quantum.dat\
 CO2/quantum_ideal.dat\
 CO2/quart.dat\
 CO2/quart_ideal.dat\
 CO2/trit.dat\
 CO2/trit_ideal.dat)
molecules.pdf : $(molecules_data) molecules.pyx
	pyxplot molecules.pyx

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

simplehom.pdf : hom.eps simplehom.pyx
	pyxplot simplehom.pyx

sixphoton.pdf : sixphoton.pyx ../reck/data/classical_events.dat\
 ../reck/data/quantum_events.dat
	pyxplot sixphoton.pyx

tevol_data=$(addprefix ../hamiltomo/data/TOpt/,tevol_774.dat\
 tevol_776.dat\
 tevol_778.dat)
tevol.pdf : $(tevol_data) tevol.pyx
	pyxplot tevol.pyx

threesite_data=$(addprefix ../pt/data/threesite/,symmetric/theory/singles0.dat\
 symmetric/theory/singles1.dat\
 symmetric/theory/singles2.dat\
 symmetric/experimental/singles0.dat\
 symmetric/experimental/singles1.dat\
 symmetric/experimental/singles2.dat\
 broken/theory/singles0.dat\
 broken/theory/singles1.dat\
 broken/theory/singles2.dat\
 broken/experimental/singles0.dat\
 broken/experimental/singles1.dat\
 broken/experimental/singles2.dat\
 symmetric/theory/pairs01.dat\
 symmetric/theory/pairs02.dat\
 symmetric/theory/pairs12.dat\
 symmetric/experimental/pairs01.dat\
 symmetric/experimental/pairs02.dat\
 symmetric/experimental/pairs12.dat\
 broken/theory/pairs01.dat\
 broken/theory/pairs02.dat\
 broken/theory/pairs12.dat\
 broken/experimental/pairs01.dat\
 broken/experimental/pairs02.dat\
 broken/experimental/pairs12.dat\
)
threesite_singles.pdf threesite_pairs.pdf: $(threesite_data) threesite.pyx
	pyxplot threesite.pyx

timestep_data=$(addprefix ../hamiltomo/data/,timestep0.dat\
 timestep_1e-04.dat\
 timestep_1e-06.dat\
 timestep_1e-08.dat)
timestep.pdf : $(timestep_data) timestep.pyx
	pyxplot timestep.pyx

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

vibrations.pdf : vibrations.pyx vibrations.png
	pyxplot vibrations.pyx

clean : 
	for f in *.pdf; do if [ -e $$f ]; then rm $$f; fi; done
	for f in *.eps; do if [ -e $$f ]; then rm $$f; fi; done
	for f in *.png; do if [ -e $$f ]; then rm $$f; fi; done


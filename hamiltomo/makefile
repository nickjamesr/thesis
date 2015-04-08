comparison=$(addprefix data/,comparison00.dat\
 comparison01.dat\
 comparison02.dat\
 comparison03.dat\
 comparison04.dat\
 comparison05.dat\
 comparison06.dat)

timestep=$(addprefix data/,timestep0.dat\
 timestep_1e-04.dat\
 timestep_1e-06.dat\
 timestep_1e-08.dat)

$(comparison) : code/comparison.py
	python code/comparison.py

$(timestep) : code/timestep.py
	python code/timestep.py

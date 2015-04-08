comparison=$(addprefix data/,comparison00.dat\
 comparison01.dat\
 comparison02.dat\
 comparison03.dat\
 comparison04.dat\
 comparison05.dat\
 comparison06.dat)

hamiltonians=$(addprefix data/Hamiltonians/,refs0803.dat\
 refs0804.dat\
 refs0806.dat\
 refs0903.dat\
 refs0904.dat\
 refs0906.dat)

timestep=$(addprefix data/,timestep0.dat\
 timestep_1e-04.dat\
 timestep_1e-06.dat\
 timestep_1e-08.dat)

$(comparison) : code/comparison.py
	python code/comparison.py

$(timestep) : code/timestep.py
	python code/timestep.py

data/Hamiltonians/refs0803.dat : code/ReconstructHamiltonian.py\
 data/Unitaries/774_refs0803.dat\
 data/Unitaries/776_refs0803.dat\
 data/Unitaries/778_refs0803.dat
	python code/ReconstructHamiltonian.py 8 3

data/Hamiltonians/refs0804.dat : code/ReconstructHamiltonian.py\
 data/Unitaries/774_refs0804.dat\
 data/Unitaries/776_refs0804.dat\
 data/Unitaries/778_refs0804.dat
	python code/ReconstructHamiltonian.py 8 4

data/Hamiltonians/refs0806.dat : code/ReconstructHamiltonian.py\
 data/Unitaries/774_refs0806.dat\
 data/Unitaries/776_refs0806.dat\
 data/Unitaries/778_refs0806.dat
	python code/ReconstructHamiltonian.py 8 6

data/Hamiltonians/refs0903.dat : code/ReconstructHamiltonian.py\
 data/Unitaries/774_refs0903.dat\
 data/Unitaries/776_refs0903.dat\
 data/Unitaries/778_refs0903.dat
	python code/ReconstructHamiltonian.py 9 3

data/Hamiltonians/refs0904.dat : code/ReconstructHamiltonian.py\
 data/Unitaries/774_refs0904.dat\
 data/Unitaries/776_refs0904.dat\
 data/Unitaries/778_refs0904.dat
	python code/ReconstructHamiltonian.py 9 4

data/Hamiltonians/refs0906.dat : code/ReconstructHamiltonian.py\
 data/Unitaries/774_refs0906.dat\
 data/Unitaries/776_refs0906.dat\
 data/Unitaries/778_refs0906.dat
	python code/ReconstructHamiltonian.py 9 6

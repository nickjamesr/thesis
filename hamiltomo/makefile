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

timestep=$(addprefix data/TOpt/,timestep0.dat\
 timestep_1e-04.dat\
 timestep_1e-06.dat\
 timestep_1e-08.dat)

tevol=$(addprefix data/TOpt/,tevol_774.dat\
 tevol_776.dat\
 tevol_778.dat)

topt=$(addprefix data/TOpt/,ideal.dat experimental.dat)

$(comparison) : code/comparison.py
	python code/comparison.py

$(timestep) : code/timestep.py
	python code/timestep.py

$(tevol) : code/TEvol.py
	python code/TEvol.py

$(topt) : code/TOpt.py
	python code/TOpt.py

### Hamiltonian reconstructions

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

### Unitary reconstructions

data/Unitaries/774_refs0803.dat : code/ReconstructUnitary.py\
 data/Singles/774_absolutes.dat\
 data/774/Dips/refs0803_col09_signs.dat\
 data/774/Dips/refs0803_col10_signs.dat\
 data/774/Dips/refs0803_col11_signs.dat
	python code/ReconstructUnitary.py 774 8 3

data/Unitaries/776_refs0803.dat : code/ReconstructUnitary.py\
 data/Singles/776_absolutes.dat\
 data/776/Dips/refs0803_col09_signs.dat\
 data/776/Dips/refs0803_col10_signs.dat\
 data/776/Dips/refs0803_col11_signs.dat
	python code/ReconstructUnitary.py 776 8 3

data/Unitaries/778_refs0803.dat : code/ReconstructUnitary.py\
 data/Singles/778_absolutes.dat\
 data/778/Dips/refs0803_col09_signs.dat\
 data/778/Dips/refs0803_col10_signs.dat\
 data/778/Dips/refs0803_col11_signs.dat
	python code/ReconstructUnitary.py 778 8 3

data/Unitaries/774_refs0804.dat : code/ReconstructUnitary.py\
 data/Singles/774_absolutes.dat\
 data/774/Dips/refs0804_col09_signs.dat\
 data/774/Dips/refs0804_col10_signs.dat\
 data/774/Dips/refs0804_col11_signs.dat
	python code/ReconstructUnitary.py 774 8 4

data/Unitaries/776_refs0804.dat : code/ReconstructUnitary.py\
 data/Singles/776_absolutes.dat\
 data/776/Dips/refs0804_col09_signs.dat\
 data/776/Dips/refs0804_col10_signs.dat\
 data/776/Dips/refs0804_col11_signs.dat
	python code/ReconstructUnitary.py 776 8 4

data/Unitaries/778_refs0804.dat : code/ReconstructUnitary.py\
 data/Singles/778_absolutes.dat\
 data/778/Dips/refs0804_col09_signs.dat\
 data/778/Dips/refs0804_col10_signs.dat\
 data/778/Dips/refs0804_col11_signs.dat
	python code/ReconstructUnitary.py 778 8 4

data/Unitaries/774_refs0806.dat : code/ReconstructUnitary.py\
 data/Singles/774_absolutes.dat\
 data/774/Dips/refs0806_col09_signs.dat\
 data/774/Dips/refs0806_col10_signs.dat\
 data/774/Dips/refs0806_col11_signs.dat
	python code/ReconstructUnitary.py 774 8 6

data/Unitaries/776_refs0806.dat : code/ReconstructUnitary.py\
 data/Singles/776_absolutes.dat\
 data/776/Dips/refs0806_col09_signs.dat\
 data/776/Dips/refs0806_col10_signs.dat\
 data/776/Dips/refs0806_col11_signs.dat
	python code/ReconstructUnitary.py 776 8 6

data/Unitaries/778_refs0806.dat : code/ReconstructUnitary.py\
 data/Singles/778_absolutes.dat\
 data/778/Dips/refs0806_col09_signs.dat\
 data/778/Dips/refs0806_col10_signs.dat\
 data/778/Dips/refs0806_col11_signs.dat
	python code/ReconstructUnitary.py 778 8 6

# Refcol 9

data/Unitaries/774_refs0903.dat : code/ReconstructUnitary.py\
 data/Singles/774_absolutes.dat\
 data/774/Dips/refs0903_col08_signs.dat\
 data/774/Dips/refs0903_col10_signs.dat\
 data/774/Dips/refs0903_col11_signs.dat
	python code/ReconstructUnitary.py 774 9 3

data/Unitaries/776_refs0903.dat : code/ReconstructUnitary.py\
 data/Singles/776_absolutes.dat\
 data/776/Dips/refs0903_col08_signs.dat\
 data/776/Dips/refs0903_col10_signs.dat\
 data/776/Dips/refs0903_col11_signs.dat
	python code/ReconstructUnitary.py 776 9 3

data/Unitaries/778_refs0903.dat : code/ReconstructUnitary.py\
 data/Singles/778_absolutes.dat\
 data/778/Dips/refs0903_col08_signs.dat\
 data/778/Dips/refs0903_col10_signs.dat\
 data/778/Dips/refs0903_col11_signs.dat
	python code/ReconstructUnitary.py 778 9 3

data/Unitaries/774_refs0904.dat : code/ReconstructUnitary.py\
 data/Singles/774_absolutes.dat\
 data/774/Dips/refs0904_col08_signs.dat\
 data/774/Dips/refs0904_col10_signs.dat\
 data/774/Dips/refs0904_col11_signs.dat
	python code/ReconstructUnitary.py 774 9 4

data/Unitaries/776_refs0904.dat : code/ReconstructUnitary.py\
 data/Singles/776_absolutes.dat\
 data/776/Dips/refs0904_col08_signs.dat\
 data/776/Dips/refs0904_col10_signs.dat\
 data/776/Dips/refs0904_col11_signs.dat
	python code/ReconstructUnitary.py 776 9 4

data/Unitaries/778_refs0904.dat : code/ReconstructUnitary.py\
 data/Singles/778_absolutes.dat\
 data/778/Dips/refs0904_col08_signs.dat\
 data/778/Dips/refs0904_col10_signs.dat\
 data/778/Dips/refs0904_col11_signs.dat
	python code/ReconstructUnitary.py 778 9 4

data/Unitaries/774_refs0906.dat : code/ReconstructUnitary.py\
 data/Singles/774_absolutes.dat\
 data/774/Dips/refs0906_col08_signs.dat\
 data/774/Dips/refs0906_col10_signs.dat\
 data/774/Dips/refs0906_col11_signs.dat
	python code/ReconstructUnitary.py 774 9 6

data/Unitaries/776_refs0906.dat : code/ReconstructUnitary.py\
 data/Singles/776_absolutes.dat\
 data/776/Dips/refs0906_col08_signs.dat\
 data/776/Dips/refs0906_col10_signs.dat\
 data/776/Dips/refs0906_col11_signs.dat
	python code/ReconstructUnitary.py 776 9 6

data/Unitaries/778_refs0906.dat : code/ReconstructUnitary.py\
 data/Singles/778_absolutes.dat\
 data/778/Dips/refs0906_col08_signs.dat\
 data/778/Dips/refs0906_col10_signs.dat\
 data/778/Dips/refs0906_col11_signs.dat
	python code/ReconstructUnitary.py 778 9 6


results_files=$(addprefix data/,classical_experimental.dat\
 classical_ideal.dat\
 fidelities.dat\
 quantum_experimental.dat\
 quantum_ideal.dat\
 quart_experimental.dat\
 quart_ideal.dat\
 trit_experimental.dat\
 trit_ideal.dat)

results_files : code/reconstruct.py
	python code/reconstruct.py

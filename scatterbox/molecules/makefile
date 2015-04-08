ideal=$(addprefix data/,\
 OCS/classical_ideal.dat\
 OCS/quantum_ideal.dat\
 OCS/quart_ideal.dat\
 OCS/trit_ideal.dat\
 CO2/classical_ideal.dat\
 CO2/quantum_ideal.dat\
 CO2/quart_ideal.dat\
 CO2/trit_ideal.dat)
experimental=$(addprefix data/,\
 OCS/classical.dat\
 OCS/quantum.dat\
 OCS/quart.dat\
 OCS/trit.dat\
 CO2/classical.dat\
 CO2/quantum.dat\
 CO2/quart.dat\
 CO2/trit.dat)

$(ideal) : code/makeunitaries.py
	cd code && python makeunitaries.py

$(experimental) : code/analyze.py
	cd code && python analyze.py

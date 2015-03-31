fnames=classical.dat\
 fidelities.dat\
 quantum.dat\
 quart.dat\
 simulated.dat\
 theory.dat\
 trit.dat

symmetric=$(addprefix data/symmetric/,$(fnames))
critical=$(addprefix data/critical/,$(fnames))
broken=$(addprefix data/broken/,$(fnames))
manifolds=$(addprefix data/manifold/,manifold_A.dat rawmanifold_A.dat)

all=$(symmetric) $(critical) $(broken) $(manifolds)

default : $(all)

data/manifold/% : code/manifold.py
	cd code && ./manifold.py

data/symmetric/simulated.dat data/symmetric/theory.dat : code/matrices.py
	cd code && ./matrices.py
data/critical/simulated.dat data/critical/theory.dat : code/matrices.py
	cd code && ./matrices.py
data/broken/simulated.dat data/broken/theory.dat : code/matrices.py
	cd code && ./matrices.py

data/symmetric/classical.dat\
 data/symmetric/fidelities.dat\
 data/symmetric/quantum.dat\
 data/symmetric/quart.dat\
 data/symmetric/trit.dat : code/reconstruct.py
	cd code && ./reconstruct.py
data/critical/classical.dat\
 data/critical/fidelities.dat\
 data/critical/quantum.dat\
 data/critical/quart.dat\
 data/critical/trit.dat : code/reconstruct.py
	cd code && ./reconstruct.py
data/broken/classical.dat\
 data/broken/fidelities.dat\
 data/broken/quantum.dat\
 data/broken/quart.dat\
 data/broken/trit.dat : code/reconstruct.py
	cd code && ./reconstruct.py

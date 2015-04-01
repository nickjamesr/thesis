chapters=$(addprefix chapters/,qcv.tex dialling.tex simulations.tex\
 hamiltomo.tex background.tex)

background_figs=bosonsampling.pdf\
 reck_original.pdf\
 reck_general.pdf\
 
dialling_figs=cascade.pdf\
 example.pdf\
 qubits.pdf\
 recursive.pdf

simulations_figs=manifolds.pdf\
 twosite.pdf\
 circuit.pdf\
 opensystem.pdf

hamiltomo_figs=

qcv_figs=protected/dilbert.png\
 interferometerAB.pdf\
 interferometerCD.pdf\
 rstar.pdf\
 schematic.pdf\
 sixphoton.pdf

figures=$(addprefix figures/, $(background_figs)\
 $(dialling_figs)\
 $(simulations_figs)\
 $(qcv_figs)\
 $(hamiltomo_figs))

thesis.pdf : $(figures) thesis.tex title.tex thesis.sty $(chapters)\
		bib/thesis.bib
	pdflatex thesis
	bibtex thesis
	pdflatex thesis
	pdflatex thesis

%.pdf : thesis.tex thesis.sty chapters/%.tex bib/thesis.bib $(figures)
	pdflatex thesis
	bibtex thesis
	cp thesis.bbl $*.bbl
	pdflatex -jobname=$* "\includeonly{chapters/$*} \input{thesis.tex}"
	pdflatex -jobname=$* "\includeonly{chapters/$*} \input{thesis.tex}"
	pdflatex -jobname=$* "\includeonly{chapters/$*} \input{thesis.tex}"

figures/%.pdf : figures/%.svg figures/%.pyx
	cd figures && $(MAKE) $*.pdf

figures/%.pdf : figures/%.pyx
	cd figures && $(MAKE) $*.pdf

figures/protected/% :
	cd figures/protected &&\
 wget http://www.mostlydowntime.co.uk/physics/thesis/$@

verification/data/clouds/% :
	cd verification/data &&\
 wget http://www.mostlydowntime.co.uk/physics/thesis/data/clouds.tar.gz &&\
 tar xvzf clouds.tar.gz

clean :
	cd figures && $(MAKE) clean
	for f in *.pdf; do if [ -e $$f ]; then rm $$f; fi; done
	for f in *.aux; do if [ -e $$f ]; then rm $$f; fi; done
	for f in chapters/*.aux; do if [ -e $$f ]; then rm $$f; fi; done
	if [ -e thesis.bbl ]; then rm thesis.bbl; fi
	if [ -e thesis.blg ]; then rm thesis.blg; fi
	if [ -e thesis.lof ]; then rm thesis.lof; fi
	if [ -e thesis.log ]; then rm thesis.log; fi
	if [ -e thesis.toc ]; then rm thesis.toc; fi

sweep :
	if [ -e thesis.pdf ]; then rm thesis.pdf; fi
	if [ -e thesis.aux ]; then rm thesis.aux; fi

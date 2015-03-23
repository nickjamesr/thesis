chapters=$(addprefix chapters/,qcvv.tex dialling.tex simulations.tex\
 decoupling.tex hamiltomo.tex introduction.tex)
figures=$(addprefix figures/, circuit.pdf schematic.pdf interferometerAB.pdf\
 interferometerCD.pdf reck_original.pdf reck_general.pdf)

thesis.pdf : $(figures) thesis.tex title.tex thesis.sty $(chapters)\
		bib/thesis.bib
	pdflatex thesis
	bibtex thesis
	pdflatex thesis
	pdflatex thesis

%.pdf : thesis.tex thesis.sty chapters/%.tex bib/thesis.bib
	pdflatex thesis
	bibtex thesis
	cp thesis.bbl $*.bbl
	pdflatex -jobname=$* "\includeonly{chapters/$*} \input{thesis.tex}"
	pdflatex -jobname=$* "\includeonly{chapters/$*} \input{thesis.tex}"
	pdflatex -jobname=$* "\includeonly{chapters/$*} \input{thesis.tex}"

figures/%.pdf : figures/%.svg figures/%.pyx
	cd figures && $(MAKE) $*.pdf

clean :
	@rm *.pdf *.aux chapters/*.aux

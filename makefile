chapters=$(addprefix chapters/,calibration.tex dialling.tex simulations.tex\
 decoupling.tex hamiltomo.tex verification.tex)
figures=scatterbox/calibration/figures/circuit.pdf\
 scatterbox/calibration/figures/schematic.pdf\
 scatterbox/calibration/figures/interferometerAB.pdf\
 scatterbox/calibration/figures/interferometerCD.pdf

thesis.pdf : $(figures) thesis.tex thesis.sty $(chapters) bib/thesis.bib
	pdflatex thesis
	bibtex thesis
	pdflatex thesis
	pdflatex thesis
	@rm thesis.aux thesis.bbl thesis.blg thesis.log thesis.toc chapters/*.aux

%.pdf : thesis.tex thesis.sty chapters/%.tex bib/thesis.bib
	pdflatex thesis
	bibtex thesis
	cp thesis.bbl $*.bbl
	pdflatex -jobname=$* "\includeonly{chapters/$*} \input{thesis.tex}"
	pdflatex -jobname=$* "\includeonly{chapters/$*} \input{thesis.tex}"
	pdflatex -jobname=$* "\includeonly{chapters/$*} \input{thesis.tex}"
	@rm *.aux *.bbl *.blg *.log *.toc chapters/*.aux

scatterbox/calibration/figures/%.pdf : scatterbox/calibration/figures/%.svg scatterbox/calibration/figures/%.pyx
	cd scatterbox/calibration/figures && $(MAKE) $*.pdf

clean :
	@rm *.pdf

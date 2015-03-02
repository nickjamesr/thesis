chapters=$(addprefix chapters/,calibration.tex dialling.tex simulations.tex\
 decoupling.tex hamiltomo.tex verification.tex)

thesis.pdf : thesis.tex thesis.sty $(chapters) bib/thesis.bib
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

upload : thesis.pdf
	@cp thesis.pdf /var/www/html/physics/thesis

clean :
	@rm *.pdf

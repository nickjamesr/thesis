thesis.pdf : thesis.tex bib/thesis.bib
	pdflatex thesis
	bibtex thesis
	pdflatex thesis
	pdflatex thesis
	@rm thesis.aux thesis.bbl thesis.blg thesis.log

upload : thesis.pdf
	@cp thesis.pdf /var/www/html/physics/thesis

clean :
	@rm thesis.aux thesis.bbl thesis.blg thesis.log thesis.pdf

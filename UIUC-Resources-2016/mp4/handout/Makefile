proj4.pdf: proj4.tex
	pdflatex proj4.tex
	pdflatex proj4.tex

clean:
	rm -f proj4.pdf *.aux *.blg *.bbl *.log *.tmp *.xref *.idv *.4og *.4ct *.lg *.4tc *~ *.out

mac: proj4.pdf
	open -a preview.app proj4.pdf

proj5.pdf: proj5.tex
	pdflatex proj5.tex
	pdflatex proj5.tex
	pdflatex proj5.tex

clean:
	rm -f proj5.pdf *.aux *.blg *.bbl *.log *.tmp *.xref *.idv *.4og *.4ct *.lg *.4tc *~ *.out

mac: proj5.pdf
	open -a preview.app proj5.pdf

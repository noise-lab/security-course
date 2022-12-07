final-s16.pdf: final-s16.tex
	pdflatex final-s16.tex
	pdflatex final-s16.tex
	pdflatex final-s16.tex

clean:
	rm -f final-s16.pdf *.aux *.blg *.bbl *.log *.tmp *.xref *.idv *.4og *.4ct *.lg *.4tc *~ *.out

mac: final-s16.pdf
	open -a preview.app final-s16.pdf

final-studyguide.pdf: final-studyguide.tex 
	pdflatex final-studyguide.tex
	pdflatex final-studyguide.tex
	pdflatex final-studyguide.tex

clean:	
	rm -f final-studyguide.pdf *.aux *.blg *.bbl *.log *.tmp *.xref *.idv *.4og *.4ct *.lg *.4tc *~ *.out

mac: final-studyguide.pdf
	open -a preview.app final-studyguide.pdf

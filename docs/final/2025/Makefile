# Makefile for Security Course Midterm Exam
# Builds both student version (no solutions) and solution version

.PHONY: all exam solution clean distclean

# Default target: build both versions
all: exam solution

# Student version (no solutions)
exam: exam.pdf

exam.pdf: exam.tex instructions.tex questions.tex feamster.sty
	pdflatex exam.tex
	pdflatex exam.tex

# Solution version (with solutions)
solution: exam-solution.pdf

exam-solution.pdf: exam.tex instructions.tex questions.tex feamster.sty
	sed 's/\\usepackage\[\]{feamster}/\\usepackage[solution]{feamster}/' exam.tex > exam-solution.tex
	pdflatex exam-solution.tex
	pdflatex exam-solution.tex
	mv exam-solution.pdf exam-solution.pdf

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.out *.toc exam-solution.tex

# Clean everything including PDFs
distclean: clean
	rm -f exam.pdf exam-solution.pdf

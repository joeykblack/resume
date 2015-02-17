SRC = $(wildcard *.md)

PDFS=$(SRC:.md=.pdf)
HTML=$(SRC:.md=.html)
LATEX_TEMPLATE=./pandoc-templates/default.latex

all:    clean gen $(PDFS) $(HTML)

pdf:   clean gen $(PDFS)
html:  clean gen $(HTML)

%.html: %.md
	python resume.py html $(GRAVATAR_OPTION) < $< | pandoc -t html -c resume.css -o $@

%.pdf:  %.md $(LATEX_TEMPLATE)
	python resume.py tex < $< | pandoc --template=$(LATEX_TEMPLATE) -H header.tex -o $@

gen:
    python gen_resume_md.py
    
clean:
	rm -f *.html *.pdf *.md

$(LATEX_TEMPLATE):
	git submodule update --init

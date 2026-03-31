# Makefile for LaTeX-Tutorial
# Compiles all .tex examples and cleans auxiliary files.
#
# Usage:
#   make all       — compile every example
#   make clean     — remove auxiliary files
#   make help      — show targets
#   make examples/document.pdf — compile a single example

SHELL := /bin/bash

# Find all main.tex and standalone .tex files
TEX_MAINS := $(shell find examples -name 'main.tex')
TEX_STANDALONE := examples/document.tex
TEX_ALL := $(TEX_MAINS) $(TEX_STANDALONE)

# Derive PDF targets
PDF_TARGETS := $(TEX_MAINS:main.tex=main.pdf) $(TEX_STANDALONE:.tex=.pdf)

# LaTeX compiler
LATEX := pdflatex
LATEX_FLAGS := -interaction=nonstopmode -halt-on-error

# Biber for bibliography
BIBER := biber

.PHONY: all clean help list

## all: Compile all examples
all: $(PDF_TARGETS)
	@echo "✓ All examples compiled."

## help: Show available targets
help:
	@echo "LaTeX-Tutorial Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  make all        Compile all .tex examples to PDF"
	@echo "  make clean      Remove all generated auxiliary files"
	@echo "  make list       List all .tex files that will be compiled"
	@echo "  make <path>.pdf Compile a single example"
	@echo ""
	@echo "Prerequisites:"
	@echo "  - pdflatex (from TeX Live or MiKTeX)"
	@echo "  - biber (for bibliography examples)"
	@echo "  - TikZ, circuitikz, pgfplots packages"

## list: Show all .tex files
list:
	@echo "Examples to compile:"
	@for f in $(TEX_ALL); do echo "  $$f"; done

# Pattern rule for main.tex files (compile in their own directory)
%/main.pdf: %/main.tex
	cd $(dir $<) && $(LATEX) $(LATEX_FLAGS) main.tex $(if $(findstring bibliography,$(dir $<)), && $(BIBER) main && $(LATEX) $(LATEX_FLAGS) main.tex) && $(LATEX) $(LATEX_FLAGS) main.tex

# Rule for standalone .tex files
examples/document.pdf: examples/document.tex
	cd examples && $(LATEX) $(LATEX_FLAGS) document.tex

## clean: Remove auxiliary files
clean:
	find examples -type f \( \
		-name '*.aux' -o -name '*.log' -o -name '*.out' -o \
		-name '*.toc' -o -name '*.nav' -o -name '*.snm' -o \
		-name '*.vrb' -o -name '*.bbl' -o -name '*.blg' -o \
		-name '*.bcf' -o -name '*.run.xml' -o -name '*.fls' -o \
		-name '*.fdb_latexmk' -o -name '*.synctex.gz' -o \
		-name '*.pdf' \
	\) -delete
	@echo "✓ Cleaned auxiliary files."

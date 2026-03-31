# LaTeX-Tutorial

A comprehensive, hands-on tutorial for learning LaTeX — from your first document to TikZ graphics, Beamer presentations, and beyond.

![latex_tutorial](https://github.com/user-attachments/assets/c6b4fef4-d74d-47e9-b354-b7142a65a621)

## What is LaTeX?

LaTeX is a typesetting system created by Leslie Lamport on top of Donald Knuth's TeX engine (1978). It produces professional-quality documents — books, articles, presentations, and more — by separating content from formatting. LaTeX is the standard in academia for scientific and mathematical writing.

## Quick Start

### Prerequisites

| Tool | Purpose | Options |
|------|---------|---------|
| **TeX distribution** | Compiler + packages | [TeX Live](https://www.tug.org/texlive/), [MiKTeX](https://miktex.org/) |
| **Text editor** | Write `.tex` files | [TeXstudio](https://www.texstudio.org/), [VS Code](https://code.visualstudio.com/) + LaTeX Workshop, [Overleaf](https://www.overleaf.com/) (online) |
| **PDF viewer** | View output | Any PDF reader |

### Compile your first document

```bash
# Clone this repo
git clone https://github.com/djeada/LaTeX-Tutorial.git
cd LaTeX-Tutorial

# Compile the basic example
cd examples
pdflatex document.tex

# Or use the Makefile to compile everything
cd ..
make all
```

## Learning Path

Follow this progression from beginner to advanced. Each link points to a working, commented example in this repo.

### 1. Basics — Document Structure

Start here to understand how a LaTeX document is organized.

| Example | What You'll Learn |
|---------|-------------------|
| [`examples/document.tex`](examples/document.tex) | Document class, packages, title, figures, lists, equations |
| [`document_structure`](examples/document_structure/main.tex) | Report class, chapters, TOC, cross-references, footnotes, appendices |
| [`tables`](examples/tables/main.tex) | Booktabs, multicolumn/multirow, colored rows, custom column types |
| [`page_layout`](examples/page_layout/main.tex) | Geometry, fancyhdr, two-column, margin notes |
| [`letter`](examples/letter/main.tex) | Formal letter class with addresses and signature |

📖 **Reference:** [`notes/cheat_sheet.md`](notes/cheat_sheet.md) — comprehensive command reference

### 2. Text & Code

| Example | What You'll Learn |
|---------|-------------------|
| [`code_listings`](examples/code_listings/main.tex) | Syntax-highlighted code (Python, C, Java), custom languages |
| [`math_advanced`](examples/math_advanced/main.tex) | Align, gather, theorems/proofs, cases, custom operators |
| [`minipages_and_floats`](examples/minipages_and_floats/main.tex) | Side-by-side content, subfigures, wrapfig, float placement |
| [`custom_commands`](examples/custom_commands/main.tex) | `\newcommand`, `\newenvironment`, macros with arguments |
| [`bibliography`](examples/bibliography/main.tex) | BibLaTeX citations, `.bib` files, compiling with Biber |

### 3. TikZ — Drawing Graphics

Learn to create diagrams and figures directly in LaTeX.

| Example | What You'll Learn |
|---------|-------------------|
| [`tikz/basics/coordinate_system`](examples/tikz/basics/coordinate_system/main.tex) | Axes, grid, tick marks, plotting points |
| [`tikz/basics/shapes`](examples/tikz/basics/shapes/main.tex) | Rectangles, circles, ellipses, parabolas |
| [`tikz/basics/variables`](examples/tikz/basics/variables/main.tex) | `\def`, `\pgfmathsetmacro`, `\foreach` loops |
| [`tikz/basics/trigonometric_circle`](examples/tikz/basics/trigonometric_circle/main.tex) | Unit circle, sin/cos triangle, angle arcs |
| [`tikz/basics/triangle_with_angles`](examples/tikz/basics/triangle_with_angles/main.tex) | Labeled angles, side names, filled arcs |
| [`tikz/decorations`](examples/tikz/decorations/main.tex) | Patterns, gradients, shadows, text along paths |

### 4. TikZ — Functions & Plots

| Example | What You'll Learn |
|---------|-------------------|
| [`tikz/functions/area_between_two_curves`](examples/tikz/functions/area_between_two_curves/main.tex) | Parametric curves, shaded regions |
| [`tikz/functions/pgfplots_basics`](examples/tikz/functions/pgfplots_basics/main.tex) | Line plots, bar charts, scatter plots with `pgfplots` |
| [`tikz/functions/plots_3d`](examples/tikz/functions/plots_3d/main.tex) | 3D surfaces, parametric helix, contour plots |

### 5. TikZ — Trees & Graphs

| Example | What You'll Learn |
|---------|-------------------|
| [`tikz/trees/simple_tree`](examples/tikz/trees/simple_tree/main.tex) | Basic tree structure with child nodes |
| [`tikz/trees/red_black_tree`](examples/tikz/trees/red_black_tree/main.tex) | Custom node styles, colored data structure |
| [`tikz/graphs/node_graph`](examples/tikz/graphs/node_graph/main.tex) | Directed graphs, edge labels, self-loops |

### 6. TikZ — Diagrams

| Example | What You'll Learn |
|---------|-------------------|
| [`tikz/flowchart`](examples/tikz/flowchart/main.tex) | Flowchart with decision diamonds, process blocks, routing |
| [`tikz/timeline`](examples/tikz/timeline/main.tex) | Horizontal timeline with events and date markers |
| [`tikz/automata`](examples/tikz/automata/main.tex) | Finite state machines (DFA) with states and transitions |
| [`venn_diagram/union`](examples/tikz/venn_diagram/union/main.tex) | Set union with filled circles |
| [`venn_diagram/intersection`](examples/tikz/venn_diagram/intersection/main.tex) | Scope/clip technique for intersections |
| [`venn_diagram/set_difference`](examples/tikz/venn_diagram/set_difference/main.tex) | Fill-order technique for set difference |

### 7. Physics

| Example | What You'll Learn |
|---------|-------------------|
| [`physics/free_body_diagram`](examples/physics/free_body_diagram/main.tex) | Force vectors, inclined planes, pulleys, Atwood machines |
| [`physics/electric_field_lines`](examples/physics/electric_field_lines/main.tex) | Point charges, dipoles, parallel plates, equipotentials |
| [`physics/optics_ray_diagram`](examples/physics/optics_ray_diagram/main.tex) | Converging lens, concave mirror, prism dispersion |
| [`physics/waves_and_oscillations`](examples/physics/waves_and_oscillations/main.tex) | Standing waves, beats, damped oscillations, EM waves |
| [`physics/thermodynamic_cycle`](examples/physics/thermodynamic_cycle/main.tex) | Carnot cycle, Otto cycle, PV diagrams with pgfplots |
| [`physics/feynman_diagrams`](examples/physics/feynman_diagrams/main.tex) | QED vertex, Compton scattering, gluon exchange, β decay |
| [`physics/quantum_circuit`](examples/physics/quantum_circuit/main.tex) | Bell state, quantum teleportation, GHZ state circuits |

### 8. Electronics

| Example | What You'll Learn |
|---------|-------------------|
| [`electronics/logic_gates`](examples/electronics/logic_gates/main.tex) | AND, OR, NOT, NAND, XOR gates + half adder |
| [`electronics/opamp_circuits`](examples/electronics/opamp_circuits/main.tex) | Inverting, non-inverting, buffer, summing amplifiers |
| [`electronics/filter_circuits`](examples/electronics/filter_circuits/main.tex) | RC/RL/RLC filters with Bode magnitude plots |
| [`electronics/transistor_circuits`](examples/electronics/transistor_circuits/main.tex) | BJT common-emitter, NMOS switch, CMOS inverter |
| [`electronics/timing_diagram`](examples/electronics/timing_diagram/main.tex) | Clock, data, enable waveforms with rising edge markers |
| [`electronics/control_system_block_diagram`](examples/electronics/control_system_block_diagram/main.tex) | PID feedback loop, disturbance rejection, block reduction |

### 9. Basic Circuits

| Example | What You'll Learn |
|---------|-------------------|
| [`circuits/flow_of_current`](examples/circuits/flow_of_current/main.tex) | CircuiTikz basics, batteries, resistors, current labels |
| [`circuits/voltage_source`](examples/circuits/voltage_source/main.tex) | Complex networks with multiple sources |
| [`circuits/voltage_loop`](examples/circuits/voltage_loop/main.tex) | IEC circuit symbols, Kirchhoff's voltage law |

### 10. Presentations

| Example | What You'll Learn |
|---------|-------------------|
| [`presentations/beamer_basics`](examples/presentations/beamer_basics/main.tex) | Beamer slides, themes, columns, blocks, math |

## Tools & Utilities

| Tool | Description |
|------|-------------|
| [`scripts/markdown_to_latex.py`](scripts/markdown_to_latex.py) | Convert Markdown files to Beamer presentations |

Usage:
```bash
python scripts/markdown_to_latex.py input.md -o slides.tex
pdflatex slides.tex
```

## Building All Examples

```bash
make all      # Compile every .tex file
make clean    # Remove auxiliary files
make list     # See all files that will be compiled
make help     # Show all targets
```

## Editors

| Editor | Link |
|--------|------|
| Gummi | https://gummi.app/ |
| Texmaker | https://www.xm1math.net/texmaker/ |
| TeXstudio | https://www.texstudio.org/ |
| Overleaf (online) | https://www.overleaf.com/ |
| VS Code + LaTeX Workshop | https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop |

## Handwriting to LaTeX

* [Detexify](https://detexify.kirelabs.org/classify.html) — Draw a symbol, get the LaTeX command

## References

* [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX) — Comprehensive free reference
* [Overleaf Documentation](https://www.overleaf.com/learn) — Tutorials and guides
* [CTAN](https://ctan.org/) — The Comprehensive TeX Archive Network
* [TikZ & PGF Manual](https://tikz.dev/) — Official TikZ documentation

## Contributing

Pull requests are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines, templates, and code style.

For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

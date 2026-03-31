# Contributing to LaTeX-Tutorial

Thank you for your interest in contributing! This project aims to be a comprehensive, beginner-friendly LaTeX learning resource. Here's how you can help.

## Ways to Contribute

- **Add a new example** — See the template below
- **Improve existing examples** — Better comments, clearer code, bug fixes
- **Expand the cheat sheet** — Add missing commands or sections
- **Fix documentation** — Typos, broken links, unclear explanations
- **Report issues** — Found a bug or have a suggestion? Open an issue

## Getting Started

1. **Fork** the repository
2. **Clone** your fork locally
3. Create a **feature branch**: `git checkout -b add-example-foo`
4. Make your changes
5. **Test** that your `.tex` files compile: `pdflatex main.tex`
6. **Commit** with a clear message: `git commit -m "[feature]: add foo example"`
7. **Push** and open a **Pull Request**

## Adding a New Example

### Directory Structure

Each example lives in its own directory under `examples/`:

```
examples/
  <category>/
    <example_name>/
      main.tex        # The LaTeX source file
```

### Example Template

Every `.tex` file should follow this template:

```latex
% <Title of Example>
% Demonstrates: <what this example teaches>.
% Compile with: pdflatex main.tex

\documentclass{article}
\usepackage{...}

\begin{document}

% --- Section Name ---
% Brief comment explaining what follows

...your LaTeX code...

\end{document}
```

### Requirements for Examples

- [ ] File compiles without errors using `pdflatex`
- [ ] First 3 lines are comment header (title, demonstrates, compile command)
- [ ] Code sections are separated by `% --- Section Name ---` comments
- [ ] No hardcoded absolute paths
- [ ] No external dependencies that require internet access at compile time

## Commit Message Format

Use this format for commit messages:

```
[type]: short description

Optional longer description.
```

Types:
- `[feature]` — New example or capability
- `[fix]` — Bug fix
- `[refactor]` — Code improvement without behavior change
- `[docs]` — Documentation only

## Code Style

- Use **4-space indentation** in `.tex` files
- Use **descriptive comments** — the code should teach, not just demonstrate
- Keep examples **focused** — one concept per file
- Use **UTF-8 encoding** for all files

## Questions?

Open an issue or start a discussion. We're happy to help!

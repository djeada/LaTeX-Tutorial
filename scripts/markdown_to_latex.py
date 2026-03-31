"""Markdown to LaTeX (Beamer) Converter

Converts a Markdown file into a LaTeX Beamer presentation.
Supports headings, lists, inline code, code blocks, bold, italic,
hyperlinks, and images (downloaded to a local directory).

Usage:
    python markdown_to_latex.py input.md -o output.tex
    python markdown_to_latex.py input.md                  # writes to output.tex
"""

import argparse
import os
import re
import sys
import urllib.request
import urllib.error


# ---------------------------------------------------------------------------
# Inline transformations
# ---------------------------------------------------------------------------

def escape_special_chars(text, inside_verbatim=False):
    """Escape LaTeX special characters, skipping verbatim blocks."""
    if inside_verbatim:
        return text
    text = text.replace("_", r"\_")
    text = text.replace("&", r"\&")
    text = text.replace("%", r"\%")
    text = text.replace("#", r"\#")
    return text


def convert_inline_code(text):
    """Convert `code` to \\texttt{code}."""
    return re.sub(r"`([^`]+)`", r"\\texttt{\1}", text)


def convert_bold(text):
    """Convert **bold** to \\textbf{bold}."""
    return re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text)


def convert_italic(text):
    """Convert *italic* to \\textit{italic}."""
    return re.sub(r"\*(.+?)\*", r"\\textit{\1}", text)


def convert_hyperlinks(text):
    """Convert [text](url) to \\href{url}{text}."""
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\\href{\2}{\1}", text)


def apply_inline_transforms(text):
    """Apply all inline Markdown-to-LaTeX conversions."""
    text = convert_inline_code(text)
    text = convert_bold(text)
    text = convert_italic(text)
    text = convert_hyperlinks(text)
    return text


# ---------------------------------------------------------------------------
# Image handling
# ---------------------------------------------------------------------------

def download_images(lines, image_dir="images"):
    """Find ![alt](url) patterns, download images, and rewrite to LaTeX."""
    os.makedirs(image_dir, exist_ok=True)
    result = []
    pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

    for line in lines:
        match = pattern.search(line)
        if match:
            alt_text = match.group(1)
            url = match.group(2)
            filename = os.path.basename(url.split("?")[0])
            local_path = os.path.join(image_dir, filename)

            if not os.path.exists(local_path):
                try:
                    urllib.request.urlretrieve(url, local_path)
                except (urllib.error.URLError, OSError) as exc:
                    print(f"Warning: could not download {url}: {exc}",
                          file=sys.stderr)

            latex = (
                "\\begin{figure}[h!]\n"
                "\\centering\n"
                f"\\includegraphics[width=0.9\\textwidth]{{{local_path}}}\n"
                f"\\caption{{{alt_text}}}\n"
                "\\end{figure}\n"
            )
            result.append(latex)
        else:
            result.append(line)
    return result


# ---------------------------------------------------------------------------
# Block-level transformations
# ---------------------------------------------------------------------------

def process_heading(line):
    """Convert Markdown headings to LaTeX sizing commands."""
    if line.startswith("###"):
        return "\\large\\textbf{" + line.lstrip("#").strip() + "}\n"
    elif line.startswith("##"):
        return "\\Large\\textbf{" + line.lstrip("#").strip() + "}\n"
    elif line.startswith("#"):
        return "\\huge\\textbf{" + line.lstrip("#").strip() + "}\n"
    return None


def process_code_blocks(lines):
    """Convert fenced code blocks (```) to verbatim environments."""
    result = []
    inside_block = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if not inside_block:
                result.append("\\begin{verbatim}\n")
                inside_block = True
            else:
                result.append("\\end{verbatim}\n")
                inside_block = False
        else:
            result.append(line if inside_block else line)
    return result


def process_list_item(line):
    """Convert a single Markdown list item to a LaTeX \\item."""
    match = re.match(r"^(\s*)[-*](.+)$", line) or re.match(r"^(\s*)\d+\.(.+)$", line)
    if match:
        indent = match.group(1)
        content = match.group(2).strip()
        return f"{indent}\\item {content}\n"
    return None


# ---------------------------------------------------------------------------
# Section / slide assembly
# ---------------------------------------------------------------------------

def convert_section(lines):
    """Convert a list of Markdown lines into LaTeX content for one slide."""
    result = []
    in_list = False

    for line in lines:
        heading = process_heading(line)
        if heading:
            if in_list:
                result.append("\\end{itemize}\n")
                in_list = False
            result.append(heading)
            continue

        list_item = process_list_item(line)
        if list_item:
            if not in_list:
                result.append("\\begin{itemize}\n")
                in_list = True
            result.append(list_item)
            continue

        if in_list:
            result.append("\\end{itemize}\n")
            in_list = False

        result.append(apply_inline_transforms(line))

    if in_list:
        result.append("\\end{itemize}\n")
    return result


def split_into_sections(lines):
    """Split lines at heading boundaries to create one section per slide."""
    sections = []
    section = []
    for line in lines:
        if line.startswith("#"):
            if section:
                sections.append(section)
            section = [line]
        else:
            section.append(line)
    if section:
        sections.append(section)
    return sections


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def markdown_to_latex(input_file, output_file):
    """Read a Markdown file and produce a LaTeX Beamer document."""
    with open(input_file, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    # Pre-processing passes
    lines = download_images(lines)
    lines = process_code_blocks(lines)

    # Escape special chars outside verbatim
    inside_verbatim = False
    escaped = []
    for line in lines:
        if "\\begin{verbatim}" in line:
            inside_verbatim = True
        elif "\\end{verbatim}" in line:
            inside_verbatim = False
        escaped.append(escape_special_chars(line, inside_verbatim))
    lines = escaped

    sections = split_into_sections(lines)

    with open(output_file, "w", encoding="utf-8") as fh:
        fh.write("\\documentclass[8pt, notheorems, aspectratio=169]{beamer}\n")
        fh.write("\\usepackage[T1]{fontenc}\n")
        fh.write("\\usepackage{amsmath}\n")
        fh.write("\\usepackage{graphicx}\n")
        fh.write("\\usepackage{hyperref}\n")
        fh.write("\\begin{document}\n\n")

        for section in sections:
            fh.write("\\begin{frame}[fragile]\n")
            for line in convert_section(section):
                fh.write(line)
            fh.write("\\end{frame}\n\n")

        fh.write("\\end{document}\n")

    print(f"Wrote {output_file} ({len(sections)} slides)")


def main():
    parser = argparse.ArgumentParser(
        description="Convert a Markdown file to a LaTeX Beamer presentation."
    )
    parser.add_argument("input", help="Input Markdown file")
    parser.add_argument(
        "-o", "--output", default="output.tex",
        help="Output LaTeX file (default: output.tex)",
    )
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"Error: file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    markdown_to_latex(args.input, args.output)


if __name__ == "__main__":
    main()

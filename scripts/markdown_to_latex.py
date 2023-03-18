import re


def process_headings(line):
    if line.startswith("##"):
        return r"\Large\textbf{" + line[3:].strip() + "}\n"
    elif line.startswith("#"):
        return r"\huge\textbf{" + line[2:].strip() + "}\n"
    else:
        return None


def process_itemized_list(line):
    if line.startswith("-") or line.startswith("*") or re.match(r"^\d+\.", line):
        indentation = re.match(r"^(\s*)", line).group(1)
        return (
            indentation
            + r"\begin{itemize}"
            + "\n"
            + indentation
            + r"\item "
            + line.lstrip(" -*0123456789.").strip()
            + "\n"
            + indentation
            + r"\end{itemize}"
            + "\n"
        )
    else:
        return None


def markdown_to_latex_section(section):
    result = ""
    for line in section:
        heading = process_headings(line)
        itemized_list = process_itemized_list(line)

        if heading:
            result += heading
        elif itemized_list:
            result += itemized_list
        else:
            result += line
    return result


def replace_underscores(strings):
    def replace_underscore_in_string(string):
        return string.replace("_", r"\textunderscore ")

    code_block_delimiter = "```"
    inside_code_block = False
    result = []
    for string in strings:
        if code_block_delimiter in string:
            inside_code_block = not inside_code_block
            result.append(string)
        elif not inside_code_block:
            result.append(replace_underscore_in_string(string))
        else:
            result.append(string)
    return result


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def replace_pairs(str, pair_substring, prefix, suffix):
    pairs = []
    pair = None
    for i in range(len(str)):
        if str[i : i + len(pair_substring)] == pair_substring:
            if pair is None:
                pair = Pair(i, i + len(pair_substring))
            else:
                pair.second = i + len(pair_substring)
                pairs.append(pair)
                pair = None

    if pair is not None:
        pairs.append(pair)

    result = ""
    i = 0
    for pair in pairs:
        result += (
            str[i : pair.first]
            + prefix
            + str[pair.first + len(pair_substring) : pair.second - len(pair_substring)]
            + suffix
        )
        i = pair.second

    result += str[i:]

    return result


def to_string(lst):
    return "\r\n".join(lst)


def to_list(string):
    return string.split("\r\n")


def replace_code_blocks(strings):
    string = to_string(strings)
    result = replace_pairs(string, "```", r"\begin{verbatim}", r"\end{verbatim}")
    return to_list(result)


def replace_inline_code_snipets(strings):
    string = to_string(strings)
    result = replace_pairs(string, "`", r"{\bf ", "}")
    return to_list(result)


def convert_images(strings):
    string = to_string(strings)
    pattern = r"!\[(.*)\]\((.*)\)"
    matches = re.findall(pattern, string)

    for match in matches:
        filename = match[1].split("/")[-1]

        latex = r"\write18{wget " + match[1] + "}\n"
        latex += r"\begin{figure}[h!]"
        latex += r"\centering"
        latex += r"\includegraphics[width=1\textwidth]{" + filename + "}"
        latex += r"\caption{" + match[0] + "}"
        latex += r"\end{figure}"
        string = string.replace("![" + match[0] + "](" + match[1] + ")", latex)

    return to_list(string)


def markdown_to_latex(input_file, output_file):
    with open(input_file, "r") as f:
        content = f.read()
        lines = content.splitlines(True)

    lines = replace_underscores(lines)
    lines = replace_code_blocks(lines)
    lines = replace_inline_code_snipets(lines)
    lines = convert_images(lines)

    sections = []
    section = []
    for line in lines:
        if line.startswith("##") or line.startswith("#"):
            if section:
                sections.append(section)
                section = []
            section.append(line)
        else:
            section.append(line)
    sections.append(section)

    with open(output_file, "w") as f:
        f.write(r"\documentclass[8pt, notheorems, aspectratio=54]{beamer}" + "\n")
        f.write(r"\usepackage[T1]{fontenc}" + "\n")
        f.write(r"\usepackage{amsmath}" + "\n")
        f.write(r"\begin{document}" + "\n")

        for section in sections:
            f.write(r"\begin{frame}[fragile]" + "\n")
            f.write(markdown_to_latex_section(section))
            f.write(r"\end{frame}" + "\n")

        f.write(r"\end{document}" + "\n")


if __name__ == "__main__":
    markdown_to_latex("input.md", "output.tex")

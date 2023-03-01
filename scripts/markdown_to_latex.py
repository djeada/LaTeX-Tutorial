import re

def markdown_to_latex_section(section):
    result = ''
    for line in section:
        if line.startswith("##"):
            result += r'\Large\textbf{' + line[3:].strip() + '}\n'
        elif line.startswith("#"):
            result += r'\huge\textbf{' + line[2:].strip() + '}\n'
        elif line.startswith("-"):
            result += r'\begin{itemize}' + '\n'
            result += r'\item ' + line[2:].strip() + '\n'
            result += r'\end{itemize}' + '\n'
        elif line.startswith("*"):
            result += r'\begin{itemize}' + '\n'
            result += r'\item ' + line[2:].strip() + '\n'
            result += r'\end{itemize}' + '\n'
        else:
            result += line.strip() + '\n'
    return result

def replace_underscores(strings):
    result = []
    for string in strings:
        result.append(string.replace('_', r'\textunderscore '))
    return result

def replace_pairs(strings, pair, prefix, sufix):
    result = []
    in_block = False
    block_start = None
    for i, string in enumerate(strings):
        if pair in string:
            if not in_block:
                in_block = True
                block_start = i
            else:
                in_block = False
                result.append(strings[block_start].replace(pair, prefix ))
                for j in range(block_start+1, i):
                    result.append(strings[j])
                result.append(string.replace(pair, sufix))
                result.append(string)
        else:
            result.append(string)
    return result

def replace_code_blocks(strings):
    return replace_pairs(strings, '```', r'\begin{verbatim}', r'\end{verbatim}')



def markdown_to_latex(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    lines = replace_underscores(lines)
    lines = replace_code_blocks(lines)

    # Create a list to store the sections
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

    with open(output_file, 'w') as f:
        f.write(r'\documentclass{beamer}'+ '\n')
        f.write(r'\usepackage[T1]{fontenc}'+ '\n')
        f.write(r'\usepackage{amsmath}'+ '\n')
        f.write(r'\begin{document}'+ '\n')

        for section in sections:
            f.write(r'\begin{frame}[fragile]'+ '\n')
            f.write(markdown_to_latex_section(section))
            f.write(r'\end{frame}'+ '\n')

        f.write(r'\end{document}'+ '\n')

if __name__ == '__main__':
    markdown_to_latex('input.md', 'output.tex')

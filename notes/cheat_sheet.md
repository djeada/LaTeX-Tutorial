
## Paragraphs and sections

A paragraph is a block of text that is separated from the rest of the text by a blank line. The paragraph is usually indented A paragraph can be started with the *\paragraph* command:

    \paragraph{My first paragraph}
    This is my first paragraph.


Sections are also blocks of text, but they are separated from the rest of the text by a blank line, but they are also used to create a table of contents. Sections are numbered by default and can be nested. A section can be started with the *\section* command:

    \section{Main section}
    This is the main section.

    \subsection{Subsection}
    This is a subsection.

    \subsubsection{Subsubsection}
    This is a subsubsection.


## Formulas

For inline formulas, enclose the formula in `$…$`. For displayed formulas, use `$$…$$`. These will be rendered differently. 

For example, type `$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$` to show:

$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$

or type `$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$` to show:

$$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$$

## Special symbols

There are a very large number of special symbols and notations.

| Command | Result |
| ------- | ------ |
| `\lt` | $\lt$ |
| `\gt` | $\gt$ |
| `\le` | $\le$ |
| `\ge` | $\ge$ |
| `\neq` | $\neq$ |
| `\times` | $\times$ |
| `\cdot` | $\cdot$ |
| `\div` | $\div$ |
| `\in` | $\in$ |
| `\notin` | $\notin$ |
| `\approx` | $\approx$ |
| `\cong` | $\cong$ |
| `\equiv` | $\equiv$ |
| `\aleph_0` | $\aleph_0$ |
| `\nabla` | $\nabla$ |
| `\partial` | $\partial$ |

### Radical signs 

| Command | Result |
| ------- | ------ |
| `\sqrt{x}` | $\sqrt{x}$ |
| `\sqrt{x^3}` | $\sqrt{x^3}$ |
| `\sqrt{x}^3` | $\sqrt{x}^3$ |

### Fractions 

| Command | Result |
| ------- | ------ |
| `\frac{a+1}{b+1}` | $\frac{a+1}{b+1}$ |
| `{a+1\over b+1}` | ${a+1\over b+1}$ |
| `\binom{n+1}{2k}` | $\binom{n+1}{2k}$ |

### Sums and integrals 

| Command | Result |
| ------- | ------ |
| `\sum_{i=0}^\infty i^2` | $\sum\limits_{i=0}^\infty i^2$ |
| `\prod{i=0}^\infty i^2` |  $\prod\limits_{i=0}^\infty i^2$ |
| `\bigcup{i=0}^\infty i^2` |  $\bigcup\limits_{i=0}^\infty i^2$ |
| `\bigcap{i=0}^\infty i^2` |  $\bigcap\limits_{i=0}^\infty i^2$ |
| `\int{i=0}^\infty xdx` |  $\int\limits_{0}^\infty x dx$ |
| `\oint f(z)` |  $\oint\limits_{0}^\infty f(z)$ |

### Functions 

| Command | Result |
| ------- | ------ |
| `\mathbb{R} \to \mathbb{Z}` | $\mathbb{R} \to \mathbb{Z}$ |
| `f \circ g` | $f \circ g$ |

For piecewise functions, use `|x|= \begin{cases} x & x\ge 0\\ -x & x<0 \end{cases}`:

$$
|x|= 
\begin{cases} 
x & x \ge 0\\ 
-x & x \lt 0 
\end{cases}
$$

### Special functions 

| Command | Result |
| ------- | ------ |
| `\sin{x}` | $\sin{x}$ |
| `\ln{10}` | $\ln{10}$ |
| `\max{(x, y)}` | $\max{(x, y)}$ |
| `\lim_{x \to +\infty} f(x)` | $\lim\limits_{x \to +\infty} f(x)$ |

### Logic

| Description | Command | Result |
| ------- | ------ | ------ |
| there exists at least one | `\exists` | $\exists$ |
| there is no | `\nexists` | $\nexists$ |
| for all | `\forall ` | $\forall $ |
| logical not | `\neg` | $\neg$ |
| logical or | `\lor` | $\lor$ |
| logical and | `\land` | $\land$ |
| implies | `\implies` | $\implies$ |
| if and only if | `\iff` | $\iff$ |
| a divides b | `a \mid b` | $a \mid b$ |
| a does not divide b | `a \nmid b` | $a \nmid b$ |

### Sets

| Command | Result |
| ------- | ------ |
| `\varnothing` | $\varnothing$ |
| `\subset` | $\subset$ |
| `\subseteq` | $\subseteq$ |
| `\supset` | $\supset$ |
| `\supseteq` | $\supseteq$ |
| `\cup` | $\cup$ |
| `\cap` | $\cap$ |
| `\setminus` | $\setminus$ |

### Greek letters

Lowercase letters:

| Command | Letter |
| ------- | ------ |
| `\alpha` | $\alpha$ |
| `\beta` | $\beta$ |
| ... | ... |
| `\omega` | $\omega$ |

Uppercase letters:

| Command | Letter |
| ------- | ------ |
| `\Gamma` | $\Gamma$ |
| `\Delta` | $\Delta$ |
| ... | ... |
| `\Omega` | $\Omega$ |

There might be more than one variant for some letters:

| Command | Letter |
| ------- | ------ |
| `\epsilon` | $\epsilon$ |
| `\varepsilon` | $\varepsilon$ |
| `\phi` | $\phi$ |
| `\varphi` | $\varphi$ |

### Superscripts and subscripts

For superscripts and subscripts, use `^` and `_`.
Superscripts, subscripts, and other operations apply only to the next “group”. A “group” is either a single symbol, or any formula surrounded by curly braces `{…}`. If you do `10^10`, you will get a surprise: $10^0$. But `10^{10}` gives what you probably wanted: $10^{10}$. Use curly braces to delimit a formula to which a superscript or subscript applies.

| Command | Result |
| ------- | ------ |
| `x^2` | $x^2$ |
| `log_2` | $log_2$ |
| `x_i^2` | $x_i^2$ |
| `{x_i}^2` | ${x_i}^2$ |
| `x_{i^2}` | $x_{i^2}$ |
| `{x^y}^z` | ${x^y}^z$ |

### Parentheses 

Ordinary symbols are used for parentheses.

| Command | Result |
| ------- | ------ |
| `(x + 5)` | $(x + 5)$ |
| `[x + 5]` | $[x + 5]$ |
| `\\{x + 5\\}` | $\\{x + 5\\}$ |

These do not scale with the formula in between, so if you write `(\frac{\sqrt x}{y^3})` the parentheses will be too small: $(\frac{\sqrt x}{y^3})$. Using `\left(…\right)` will make the sizes adjust automatically to the formula they enclose: $\left(\frac{\sqrt x}{y^3}\right)$.

### Fonts

| Command | Result |
| ------- | ------ |
| `\mathbb{abc}` | $\mathbb{abc}$ |
| `\mathbf{abc}` | $\mathbf{abc}$ |
| `\mathit{abc}` | $\mathit{abc}$ |
| `\pmb{abc}` | $\pmb{abc}$ |
| `\mathtt{abc}` | $\mathtt{abc}$ |
| `\mathrm{abc}` | $\mathrm{abc}$ |
| `\mathsf{abc}` | $\mathsf{abc}$ |
| `\mathscr{abc}` | $\mathscr{abc}$ |
| `\mathfrak{abc}` | $\mathfrak{abc}$ |

### Accents and diacritical marks 

 Command | Result |
| ------- | ------ |
| `\hat` | $\hat{x}$ |
| `\widehat` | $\widehat{xy}$ |
| `\bar` | $\bar{x}$ |
| `\overline` | $\overline{xyz}$ |
| `\vec` | $\vec{x}$ |
| `\dot` | $\dot{x}$ |
| `\ddot` | $\ddot{x}$ |

### Spaces 

You cannot just add extra whitespaces to the formulas to provide more space; this will not impact the final result.
You must use one of the following commands: 

 Command | Result |
| ------- | ------ |
| `a \, b` | $b \\, a$ |
| `a \; b` | $b \\; a$ |
| `a \quad b` | $b \quad a$ |
| `a \qquad b` | $b \qquad a$ |


## Systems of equation

```Latex
\begin{eqnarray*}
  -x + 5y &=& 12 \\
   x - 7y &=& 35
\end{eqnarray*} 
```

$$
\begin{eqnarray*}
  -x + 5y &=& 12 \\
   x - 7y &=& 35
\end{eqnarray*} 
$$

## Matrix

Vector:

```Latex
\begin{bmatrix}
  1 \\
  0 \\
  \vdots \\
  1 \\
\end{bmatrix}
```

$$
\begin{bmatrix}
  1 \\
  0 \\
  \vdots \\
  1 \\
\end{bmatrix}
$$

Square matrix:

```Latex
\begin{bmatrix}
  1 & 0 & 0 \\
  0 & 1 & 0 \\
  0 & 0 & 1 \\
\end{bmatrix}
```

$$
\begin{bmatrix}
  1 & 0 & 0 \\
  0 & 1 & 0 \\
  0 & 0 & 1 \\
\end{bmatrix}
$$

```Latex
\begin{bmatrix}
  1 & 0 & \cdots & 0 \\
  0 & 1 & \cdots & 0 \\
  \vdots & \vdots & \ddots & \vdots \\
  0 & 0 & \cdots & 1 \\
\end{bmatrix}
```

$$
\begin{bmatrix}
  1 & 0 & \cdots & 0 \\
  0 & 1 & \cdots & 0 \\
  \vdots & \vdots & \ddots & \vdots \\
  0 & 0 & \cdots & 1 \\
\end{bmatrix}
$$


## Matrix equations

```Latex
\left(
  \begin{array}{rr}
    -1 & 5 \\
    1 & -7  \\
  \end{array}
\right)\left(
  \begin{array}{c}
    x \\
    y \\
  \end{array}
\right) = \left(
  \begin{array}{c}
    12 \\
    35 \\
  \end{array}
\right)
```

$$
\left(
  \begin{array}{rr}
    -1 & 5 \\
    1 & -7  \\
  \end{array}
\right)\left(
  \begin{array}{c}
    x \\
    y \\
  \end{array}
\right) = \left(
  \begin{array}{c}
    12 \\
    35 \\
  \end{array}
\right)
$$

## Augumented matrix

```Latex
[A|\boldsymbol{b}] = 
\left[
  \begin{array}{rr|r}
    2 & 3 & 7 \\
    1 & -4 & 3  \\
  \end{array}
\right]
```

$$
[A|\boldsymbol{b}] = 
\left[
  \begin{array}{rr|r}
    2 & 3 & 7 \\
    1 & -4 & 3  \\
  \end{array}
\right]
$$

## Tables

Tables are created using the `tabular` environment. The first line of the environment contains the column specification. The `l` column type is for left-aligned text, `c` is for centered text, and `r` is for right-aligned text. The `|` symbol is used to add vertical lines between columns. The rows are separated by `\\` and the columns are separated by `&`.


```Latex
\begin{table}[t]
\begin{tabular}{l|c|c}
\# & Displacement & Force \\
\hline
1 & 11.2cm & 8N \\
2 & 17.3cm & 12N \\
3 & 23.5cm & 15N
\end{tabular}
\caption{The outcomes of a certain measurement}\label{table:measurement}
\end{table}
```

| # | Displacement | Force |
| - | ------------ | ----- |
| 1 | 11.2cm | 8N |
| 2 | 17.3cm | 12N |
| 3 | 23.5cm | 15N |

## Lists

Ordered lists:

```Latex
\begin{enumerate}
 \item one
 \item two
 \item three
\end{enumerate}
```

1. one
1. two
1. three

Unordered lists:


```Latex
\begin{itemize}
 \item one
 \item two
 \item three
\end{itemize}
```

* one
* two
* three

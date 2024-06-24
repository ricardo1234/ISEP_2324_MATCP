```table-of-contents
```
- [Teórica](https://moodle.isep.ipp.pt/pluginfile.php/368688/mod_resource/content/1/CAP%C3%8DTULO%203_MATCP_LEI_2023_2024_V2.pdf)
- [Exercicios](https://moodle.isep.ipp.pt/pluginfile.php/366721/mod_resource/content/1/Exercicios_MATCP_Capitulo_3_LEI_2023_24.pdf)
- [DISTRIBUIÇÃO BINOMIAL](DISTRIBUIÇÃO%20BINOMIAL.md)
- [DISTRIBUIÇÃO POISSON](DISTRIBUIÇÃO%20POISSON.md)
- [DISTRIBUIÇÃO UNIFORME](DISTRIBUIÇÃO%20UNIFORME.md)
- [DISTRIBUIÇÃO EXPONENCIAL](DISTRIBUIÇÃO%20EXPONENCIAL.md)
- [DISTRIBUIÇÃO NORMAL](DISTRIBUIÇÃO%20NORMAL.md)

## VARIAVEIS ALEATÓRIAS DISCRETAS
### Exercício 1

#### 1.1) Estabeleça a função de probabilidade do número de bombons de chocolate branco na amostra.
X:"Número de chocolates brancos em 3 escolhidos ao acaso"
A:"Sair chocolate Branco"

$f(x) = P(X=x)$

$P(X=0) = P(\overline{A}\overline{A}\overline{A})=\frac{6}{8}\times \frac{5}{7}\times \frac{4}{6} = \frac{5}{14}$
$P(X=1) = P(A\overline{A}\overline{A}+\overline{A}A\overline{A}+\overline{A}\overline{A}A)=\frac{2}{8}\times \frac{6}{7}\times \frac{5}{6} \times 3 = \frac{15}{28}$
$P(X=2) = P(AA\overline{A}+\overline{A}AA+A\overline{A}A)=\frac{2}{8}\times \frac{1}{7}\times \frac{6}{6} \times 3 = \frac{3}{28}$

#### 1.2) Determine o do esperado de bombons de chocolate branco na amostra.
$\mu = \sum{(x)} = \sum{x\times f(x)} = 0\times\frac{5}{14}+1\times\frac{15}{28}+2\times\frac{3}{28} = \frac{3}{4}=0,75$

#### 1.3) Constatou-se que a amostra continha no máximo um bombom de chocolate branco. Qual a probabilidade da amostra conter exatamente um?
$P(X=1|X\geq1) = \frac{P(X=1\cup X\geq1)}{P(X\geq1)} = \frac{P(X=1)}{P(X\geq1)} = \frac{\frac{15}{28}}{\frac{5}{14}+\frac{15}{28}} = \frac{3}{5} = 0,6$

### Exercício 3

#### 3.1) Calcule o valor de k e de a sabendo que $E(X) = \frac{13}{3}$.
$$
\left\{ \begin{array}{c} 
E(X) = \frac{13}{3}  \\ 
\sum_{i=1}^4 f(x_i) = 1
\end{array} \right. \iff
\left\{ \begin{array}{c} 
2f(2) + 3f(3) + 4f(4) + ak = \frac{13}{3}   \\ 
f(2) + f(3) + f(4) + f(a) = 1
\end{array} \right. \iff
\left\{ \begin{array}{c} 
2\times\frac{1}{4} + 3\times\frac{1}{3} + 4\times\frac{3}{16} + ak = \frac{13}{3}   \\ 
\frac{1}{4} + \frac{1}{3} + \frac{3}{16} + k = 1
\end{array} \right. \iff
\left\{ \begin{array}{c} 
\frac{11}{48} a = \frac{13}{3}   \\ 
k = \frac{11}{48}
\end{array} \right. \iff
\left\{ \begin{array}{c} 
a = \frac{100}{11}   \\ 
k = \frac{11}{48}
\end{array} \right.
$$
#### 3.2) Determine a expressão analítica da função de distribuição acumulada F(x).

|  $x$   |      $2$      |      $3$      |      $4$       | $\frac{100}{11}$ |
| :----: | :-----------: | :-----------: | :------------: | :--------------: |
| $f(x)$ | $\frac{1}{4}$ | $\frac{1}{3}$ | $\frac{3}{16}$ | $\frac{11}{48}$  |

$x \lt 2 \Rightarrow F(x) = P(X \le x) = 0$
$2 \le x \lt 3 \Rightarrow F(x) = P(X = 2) = \frac{1}{4}$
$3 \le x \lt 4 \Rightarrow F(x) = P(X = 2) + P(X = 3)= \frac{1}{4} + \frac{1}{3} = \frac{7}{12}$
$4 \le x \lt \frac{100}{11} \Rightarrow F(x) = P(X = 2) + P(X = 3) + P(X = 4)= \frac{1}{4} + \frac{1}{3} + \frac{3}{16} = \frac{37}{48}$
$x \ge \frac{100}{11} \Rightarrow F(x) = 1$

$$ \begin{align}
F(x) = \left\{ \begin{array}{c} 
0 , x \lt 2  \\ 
\frac{1}{4}, 2 \le x \lt 3 \\
\frac{7}{12}, 3 \le x \lt 4 \\
\frac{37}{48}, 4 \le x \lt \frac{100}{11} \\
1, x \ge \frac{100}{11} \\
\end{array} \right.
\end{align}
$$
#### 3.3) Calcule a variância de X, var(X).

$\partial^2 = var(X) = E(X^2) - E^2(X) = \sum_x x^2f(x) - \mu^2 = \frac{856}{33} - (\frac{13}{3})^2 = \frac{709}{99} \simeq 7,16$
$\sum_x x^2f(x) = 2^2\times\frac{1}{4} + 3^2\times\frac{1}{3} + 4^2\times\frac{3}{16} + (\frac{100}{11})^2\times\frac{11}{48} = \frac{856}{33}$

### Exercício 4

X: Número de defeitos em 100 metros.

|  $x$   |  $0$   |  $1$   |  $2$   |  $3$   | $4$    | $5$    |
| :----: | :----: | :----: | :----: | :----: | ------ | ------ |
| $f(x)$ | $0.10$ | $0.35$ | $0.25$ | $0.15$ | $0.10$ | $0.05$ |

#### 4.1)  Determine: P(0 < X ≤ 2).
$$
	P(0 \lt X \le 2) 
\begin{array}[t]{l}
	\space = P(X=1) + P(X = 2) \\
	 \space = 0,35 + 0,25 \\
	\space = 0.26
\end{array}
$$
#### 4.2) A probabilidade de, em 100 metros de cabo, existirem não mais de três defeitos
$$
	P(X \le 3) 
\begin{array}[t]{l}
	\space = P(X=0) + P(X=1) + P(X = 2) + P(X=3) \\
	 \space = 0.1 + 0.35 + 0.25 + 0.15 \\
	\space = 0.85
\end{array}
$$
#### 4.3) A probabilidade de, em 100 metros de cabo, o número de defeitos ser superior a dois.
$$
	P(X \gt 2) 
\begin{array}[t]{l}
	\space = 1 - (P(X=0) + P(X=1) + P(X = 2)) \\
	 \space = 1 - (0.1 + 0.35 + 0.25) \\
	\space = 0.3
\end{array}
$$
#### 4.4) A expressão analítica da função de distribuição acumulada de X.

$$ \begin{align}
F(x) = \left\{ \begin{array}{l} 
0 \space\space\space\space\space\space\space,\space\space\space  x \lt 0  \\ 
0.1 \space\space\space\space,\space\space\space 0 \le x \lt 1 \\
0.45 \space\space,\space\space\space 1 \le x \lt 2 \\
0.7 \space\space\space\space,\space\space\space 2 \le x \lt 3 \\
0.85 \space\space,\space\space\space 3 \le x \lt 4 \\
0.95 \space\space,\space\space\space 4 \le x \lt 5 \\
1 \space\space\space\space\space\space\space,\space\space\space x \ge 5 \\
\end{array} \right.
\end{align}
$$
#### 4.5) A média e a variância de X.

$\mu = 0 \times 0.1 + 1 \times 0.35 + 2 \times 0.25 + 3 \times 0.15 + 4 \times 0.1 + 5 \times 0.05 = 1.95$
$E(x^2) = o^2 \times 0.1 + 1^2 \times 0.35 + 2^2 \times 0.25 + 3^2 \times 0.15 + 4^2 \times 0.1 + 5^2 \times 0.05 = 5.55$
$var(X) = E(x^2) - \mu^2 = 5.55 - 1.95^2 = 1.75$





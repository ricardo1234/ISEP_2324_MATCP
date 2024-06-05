```table-of-contents
```
## Teórica

### Definição da v.a.
X v.a. que representa o numero de sucessos em $n$ tentativas de Bernoulli com probabilidade $p$ de sucesso em cada tentativa
### Notação
$X \sim Bi(n, p)$ 
$n$ -> Número de tentativas
$p$ -> Probabilidade de sucesso
### Parâmetros:
$n \in IN$ e $p \in \space ]0, 1[$
### Função de probabilidade
$$
f(x) = 
\left\{
\begin{array}{l}
 ^nC_x p^x(1-p)^{n-x} , x \in \{0,1,...,n\} \\
0,\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space, x \notin \{0,1,...,n\}
\end{array} 
\right.
$$
em que $^nC_x$ representa o número de maneiras distintas de se conseguir $x$ sucessos em $n$ tentativas.
### Média
$E(X) = \mu_X = np$
### Variância
$var(X) = \sigma^2_X = np(1-p)$
### Função de distribuição acumulada
$$
f(x) = 
\left\{
\begin{array}{l}
0,\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space x\lt0 \\
 \sum^{Int[X]}_{i=0} p^i(1-p)^{n-i}) , x \le x \le n\\
0,\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space x\gt n \\
\end{array} 
\right.
$$

## Código Python
### Biblioteca 
``` python
from scipy import stats
```
### Calcular X = x
```python
stats.binom.pmf(x, n, p)
```
### Calcular X <= x
```python
stats.binom.cdf(x, n, p)
```
### Calcular X > x
```python
1 - stats.binom.cdf(x, n, p)
```
**Nota**
	Caso seja maior ou igual temos de calcular a probabilidade do número antes de x
### Calcular z < X <= x
```python
stats.binom.cdf(x, n, p) - stats.binom.cdf(z, n, p)
```
**Nota**
	Caso seja maior ou igual temos de calcular a probabilidade de do número antes de z

## Extensão da classe "scipy"

```python
from scipy import stats

class BinomialExtension:
    def __init__(self, n, p):
        self.n = n
        self.p = p

    def Equal(self, x, toPercentage=False):
        return stats.binom.pmf(x, self.n, self.p)*(100 if toPercentage else 1)

    def LessOrEqual(self, x, toPercentage=False):
        return stats.binom.cdf(x, self.n, self.p)*(100 if toPercentage else 1)

    def Less(self, x, passe = 1, toPercentage=False):
        return stats.binom.cdf(x-passe, self.n, self.p)*(100 if toPercentage else 1)

    def Greater(self, x, toPercentage=False):
        return 1 - stats.binom.cdf(x, self.n, self.p)*(100 if toPercentage else 1)

    def GreaterOrEqual(self, x, passe = 1, toPercentage=False):
        return 1 - stats.binom.cdf(x-passe, self.n, self.p)*(100 if toPercentage else 1)

    def GreaterAndLessOrEqual(self, a, b, toPercentage=False):
        return stats.binom.cdf(b, self.n, self.p) - stats.binom.cdf(a, self.n, self.p)*(100 if toPercentage else 1)

    def GreaterOrEqualAndLessOrEqual(self, a, b, passe = 1, toPercentage=False):
        return stats.binom.cdf(b, self.n, self.p) - stats.binom.cdf(a-passe, self.n, self.p)*(100 if toPercentage else 1)

    def GreaterOrEqualAndLess(self, a, b, passe = 1, toPercentage=False):
        return stats.binom.cdf(b-passe, self.n, self.p) - stats.binom.cdf(a, self.n, self.p)*(100 if toPercentage else 1)

    def GreaterAndLess(self, a, b, passe = 1, toPercentage=False):
        return stats.binom.cdf(b-passe, self.n, self.p) - stats.binom.cdf(a-passe, self.n, self.p)*(100 if toPercentage else 1)
```
## Exercícios

### Exercício 11

X: Número de motores a funcionar em 4.
$X \sim Bi(n,p)$
$n = 4$
$p = 0.99$
$P(X  \ge 2) \ - P(X \lt 2) = 1- P(x \le 1) \simeq 0.999996$

``` python
from scipy import stats
n = 4
p = 0.99
x = 1
print(f"A probabilidade de x <= 1 : {stats.binom.cdf(x, n, p):.6f}")
print(f"A probabilidade de x > 1 : {1 - stats.binom.cdf(x, n, p):.6f}")
```
[Source Code](Capítulo%203/src/Exercicio_11.py)
	A probabilidade de x <= 1 : 0.000004
	A probabilidade de x > 1 : 0.999996

### Exercício 13

#### 13.1) A percentagem de lotes que são vendidos sem inspeção de todos os elementos.

X: Número de componentes defeituosos em 6 ao acaso.
$X \sim Bi(n,p)$
$n = 6$
$p = 0.04$
$P(X = 0) = 78.3\%$

``` python
from scipy import stats
n = 6
p = 0.04
x = 0
print(f"A probabilidade de x = 0 : {(stats.binom.pmf(x, n, p)*100):.1f}%")
```
[Source Code](Capítulo%203/src/Exercicio_13.py)
	A probabilidade de x = 0 : 78.3%
#### 13.2) A probabilidade de ser necessário uma inspeção total do lote.

$P(X \ge 1) = 1 - P(X = 0) = 1 - 0.783 \sim 0.217 \sim 0.2\%$
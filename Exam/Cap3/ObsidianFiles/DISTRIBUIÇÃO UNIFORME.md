```table-of-contents
```
## Teórica

### Definição da v.a.
X v.a. tal que a sua probabilidade de tomar um valor num subintervalo de $[a, b]$ é proporcional ao comprimento desse subintervalo.
### Notação
$X \sim U(a,b)$ 
$a$ -> Limite Inferior
$b$ -> Limite Superior
### Parâmetros:
$a, b => a \le b$
### Função de probabilidade
$$
f(x) = 
\left\{
\begin{array}{l}
 \frac{1}{b-a} , x \in [a,b] \\
0,\space\space\space, x \notin [a,b]
\end{array} 
\right.
$$
### Média
$E(X) = \mu_X = \frac{a + b}{2}$
### Variância
$VAR(X) = \sigma^2_X = \frac{(b - a)^2}{12}$
### Função de distribuição acumulada
$$
f(x) = 
\left\{
\begin{array}{l}
0,\space\space\space\space\space X\lt a \\
 \frac{x - a}{b - a}, X \in [a, b]\\
 1,\space\space\space\space\space X\gt b \\
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
stats.uniform.pmf(x, a, b)
```
### Calcular X <= x
```python
stats.uniform.cdf(x, a, b)
```
### Calcular X > x
```python
1 - stats.uniform.cdf(x, a, b)
```
### Calcular z < X <= x
```python
stats.uniform.cdf(x, a, b) - stats.uniform.cdf(z, a, b)
```
## Exercícios

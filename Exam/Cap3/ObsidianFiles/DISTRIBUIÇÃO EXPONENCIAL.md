```table-of-contents
```
## Teórica

### Definição da v.a.
X v.a. representa o intervalo de tempo entre dois eventos independentes.
### Notação
$X \sim$ Exp$(\beta)$ 
$\frac{1}{\beta}$ -> representa o numero médio de eventos que ocorrem por unidade de tempo ou região espacial.
$\beta = \frac{1}{\lambda}$
### Parâmetros
$\beta \gt 0$
### Função de probabilidade
$$
f(x) = 
\left\{
\begin{array}{l}
 0 , \space\space\space \space\space\space \space\space x \lt 0 \\
\frac{1}{\beta}e^{-\frac{x}{\beta}}, x \ge 0
\end{array} 
\right.
$$
### Média
$E(X) = \mu_X = \beta$
### Variância
$VAR(X) = \sigma^2_X = \beta^2$
### Função de distribuição acumulada
$$
f(x) = 
\left\{
\begin{array}{l}
 0 , \space\space\space\space\space\space\space\space\space\space \space\space x \lt 0 \\
1 - e^{-\frac{x}{\beta}}, x \ge 0\\
\end{array} 
\right.
$$

## Resultados sem Python


## Código Python
### Biblioteca 
``` python
from scipy import stats
```
### Calcular X = x
```python
stats.expon.pmf(x, loc=0, scale=beta)
```
### Calcular X <= x
```python
stats.expon.cdf(x, loc=0, scale=beta)
```
### Calcular X > x
```python
1 - stats.expon.cdf(x, loc=0, scale=beta)
```
### Calcular z < X <= x
```python
stats.expon.cdf(x, loc=0, scale=beta) - stats.expon.cdf(z, loc=0, scale=beta)
```
## Exercícios

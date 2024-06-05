```table-of-contents
```
## Teórica

### Definição da v.a.
X v.a. representa  uma distribuição simétrica.
### Notação
$X \sim N(\mu, \sigma^2)$ 
### Parâmetros
$u$ -> representa a média
$\sigma^2$ -> representa a variância
### Função de probabilidade
$$
f(x) = 
 \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{1}{2}(\frac{x - \mu}{\sigma})^2} , \ x \in I\!R \\
$$
### Média
$E(X) = \mu$
### Variância
$VAR(X) = \sigma^2$
### Distribuição normal estandardizada
$$
X \sim N(\mu, \sigma^2) \Rightarrow Z = \frac{X - \mu}{\sigma} \sim N(0,1)
$$
### Função de distribuição acumulada
$$
F(X) = P(X \le x) = \frac{1}{\sqrt{2\pi\sigma^2}} \int_{-\infty}^x e^{-\frac{1}{2}(\frac{x-\mu)}{\sigma})^2} dt
$$
### Relação media e desvio padrão
- Na distribuição normal aproximadamente 68% da população difere da media menos de 1 desvio padrão :
	$P(\mu - \sigma \lt X \lt \mu - \sigma) \approx 0.68$
- Na distribuição normal aproximadamente 95% da população difere da media menos de 2 desvio padrão :
	$P(\mu - 2\sigma \lt X \lt \mu + 2\sigma) \approx 0.95$
- Na distribuição normal aproximadamente 99.7% da população difere da media menos de 3 desvio padrão :
	$P(\mu - 3\sigma \lt X \lt \mu + 3\sigma) \approx 0.997$

## Código Python
### Biblioteca 
``` python
from scipy import stats
```
### Calcular X = x
```python
stats.norm.pmf(x, u, o)
```
### Calcular X <= x
```python
stats.norm.cdf(x, u, o)
```
### Calcular X > x
```python
1 - stats.norm.cdf(x, u, o)
```
### Calcular z < X <= x
```python
stats.norm.cdf(x, u, o) - stats.norm.cdf(z, u, o)
```
### Calcular x pela percentagem
```python
stats.norm.ppf(p, u, o)
```

## Exercícios

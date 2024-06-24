
## Continuas

### Função densidade probabilidade

$$ P(a \leq X \leq X) = \int_a^b f(X) dx, \forall a,b \in \mathbb{R} : a \leq b $$
### Função de distribuição Acumulada

$$ F(X) = P (X \leq x) = \int_{-\infty}^x f(u) du $$

## Python Para Matematica em geral

### Integrais
#### Biblioteca 
``` python
import scipy.integrate as integrate
```

#### Exemplo 
$$ \int_1^{1.4} x^{0.2} \times exp(-x^{0.2}) $$
``` python
integrate.quad(lambda x: x**0.2 * np.exp(-x**0.2),1,1.4)
```


### Logaritmo / Raiz Quadrada
#### Biblioteca 
``` python
import numpy as np
```

#### Exemplo Logaritmo
$$ log(0.11) $$
``` python
np.log(0.11)
```

#### Exemplo Raiz Quadrada

$$ \sqrt4 $$
``` python
np.sqrt(4)
```

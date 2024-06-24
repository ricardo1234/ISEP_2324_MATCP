import scipy.integrate as integrate
from scipy import stats
import numpy as np

# P1

# 1.
result_1 = integrate.quad(lambda x: x**0.2 * np.exp(-x**0.2),1,1.4)
valor_lambda = 1 / result_1[0]
print(f'P1(1.) O resultado do integral é {result_1[0]:.2f} e o valor pretendido é {valor_lambda:.2f}')

# 2.
result_2 = integrate.quad(lambda x: valor_lambda * x**0.2 * np.exp(-x**0.2),1,1.2)
print(f'P1(2.) O valor da probabilidade é {result_2[0]:.2f}')

# 3.
result_3 = integrate.quad(lambda x: valor_lambda * x**0.2 * np.exp(-x**0.2),1,1.3)
print(f'P1(3.) O valor da probabilidade é {result_3[0]:.2f}')

# 4.
result_4 = integrate.quad(lambda x: valor_lambda * x**0.2 * np.exp(-x**0.2),1.35, 1.4)
print(f'P1(4.) O valor da probabilidade é {result_4[0]:.2f}')

# 5.
valor_esperado = integrate.quad(lambda x: x * valor_lambda * x**0.2 * np.exp(-x**0.2),1,1.4)
print(f'P1(5.) O valor esperado é {valor_esperado[0]:.2f}')

# P2

# 1.1
p1 = 1 - stats.poisson.cdf(6,4.4)
print(f'P2(1.1) A probabilidade é {p1:.4f}')

# 1.2
p2 = stats.poisson.cdf(11,4 * 5.4)
print(f'P2(1.2) A probabilidade é {p2:.4f}')

# 1.3
p3 = stats.poisson.cdf(14, 4.4 + 5.4) - stats.poisson.cdf(10, 4.4 + 5.4)
print(f'P2(1.3) A probabilidade é {p3:.4f}')

# 2.1
p4 = stats.norm.cdf(15,12,4) - stats.norm.cdf(10,12,4)
print(f'P2(2.1) A probabilidade é {p4:.4f}')

# 2.2
p5 = stats.norm.cdf(15, 12, np.sqrt(16 / 10)) - stats.norm.cdf(10, 12, np.sqrt(16 / 10))
print(f'P2(2.2) A probabilidade é {p5:.4f}')

# 2.
p6 = stats.norm.cdf(15, 12, 4)
print(f'A probabilidade de esperar menos de 15 minutos é {p6:.4f}')
p7 = stats.binom.pmf(36, 55, p6)
print(f'P2(3.) A probabilidade é {p7:.4f}')

# P3

# 1.
beta = -0.7 / np.log(0.11)
print(f'P3(1.) Beta = {beta:.4f}')

# 2.
p8 = 1 - stats.gamma.cdf(1.5, a = 1, scale = beta)
print(f'A probabilidade é {p8:.4f}')

p9 = 1 - stats.gamma.cdf(2.3, a = 1, scale = beta)
p10 = 1 - stats.gamma.cdf(1.5, a = 1, scale = beta)
print(f'P3(2.) A probabilidade é {p9 / p10:.4f}')

#3.
q = stats.gamma.ppf(0.5, a = 1, scale = beta)
print(f'P3(3.) q={q:.4f}')

# P4

# 1.1
p11 = stats.norm.cdf(300, 295,14)
print(f'P4(1.1) A probabilidade é {p11:.4f}')

# 1.2
p12 = stats.norm.cdf(0, 295 - 330, np.sqrt(9**2 + 14**2))
print(f'P4(1.2) A probabilidade é {p12:.4f}')

# 1.3
mu = 5 * 295 + 5 * 330 + 550
sigma_qua = 5 * (9**2) + 5 * (14**2)
print(f'P4(1.3) O valor de mu={mu:.4f} e valor sigma é {np.sqrt(sigma_qua):.4f}')

# 1.4
p13 = 1 - stats.norm.cdf(3700, mu, np.sqrt(sigma_qua))
print(f'P4(1.4) A probabilidade é {p13:.4f}')

# 2.1
p14 = 1- stats.binom.cdf(6, 12, 1 - p13)
print(f'P4(2.1) A probabilidade é {p14:.4f}')

# 2.2
p15 = 1- stats.binom.pmf(4, 12, 1 - p13)
print(f'P4(2.2) A probabilidade é {p15:.4f}')


# P5

valor = stats.norm.ppf(0.95, 0, np.sqrt(4.82**2/70+4.38**2/95))
print(f'(P5) O limite inferior da RR é {valor:.2f}')

# P6

valor = stats.norm.ppf(0.95,0.5,np.sqrt(0.5 * (1 - 0.5) / 50))
print(f'(P6) O limite inferior da RR é {valor:.2f}')

# P7

# 1.
n = 480
bagagens = 2940 + 3010
média = bagagens / n
sigma = 6
alfa = 0.05
valor = 1 - alfa / 2
valor_z = stats.norm.ppf(valor, 0, 1)
print(f'Valor de z = {valor_z:.4f}')
lim_inf = média - valor_z * sigma / np.sqrt(n)
lim_sup = média + valor_z * sigma / np.sqrt(n)
print(f'P7(1.) O IC para a média é [{lim_inf:.3f},{lim_sup:.3f}]')

# 2.

n = 420
faltaram = 420 - 368
prop_amostral = faltaram / n
lim_inf = prop_amostral - valor_z * np.sqrt(prop_amostral * (1 - prop_amostral) / n)
lim_sup = prop_amostral + valor_z * np.sqrt(prop_amostral * (1 - prop_amostral) / n)
print(f'P7(2.) O IC para a proporção é [{lim_inf:.3f},{lim_sup:.3f}]')

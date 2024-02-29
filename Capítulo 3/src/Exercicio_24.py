from scipy import stats

n = 0
media = 1

#24.1
p0 = stats.poisson.pmf(n, media)
print(f"A probabilidade de x = 0 : {p0:.3f}")
print(f"A probabilidade de x > 0 : {(1 - p0):.3f}")

#24.2
n2 = 1
p_le1 = stats.poisson.cdf(n2, media)
print(f"A probabilidade de x <= 1 : {p_le1:.3f}")
print(f"A probabilidade de x > 1 : {(1-p_le1):.3f}")
print((1-p_le1)/(1-p0))
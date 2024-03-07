from scipy import stats

n = 0
media = 0.5

p0 = stats.poisson.pmf(n, media)
print(f"A probabilidade de x = 0 : {p0:.3f}")
print(f"A probabilidade de x > 0 : {(1 - p0):.3f}")

p = 0.393
n = 5
x = 0
print(f"A probabilidade de x = 0 : {(stats.binom.pmf(x, n, p)):.3f}")
from scipy import stats

n = 3
media = 2

# 25.1
p_le3 = stats.poisson.cdf(n, media)
print(f"A probabilidade de x <= 3 = {p_le3:.4f}")
print(f"A probabilidade de x > 3 = {(1 - p_le3):.4f}")

# 25.2
p = 0.98
n_minimo = stats.poisson.ppf(p, media)

print(f"O numero minimo e de {n_minimo:.0f}")

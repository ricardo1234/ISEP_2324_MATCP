from scipy import stats

n = 5
media = 5.5
#33.1
p5 = stats.poisson.cdf(n, media)
print(f"A probabilidade de x > 5 : {(1-p5):.4f}")

#33.2
n = 10
p10 = stats.poisson.cdf(n, media)
print(f"A probabilidade de x > 10 : {(1-p10):.4f}")

#33.3
p = 0.94
n_minimo = stats.poisson.ppf(p, media)
print(f"Stock minimo : {n_minimo}")

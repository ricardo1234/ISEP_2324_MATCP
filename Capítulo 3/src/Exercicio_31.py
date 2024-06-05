from scipy import stats

n = 0
media = 1.5

p0 = stats.poisson.pmf(n, media)
print(f"A probabilidade de x = 0 : {(p0*100):.1f}%")

n=1
p1 = stats.poisson.pmf(n, media)
print(f"A probabilidade de x = 1 : {p1}")

n=2
p2 = stats.poisson.pmf(n, media)
print(f"A probabilidade de x = 2 : {p2}")

#cat 2
print(f"A probabilidade de x = 1 e X = 2 : {p1+p2:.3f}")

pGreater2 = stats.poisson.cdf(n, media)
print(f"A probabilidade de x > 2 : {1-pGreater2}")

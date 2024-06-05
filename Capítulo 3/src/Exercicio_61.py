from scipy import stats
# 61.1
p = 0.975
media = 0
dp = 1

r = stats.norm.ppf(p,media,dp)
print(f"Resultado {r:.3f}")

# 61.2
p0 = stats.binom.cdf(0,6, 0.025)
print(f"A probabilidade de x = 0 : {p0:.3f}")

from scipy import stats

beta=2500

# 51.1
x = 3000
p3000 = stats.gamma.cdf(x, a=1, scale=beta)
print(f"A probabilidade de x < 3000 : {p3000:.3f}")
print(f"A probabilidade de x > 3000 : {(1-p3000):.3f}")

# 51.2
p=0.2
x = stats.gamma.ppf(p, a=1, scale=beta)
print(f"Duração: {x:.3f}")

#51.3
n = 12
p = 1-p3000
x=6
print(f"A probabilidade de x <= 6 : {stats.binom.cdf(x, n, p):.6f}")
print(f"A probabilidade de x > 6 : {1 - stats.binom.cdf(x, n, p):.6f}")
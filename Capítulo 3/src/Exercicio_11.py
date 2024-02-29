from scipy import stats

n = 4
p = 0.99
x = 1

print(f"A probabilidade de x <= 1 : {stats.binom.cdf(x, n, p):.6f}")
print(f"A probabilidade de x > 1 : {1 - stats.binom.cdf(x, n, p):.6f}")
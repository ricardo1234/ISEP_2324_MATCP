from scipy import stats

beta=21.7

# 52.2
x = 30
p30 = stats.expon.cdf(x, loc=0, scale=beta)
print(f"A probabilidade de x <= 30 : {p30:.3f}")
print(f"A probabilidade de x > 30 : {(1-p30):.3f}")

# 52.2
x = 10
p10 = stats.expon.cdf(x, loc=0, scale=beta)
print(f"A probabilidade de x <= 10 : {p10:.3f}")

x = 100
p100 = stats.expon.cdf(x, loc=0, scale=beta)
print(f"A probabilidade de x <= 100 : {p100:.3f}")
print(f"A probabilidade de x > 100 : {(1-p100):.3f}")
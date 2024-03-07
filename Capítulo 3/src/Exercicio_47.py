from scipy import stats

inicio = 20
fim = 80

# 47.1
x = 30
p30 = stats.uniform.cdf(x, inicio, fim)
print(f"A probabilidade de x < 30 : {p30:.3f}")

x = 70
p70 = stats.uniform.cdf(x, inicio, fim)
print(f"A probabilidade de x < 70 : {p70:.3f}")

print(f"A probabilidade de 30 < x < 70 : {p70-p30}")

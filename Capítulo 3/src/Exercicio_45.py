from scipy import stats

inicio = 18.5
fim = 21.5
x = 21

# 45.1
p21 = stats.uniform.cdf(x, inicio, fim)
print(f"A probabilidade de x < 21 : {p21:.3f}")
print(f"A probabilidade de x > 21 : {(1 - p21):.3f}")

# 45.2
x = 0.866
pi = stats.uniform.cdf(x, inicio, fim)
print(f"A probabilidade de x <  : {pi}")
print(f"A probabilidade de x >  : {(1 - pi)}")

# 45.3
x2 = 20.6
p206 = stats.uniform.cdf(x2, inicio, fim)
print(f"A probabilidade de x < 20.6 : {p206}")
x3 = 19.4
p194 = stats.uniform.cdf(x3, inicio, fim)
print(f"A probabilidade de x < 19.4 : {p194}")

print(f"A probabilidade de 19.4 < x < 20.6 : {p206-p194}")

n=8
x4=4
p=0.0558
p4 = stats.binom.cdf(x4, n,p)
print(f"A probabilidade de x < 4 : {p4:.3f}")
print(f"A probabilidade de x > 4 : {(1 - p4):.3f}")


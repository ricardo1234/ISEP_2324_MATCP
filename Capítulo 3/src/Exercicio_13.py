from scipy import stats
n = 6
p = 0.04
x = 0
print(f"A probabilidade de x = 0 : {(stats.binom.pmf(x, n, p)*100):.1f}%")
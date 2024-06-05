from scipy import stats
# 61.1
n = 2000
media = 1900
dp = 40.3

r = stats.norm.cdf(n,media,dp)
print(f"Resultado {r:.4f}")

# 61.2
n = 0
media = -20
dp = 18

r = stats.norm.cdf(n,media,dp)
print(f"Resultado {(1-r):.4f}")
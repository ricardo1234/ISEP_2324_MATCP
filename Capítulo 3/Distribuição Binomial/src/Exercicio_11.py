from BinomialExtension import BinomialExtension

myStats = BinomialExtension(n = 4, p=0.99)

print(f"A probabilidade de x > 1 : {myStats.Greater(x=1):.6f}")
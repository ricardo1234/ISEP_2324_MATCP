from BinomialExtension import BinomialExtension

myStats = BinomialExtension(n = 6, p=0.04)

print(f"A probabilidade de x = 0 : {myStats.Equal(x=0, toPercentage=True):.1f}%")
from BinomialExtension import BinomialExtension

myStats = BinomialExtension(n = 5, p=0.2)

#15.1
print(f"A probabilidade de x >= 1 : {myStats.GreaterOrEqual(1):.5f}")
print(f"A probabilidade de x = 5 : {myStats.Equal(5):.5f}")
print(f"A probabilidade : {(myStats.Equal(5)/myStats.GreaterOrEqual(1)):.5f}")

#15.2
print(f"A probabilidade de x >= 3 : {myStats.GreaterOrEqual(3):.5f}")
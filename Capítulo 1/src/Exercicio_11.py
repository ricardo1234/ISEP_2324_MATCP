import random
def caraCroa():
    if random.random() < 0.5:
        return "Cara"
    return "Coroa"

def testGame(n):
    coroas = 0
    for i in range(n):
        if caraCroa() == "Coroa":
            coroas += 1

    print(f"O numero de caras foi {coroas} que corresponde a {(coroas/n*100):.2f}%")

testGame(10)
testGame(100)
testGame(1000)
testGame(10000)
testGame(100000)
from scipy import stats

class BinomialExtension:

    def __init__(self, n, p):
        self.n = n
        self.p = p

    def Equal(self, x, toPercentage=False):
        return stats.binom.pmf(x, self.n, self.p)*(100 if toPercentage else 1)
    def LessOrEqual(self, x, toPercentage=False):
        return stats.binom.cdf(x, self.n, self.p)*(100 if toPercentage else 1)
    def Less(self, x, passe = 1, toPercentage=False):
        return stats.binom.cdf(x-passe, self.n, self.p)*(100 if toPercentage else 1)
    def Greater(self, x, toPercentage=False):
        return 1 - stats.binom.cdf(x, self.n, self.p)*(100 if toPercentage else 1)
    def GreaterOrEqual(self, x, passe = 1, toPercentage=False):
        return 1 - stats.binom.cdf(x-passe, self.n, self.p)*(100 if toPercentage else 1)
    def GreaterAndLessOrEqual(self, a, b, toPercentage=False):
        return stats.binom.cdf(b, self.n, self.p) - stats.binom.cdf(a, self.n, self.p)*(100 if toPercentage else 1)
    def GreaterOrEqualAndLessOrEqual(self, a, b, passe = 1, toPercentage=False):
        return stats.binom.cdf(b, self.n, self.p) - stats.binom.cdf(a-passe, self.n, self.p)*(100 if toPercentage else 1)
    def GreaterOrEqualAndLess(self, a, b, passe = 1, toPercentage=False):
        return stats.binom.cdf(b-passe, self.n, self.p) - stats.binom.cdf(a, self.n, self.p)*(100 if toPercentage else 1)
    def GreaterAndLess(self, a, b, passe = 1, toPercentage=False):
        return stats.binom.cdf(b-passe, self.n, self.p) - stats.binom.cdf(a-passe, self.n, self.p)*(100 if toPercentage else 1)
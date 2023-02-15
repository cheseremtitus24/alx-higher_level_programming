class fraction(object):
    def __init__(self, n, d):
        self.numerator, self.denominator = fraction.reduce(n, d)

    @staticmethod
    def gcd(a, b):
        """ Greatest common divisor
        >>> obj = fraction(8,12)
        >>> obj.gcd(8, 24)
        8
        """
        while b != 0:
            a, b = b, a%b
        return a
    @classmethod
    def reduce(cls, n1, n2):
        g = cls.gcd(n1, n2)

        return (n1 // g, n2 // g)
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)


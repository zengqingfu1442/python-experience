class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        a = self.p
        b = self.q
        if b > a:
            a, b = b, a
        while b != 0:
            r = a % b
            a = b
            b = r
        self.p = self.p // a
        self.q = self.q // a

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q *r.q)

    def __truediv__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        return '{0}/{1}'.format(self.p, self.q)

    __repr__ = __str__


def cgd(p, q):
    A = p
    B = q
    if q > p:
        p, q = q, p
    if 0 == p or 0 == q:
        print("P and Q must be positive integer")
    while q != 0:
        r = p % q
        p = q
        q = r
    print("The greatest common divider of {0} and {1} is {2}".format(A, B, p))


if __name__ == '__main__':
    r1 = Rational(1, 2)
    r2 = Rational(1, 4)
    print(r1 + r2)
    print(r1 - r2)
    print(r1 * r2)
    print(r1 / r2)
    cgd(8, 12)

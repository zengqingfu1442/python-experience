class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return self.p / self.q


if __name__ == '__main__':
    print(float(Rational(7, 2)))
    print(float(Rational(1, 3)))
# 生成器既是可迭代的对象, 又是迭代器对象
class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @staticmethod
    def is_prime_num(k):
        if k < 2:
            return False
        for i in range(2, k//2):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.is_prime_num(k):
                yield k


if __name__ == '__main__':
    for x in PrimeNumbers(1, 20):
        print(x)

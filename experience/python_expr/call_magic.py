class Fib(object):
    def __call__(self, num):
        lst = [0, 1]
        for i in range(2, num):
            lst.append(lst[i-2] + lst[i-1])
        print(lst)


if __name__ == '__main__':
    f = Fib()
    print(f(10))
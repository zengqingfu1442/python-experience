class Fib(object):
    def __init__(self, num):
        self.lst = [0, 1]
        for i in range(2, num):
            self.lst.append(self.lst[i-2] + self.lst[i-1])

    # def __call__(self, *args, **kwargs):
    #     return self.lst

    def __len__(self):
        return len(self.lst)

    def __str__(self):
        # print(self.lst)
        return str(self.lst)


if __name__ == '__main__':
    f = Fib(10)
    print(f)
    print(len(f))
#!/usr/bin/env python
# -*-coding；utf-8-*-


class Squares(object):
    def __init__(self, start, stop):
        # save state when created
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        # generate iterator object on iter
        return self

    def __next__(self):
        # return a square on each iteration
        if self.value == self.stop:
            # also called by next built-in
            raise StopIteration
        self.value += 1
        return self.value ** 2


class Fibs(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


if __name__ == '__main__':
    squa1 = Squares(1, 5)
    print(type(squa1), '\n', dir(squa1))
    print(squa1.value)
    print(squa1.stop)
    for i in squa1:  # for calls iter, which calls __iter__
        print("when i=", i, "squa1.value=", squa1.value, "squa1.stop=", squa1.stop)
        print(i, end='  \n')  # each iteration calls __next__

    # return the n-th fibnaci number
    fib = Fibs()
    n_fib = 17
    for f in fib:
        n_fib -= 1
        # if f >= 100:
        if n_fib == 0:
            print(f)
            break

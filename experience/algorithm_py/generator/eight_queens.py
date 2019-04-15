#!/usr/bin/env python
# -*-coding:utf-8-*-


def conflict(state, next_x):
    next_y = len(state)
    for i in range(next_y):
        if abs(state[i] - next_x) in (0, next_y - i):
            return True
    return False


def queens(default_num=8, state=()):
    for pos in range(default_num):
        if not conflict(state, pos):
            if len(state) == default_num - 1:
                yield (pos,)
            else:
                for result in queens(default_num, state + (pos,)):
                    yield (pos,) + result


def pretty_print(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X' + ' .' * (length - pos - 1)
    for pos in solution:
        print(line(pos))


if __name__ == "__main__":
    # print(list(queens(4)))
    for solution in queens(4):
        print(solution) # it shows that which cell the queen of each line should be put in(the first cell number is 0)

    import random
    pretty_print(random.choice(list(queens(4))))
    i = 1
    num = 10
    solution = queens(num)
    for table in list(solution):
        print("the %d-th solution" % i)
        pretty_print(table)
        i += 1
        print('-------------------------\n')


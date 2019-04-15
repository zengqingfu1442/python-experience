#!/usr/bin/env python

import random


def pinggu_theory(N):
    if N == 1:
        return 1
    elif N % 2 == 1:
        N = 3 * N + 1
    elif N % 2 == 0:
        N /= 2
    return pinggu_theory(N)


if __name__ == '__main__':
    # N = 99
    N = random.randint(1, 1000000000)
    print('N is: %d' % N)
    print(pinggu_theory(N))
#!/usr/bin/env python

def char_count(S, J):
    rslt = 0
    S = list(set(S))
    for c in S:
        rslt += J.count(c)
    return rslt


if __name__ == '__main__':
    S = 'aAAC'
    J = 'AAaaCcmnjk'
    print("The characters show up in %s also show up %s times in %s" % (S, char_count(S, J), J))
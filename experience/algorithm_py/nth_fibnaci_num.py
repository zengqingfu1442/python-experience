#!/usr/bin/env python


def fibnaci_nth(n):
    """
    fibnaci list: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233
    >>> fibnaci_nth(8)
    >>> 13
    :param n:
    :return:
    """
    lst = [0, 1]
    a, b = 0, 1
    for i in range(0, n):
        b, a = a + b, b
        lst.append(b)
        rslt = lst.pop(0)
    print(lst)
    #lst.pop(0)
    #print(lst)
    #return lst[n-1]
    return rslt


if __name__ == '__main__':
    print(fibnaci_nth(14))

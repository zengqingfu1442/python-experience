#!/usr/bin/env python
# -*-coding:utf-8-*-
# 循环生成器


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


if __name__ == '__main__':
    lst = [[1, 2], [3, 4], [5], [0, 4, 10], [7, 9, 8]]
    for num in flatten(lst):
        print(num)

    # 列表推导式
    print("*************list expression***************")
    g = (i**2 for i in range(2,10))
    print(g.__next__())
    print(g.__next__())

    # 生成器推导式
    print("************generator expression**********")
    print(sum(i**2 for i in range(2, 10)))

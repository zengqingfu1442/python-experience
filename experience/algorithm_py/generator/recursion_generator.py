#!/usr/bin/env python
# -*-coding:utf-8-*-
# 递归生成器


# 适用于处理任意层嵌套以及字符串的情况
def flatten_recursion(nested):
    try:
        # don't iter object like string
        try:
            nested + 'a'
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            print(type(sublist), sublist)
            for element in flatten_recursion(sublist):
                print(type(element), element)
                yield element
    except TypeError:
        yield nested


if __name__ == '__main__':
    lst = [[1, 2], [3, 4], [5], [0, 4, 10], 7, 9, 8, [2, [3,6]], 'aaa', (1,2)]
    # lst = ['foo', ['aaa', 'c', 'nnn']]
    for num in flatten_recursion(lst):
        # print(type(flatten_recursion(lst)), dir(flatten_recursion(lst)))
        print(num)

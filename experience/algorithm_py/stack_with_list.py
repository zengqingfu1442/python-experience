#!/usr/bin/env python

import copy


def is_stack_empty(stack):
    return True if len(stack) == 0 else False


def push(stack, x):
    stack_ret = copy.copy(stack)
    stack_ret.append(x)
    return stack_ret


def pop(stack):
    stack_ret = copy.copy(stack)
    stack_ret.pop(-1)
    return stack_ret


if __name__ == '__main__':
    x = 55
    lst = [3, 7, 8, 9, 90, 1, 34]
    print('Stack lst is empty? %s' % is_stack_empty(lst))
    lst_pushed = push(lst, x)
    print('After pushing %s into %s, it turns to %s' % (x, lst, lst_pushed))
    lst_pop = pop(lst)
    print('After poping out the top item of %s, it turns into %s' % (lst, lst_pop))

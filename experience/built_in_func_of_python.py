#!/usr/bin/env python
# -*-coding；utf-8-*-


a = -20
print(abs(a))

s = "Python语言"
print('未转之前：', type(s))

s_after_transformed = bytes(s, encoding='utf-8')
print("字符串转化之后：", s_after_transformed)
print(type(s_after_transformed))

s_2 = str(s_after_transformed, encoding='utf-8')
print('bytes转化为字符串之后：', s_2)


print(chr(98))
print(chr(48))

print(ord('c'))
print(ord('a'))
print(ord('b'))


def suiji_yanzhengma():
    import random
    li = []
    for i in range(6):
        r = random.randrange(48 + i, 100)
        li.append(chr(r))
    print(''.join(li))


suiji_yanzhengma()

expr = '5*7%4'
print(eval(expr))

print_sentence = "print(eval(expr))"
print_code = compile(print_sentence, '<string>', 'exec')
print(type(print_code))
exec(print_code)
exec('print(123)')


print(dir(print_code))

# help(list)
# help(str)

print(divmod(97, 3))
print(divmod(3*7, 4))

print(isinstance(print_code, object))


lst = [1, 22, 3, 5, 77, 98, 10, 13, 14]


def f1():
    li = []
    lst_2 = [i for i in lst if i >= 22]
    print(lst_2)
    # for i in lst:
    #     if i >= 22:
    #         li.append(i)
    # print(li)
f1()


# use filter function
def f2(a):
    if a >= 22:
        return True


res = filter(f2, lst)
print(type(res))
print(list(res))


# map function
print(lst)


def f3(a):
    return a + 10


result = map(f3, lst)
print(list(result))


print("$$$$$$$$$$$##################")
print("all global vars: ", globals())
print("all local vars:  ", locals())


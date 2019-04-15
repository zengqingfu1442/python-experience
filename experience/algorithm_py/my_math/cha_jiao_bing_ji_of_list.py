# -*-coding:utf-8-*-


a = [1, 2, 3]
b = [2, 3, 4]

# 差集
# a - b
ret = []
for i in a:
    if i not in b:
        ret.append(i)
print(ret)

ret = [ i for i in a if i not in b]
print(ret)

# a + b - (a&b)
ret = list(set(a)^set(b))
print(ret)

# 并集 b + a
ret = list(set(a).union(set(b)))
print(ret)

# b - a
ret = list(set(b).difference(set(a)))
print(ret)
# a - b
ret = list(set(a).difference(set(b)))
print(ret)

# a + b
ret = list(set(a)|set(b))
print(ret)

# a & b    a ^ b in math
ret = list(set(a)&set(b))
print(ret)



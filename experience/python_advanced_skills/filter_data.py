from random import randint


data = [randint(-10, 10) for _ in range(10)]

# 1. use filter function
dt = filter(lambda x: x >= 0, data)
print(list(dt))


# 2.list expression
dt = [x for x in data if x >= 0]
print(dt)

# In[1]: %timeit list(filter(lambda x: x >= 0, data))
# 1.01 µs ± 16.5 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
# In[2]: %timeit [x for x in data if x >= 0]
# 355 ns ± 12.2 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)


# dictionary parser
d = {x: randint(60, 100) for x in range(1,21)}
print(d)
d = {k: v for k, v in d.items() if v > 90}
print(d)

s = set(data)
s2 = {x for x in s if x % 3 == 0}
print(s2)
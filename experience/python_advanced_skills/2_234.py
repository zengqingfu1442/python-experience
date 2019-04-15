from collections import namedtuple

# ('Jim', 26, 'male', 'jim721@gmial.com')
# ('LiLei', 23, 'male', 'lilei@qq.com')
# ('Lucy', 21, 'female', 'lucy@163.com')

student = namedtuple('student', ['name', 'age', 'sex', 'email'])


s = student('Jim', 26, 'male', 'jim721@gmial.com')
print(s)

s2 = student(name='Jim', age=26, sex='male', email='jim721@gmail.com')
print(s2)

print(s.name)
print(isinstance(s, tuple))
'----------------------------------'

from random import randint
from collections import Counter


data = [randint(0, 10) for _ in range(11)]
print(data)
c = dict.fromkeys(data, 0)
print(c)
for x in data:
    c[x] += 1

print(c)
c2 = Counter(data)
print(c2)
print(c2.most_common(3))
print('--------the order of c------')
for k,v in c.items():
    print(k, v)
print('------the order of c2--------')
for k,v in c2.items():
    print(k, v)

'------------------------------------'


import re
txt = open('coding-style.rst.txt', 'r').read()
print(txt)
c3 = Counter(re.split('\W+', txt))
print(c3)
print(c3.most_common(10))

d2 = {x:randint(60, 100) for x in 'xyzabc'}
print(d2)
print(sorted(d2.items(), key=lambda x:x[1]))
print(reversed(sorted(d2.items(), key=lambda x:x[1])))




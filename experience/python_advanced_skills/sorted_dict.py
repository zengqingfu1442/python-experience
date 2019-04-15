from collections import OrderedDict # 按照进入字典的顺序排序
from time import time
from random import randint


d = OrderedDict()
#
# d['Jim'] = (2, 32)
# d['David'] = (1, 12)
# d['Will'] = (3, 40)
#
# print(d)
# for i in d:
#     print(i)

players = list('ABCDEFGH')
start = time()

for i in range(len(players)):
    input() # 按回车相当于回答完成提交的操作, 回答问题用时越短成绩排名越靠前
    p = players.pop(randint(0, 7-i))
    end = time()
    print(i+1, p, end - start)
    d[p] = (i+1, end - start)


# 公布成绩
print('-' * 20)
for k in d:
    print(k, d[k])

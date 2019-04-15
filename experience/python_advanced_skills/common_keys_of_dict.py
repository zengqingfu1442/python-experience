from random import randint, sample

players = "abcdefgh"

# 第一,二轮进球的球员名单
turn1 = sample(players, 4)
turn2 = sample(players, randint(3, 6))
turn3 = sample(players, randint(4, 6))
print(turn1)
print(turn2)

# 第一,二轮球员进球个数
score1 = {x:randint(1, 4) for x in turn1}
score2 = {x:randint(1, 4) for x in turn2}
score3 = {x:randint(1, 4) for x in turn3}

print(score1)
print(score2)
res = []
for k in score1:
    if k in score2:
        res.append(k)
print(res)

'---------------------------------'
print(score1.keys())
print(score2.keys())
print(score3.keys())
print(score1.keys() & score2.keys() & score3.keys())  # 集合set的交集操作


# 求第一二三轮中都进球的球员名单

from functools import reduce # 注意Python3中reduce函数需要导入才能使用,Python2中可以直接使用

print(map(dict.keys, [score1, score2, score3]))
for i in map(dict.keys, [score1, score2, score3]):
    print(i)
print(reduce(lambda a, b: a & b, map(dict.keys, [score1, score2, score3])))



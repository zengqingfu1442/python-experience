from collections import deque
import pickle

q = deque([], 5)
q.append(1)

q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q)

q.append(6)
print(q)


pickle.dump(q, open('history.txt', 'wb'))  # 注意Python3中必须用'wb', python2中为'w'
q2=pickle.load(open('history.txt', 'rb'))  # 主义必须Python3中必须用'rb', python2中为'r'





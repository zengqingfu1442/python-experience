#!/usr/bin/env python
#-*-coding:utf-8-*-

import threading
import time
import dummy_threading


# seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for idx in range(len(seq)):
#     item = seq[idx]
#     print(idx, "=>", item)
#
# for idx, item in enumerate(seq):
#     print("more Pythonic")
#     print(idx, "=>>", item)


def show(arg):
    time.sleep(1)
    print('thread'+str(arg))


for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()

print('main thread stop')
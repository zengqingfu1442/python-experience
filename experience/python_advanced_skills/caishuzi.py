from random import randint
from collections import deque


N = randint(0, 100)
history = deque([], 5)

def guess(k):
    if k == N:
        print('right')
        return True
    elif k< N:
        print('{0} is less than N'.format(k))
    else:
        print('{0} is greater than N'.format(k))
    return False


if __name__ == '__main__':
    while True:
        k = input('Please input a number and then press Enter(type h to see the latest 5 numbers you input): ')
        if k.isdigit():
            k = int(k)
            history.append(k)
            if guess(k):
                break
        elif k == 'history' or k == 'h':
            print("the latest 5 numbers you input are: {0}".format(history))

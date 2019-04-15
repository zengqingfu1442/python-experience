#!/usr/bin/env python


def split2aji_fenshu(a, b):
    print("%d/%d can be split into: " % (a, b))
    while True:
        if b % a != 0:
            c = b // a + 1
        else:
            c = b / a
            a = 1
        if 1 == a:
            print("1/%d\n" % c)
            break
        else:
            print("1/%d + " % c, end='')

        a = a * c - b
        b = b * c
        if a == 3 and b % 2 == 0:
            print("1/%ld + 1/%ld\n" % (b/2, b))
            break


if __name__ == '__main__':
    while True:
        s = input('Please input a real faction number(a/b), press 0 to exit: ')
        if s is not '0':
            a = int(s.split('/')[0])
            b = int(s.split('/')[1])
            print("the input is %d/%d" % (a, b))
            split2aji_fenshu(a, b)
        else:
            print("Finished! Exited Successfully!")
            break

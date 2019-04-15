#!/usr/bin/env python

# import palindrome
from palindrome import is_palindrome


if __name__ == '__main__':
    pat = 'abba'
    pat = 'iperfrepi2'
    if is_palindrome(pat):
        print('%s is a palindrome' % pat)
    else:
        print('%s is NOT a palindrome' % pat)
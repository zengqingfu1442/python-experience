#!/usr/bin/env python

def is_palindrome(text):
    n = len(text)
    for i in range(n//2):
        if text[i] != text[n-i-1]:
            return False
    return True

if __name__ == '__main__':
    txt = 'acbbcaafaf'
    print(is_palindrome(txt))
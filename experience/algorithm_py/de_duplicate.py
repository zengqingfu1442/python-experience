#!/usr/bin/env python


def de_duplicate(seq):
    if type(seq) is str:
        dedup_str = ''
        for char in seq:
            if not char in dedup_str:
                dedup_str += char
        return dedup_str
    elif type(seq) is list:
        dedup_list = []
        for word in seq:
            if not word in dedup_list:
                dedup_list.append(word)
        return dedup_list


if __name__ == '__main__':
    lst = [1, 1, 2, 4, 3, 2, 'me', '1', '2']
    string = 'jfsjfsfjsfj11123ojmimeIloveyouwangjunlu'
    print("After de-duplication, %s turns to %s" % (lst, de_duplicate(lst)))
    print("After de-duplication, %s turns to %s" % (string, de_duplicate(string)))
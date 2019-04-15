#!/usr/bin/env python
# -*-coding:utf-8-*-

import re
import operator


def single_word_count(fl_name, kw):
    kw_count = 0
    with open(fl_name, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            if line.count(kw):
                for word in line.split(): # Assume that all words are split by empty space
                    if word == kw:
                        print(line)
                        print(word)
                        kw_count += 1
    return kw_count


def all_word_count(fl_name, kw_list, sep_pat):
    kw_count = {}
    with open(fl_name, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            # for word in line.split(): # Assume that all words are split by empty space
            after_split_line = re.split(sep_pat, line)
            word = after_split_line[2].split('(')[0]
            if word in kw_list:
                try:
                    kw_count[word] += 1
                except KeyError:
                    kw_count[word] = 1
    return kw_count


def get_all_words_in_text(fl_name, sep_pat):
    kw_list = []
    # seps = [' ', '=', '(', ')', '{', '}', '[', ']']
    # sep = ' '
    with open(fl_name) as f:
        lines = f.read().splitlines()
        for line in lines:
            # for word in line.rsplit(sep):
            after_split_line = re.split(sep_pat, line)
            word = after_split_line[2].split('(')[0]
            if word not in kw_list:
                kw_list.append(word)
    return kw_list


def _sort_seed(wc_dict):
    pass


def _filter_seed():
    pass


if __name__ == '__main__':
    fl = 'output.txt'
    # sep_pat = ' |,|=|(|)|{|}|[|]'
    # sep_pat = ' |='
    sep_pat = '[ ]+'

    all_words_in_text = get_all_words_in_text(fl, sep_pat)
    # remove the empty elements in a list
    all_words_in_text = list(filter(None, all_words_in_text))
    # remove those elements which are not function name
    for i in all_words_in_text:
        if i.count('+') or i.count('<') or i.count('[-]+'):
            print(i)
            all_words_in_text.remove(i)
    all_words_in_text.remove('---')
    print(all_words_in_text)
    print(len(all_words_in_text))
    # print(all_word_count(fl, 'close'))

    word_count_dict = all_word_count(fl, all_words_in_text, sep_pat)
    # print(word_count_dict['access'])
    # sort a dictionary by its values
    word_count_dict = sorted(word_count_dict.items(), key=operator.itemgetter(1), reverse=True)
    print(word_count_dict)
    for pair in word_count_dict:
        print(pair[0], "==>", pair[1])
    print(len(word_count_dict))


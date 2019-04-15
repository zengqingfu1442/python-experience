def format_name(s):
    # ss = []
    # for i in s:
    #     # yield i.capitalize()
    #     ss.append(i.capitalize())
    return s.capitalize()  # 只有在Python2才是对的


if __name__ == '__main__':
    test_s = ['adam', 'LISA', 'barT']
    # print(format_name(test_s))
    test_ss = map(format_name, test_s)
    print(test_ss)
    # dir(test_ss)
    for i in map(format_name, test_s):
        print(i)
    print(test_ss)
    # try:
    #     print(test_ss.__next__())
    # except StopIteration:
    #     pass

    for i in format_name(test_s):
        print(i)

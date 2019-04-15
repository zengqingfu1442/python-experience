# -*-coding:utf-8-*-
list_num = []
list_num_count = 0
dict_num = {}
# 从文件读入,文件第一行为集合中元素的个数,以后每一行为一个元素
list_num_count = int(open('input.txt', 'r').readline())
for line_num, line in enumerate(open("input.txt", 'r')):
    if line_num > 0:
        list_num += line.split()
# 将读到的元素加入的字典中
for item in list_num:
    if item in dict_num.keys():
        dict_num[item] += 1
    else:
        dict_num.setdefault(item, 1)
    pass

# 找到出现次数最多的那个数,找到重数
dict_sort_by_top = {}
top_value = 0
for valus in dict_num.values():
    if valus > top_value:
        top_value = valus
    pass

# 根据重数找到众数...这是因为考虑到可能有多个元素有相同多的重数
the_pop_num = 0
the_pop_num_count = 0
for keys, values in dict_num.items():
    if values == top_value:
        print('the pop num is %s,and the appear num is %s' % (keys, values))
        the_pop_num = keys
        the_pop_num_count = values
# 输出到文件,第一行为从数,第二行为重数
write_line = '%s\n%s' % (the_pop_num, the_pop_num_count)
open("output.txt", 'w').write(write_line)
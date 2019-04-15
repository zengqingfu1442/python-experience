# $swig -python palindrome.i

# $gcc -fPIC -c palindrome.c
# $gcc -fPIC -I/home/zengxiaofuqi/anaconda3 -I/home/zengxiaofuqi/anaconda3/include/python3.7m -c palindrome_wrap.c
# $gcc -shared palindrome.o palindrome_wrap.o -o _palindrome.so
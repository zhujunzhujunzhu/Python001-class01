'''
@Description 
@Autor 朱俊
@Date 2020-07-11 19:13:55
@LastEditors 朱俊
@LastEditTime 2020-07-11 19:35:04
'''
import sys
import argparse

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv)


num_index = sys.argv.index('-n')
print(sys.argv[num_index+1])

# 上面的是成功的 可以封装成一个方法的
arg_flags = ['-n', '-f', '-p']
dict = {}


def find_arg():
    for flag in arg_flags:
        if flag in sys.argv:
            num_index = sys.argv.index(flag)
            flag_value = sys.argv[num_index+1]
            dict[flag] = flag_value


find_arg()
print(dict)

# 关于python中的列表还有哪些方法呢？


'''
python .\scriptargs.py -nama = test

.\scriptargs.py
-nama
['.\\scriptargs.py', '-nama', '=', 'test']
这里先使用 sys.argv 这个还是比较简单的
因为在可以放到列表中  可以要做的事情是 在列表中找到 比如 -n  那么它后面的就是 -n 对就的参数的
list.findIndex('')  arg = list[index+1]
'''

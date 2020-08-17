
import time
'''
作业一：

区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：

list
tuple
str
dict
collections.deque

容器序列：可以存放不同类型的数据  list tuple dict collections.deque 
扁平序列：只能容纳一种数据类型 其存放的是值而不是引用 是一段连续的内存空间 str

可变序列： list dict collections.deque
不可变序列：tuple str

'''


'''
作业二：
自定义一个 python 函数，实现 map() 函数的功能。
'''
li = [1, 2, 3, 4]
new_li = map(lambda x: x+1, li)
print(list(new_li))


li = [1, 2, 3, 4, 5]


def my_map(fn, li):
    for it in li:
        yield fn(it)


new_li1 = map(lambda x: x+1, li)
print(next(new_li1))
print(new_li1.__next__())
print(list(new_li1))


'''
作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
'''


def timer(fn):
    def wrapper(*args, **kargs):
        start_time = time.time()
        fn(*args, **kargs)
        end_time = time.time()
        print(f'共用时{end_time-start_time}')
    return wrapper


@timer
def test(*args, **kargs):
    print(f'{args}')
    print(f'{kargs}')


if __name__ == '__main__':
    test(1, 2, 3, 4, '你好', name="zhujun", age=25)

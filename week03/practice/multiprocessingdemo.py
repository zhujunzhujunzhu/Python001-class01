'''
@Description 
@Autor 朱俊
@Date 2020-07-06 15:01:24
@LastEditors 朱俊
@LastEditTime 2020-07-06 16:47:17
'''
# import os
# import threading
# import multiprocessing


# '''
# os模块是与操作系统相关的模块 os.getpid 这个是获取进程的id

# 通过threading这个模块的 threading.Thread 来开启一个线程

# 会看到的是创建子进程的时候　会进次执行的这个py文件的
# '''
# # Main
# print('Main:', os.getpid())

# # worker function


# def worker(sign, lock):
#     lock.acquire()
#     print(sign, os.getpid())
#     lock.release()


# # Multi-thread
# record = []
# lock = threading.Lock()

# # Multi-process
# record = []
# lock = multiprocessing.Lock()

# if __name__ == '__main__':
#     # for i in range(5):
#     #     # 创建进程
#     #     '''
#     #       可以看到threading.Thread的基本的规则  target 是一个函数  args是一个元组
#     #       '''
#     #     thread = threading.Thread(target=worker, args=('thread', lock))
#     #     # 启动进程
#     #     thread.start()
#     #     #  将进程添加到记录中去
#     #     record.append(thread)

#     # for thread in record:
#     #     thread.join()

#     for i in range(5):
#         '''
#          这里看到了我们的multiprocessing.Process 参数与threading.Thread是完全一样的
#          开启一个进程的时间这个py文件会再次执行的   这个需要说明的是  这个main 不是主进程也进入了吗
#          如果不是主进程进入了main的话肯定会有问题的  那就是永远停不下来的
#          当为子进程的时候   为__mp_main__

#          因此可以发现的是 使用__name__ == '__main__'
#          一个方面 当是通过 import的方式被引入的话  里面的可以不被执行 另一个方面  当为子进程的时候也不会被执行的
#         '''
#         process = multiprocessing.Process(
#             target=worker, args=('process', lock))
#         process.start()
# record.append(process)

# for process in record:
#     process.join()


# 来一个自己的示例
import os
from multiprocessing import Process
import time


def subProcess(name):
    print(f'子进程 {name} 的pid为{os.getpid()}')
    for i in range(10):
        # 从打印的结果上来看的话  time.sleep 让打印的次数变少了的   这个可能是因为子进程会处动关闭？
        # 事实的情况证明是这样的  因为执行完成了这个文件后 它就会自动关闭的  当关闭了这个文件  所有的 延时的操作的话
        # 就不会被执行了的 是主进程执行完成了  子进程就会被销毁的 才导致了这个问题的

        # 这个也就引发了一个重要的问题的
        '''
          python主进程或者主线程是否会等待子线程或子进程的问题
          看到上面的一个方法 process.join()  加入到 进程队列中  这样主进程才会等待的
          但是添加了join() 之后 似乎又有可能引发新的非异步的现象的

          这里还看到了使用一种方式  叫作守护进程   p.daemon 
          设置守护进程需要明确的是这个进程已经不存在了才可能进行设置的？？


          靠谱些的方式还是将进程记录下来  然后在所有的子进程开启后  再一一join到进程列表中去
        '''
        time.sleep(1)
        print(f'子进程 {name} pid 打印值 为{i}')


if __name__ == "__main__":
    # 开启父进程
    print(f'父进程的pid为{os.getpid()}')
    # 开启一个子进程
    # 这里很神奇的是  args=("subq1") 这个是有问题的  但是后面添加上一个, 就是可以的

    '''
  tup1 = (50) 
  type(tup1)     # 不加逗号，类型为整型
   <class 'int'>
 
   tup1 = (50,)
   type(tup1)     # 加上逗号，类型为元组
   <class 'tuple'>
   这个还是很有意思的  
    '''
    p = Process(target=subProcess, args=("sub1",))
    p.start()  # 启动进程
    p1 = Process(target=subProcess, args=("sub2",))
    p1.start()  # 启动进程

    p1.join()
    p.join()
    # time.sleep(40)

# 基本的使用方法现在是有了感觉的  但是怎么来使用它呢  多个线程并行的去干事情的

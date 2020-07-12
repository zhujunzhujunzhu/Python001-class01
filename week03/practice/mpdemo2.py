'''
@Description
@Autor 朱俊
@Date 2020-07-11 09:06:31
@LastEditors 朱俊
@LastEditTime 2020-07-12 10:40:06
'''

from multiprocessing import Process, Queue, Lock
import time


# 直接采用target 这种方式
# def run(name, q, dict):
#     print(f"{name}开始")
#     time.sleep(2)
#     print(f"{name}结束")
#     q.put({"name": name})
#     dict[name] = name


# def run1(name, lock):
#   # 这里我看到了这样的使用是没有任何的效果的  终端还是乱的
#     lock.acquire()
#     time.sleep(1)
#     print(f'{name}\n')
#     lock.release()


# if __name__ == "__main__":
# q = Queue()
# dict = {}
# p1 = Process(target=run, args=("进程1", q, dict))
# p2 = Process(target=run, args=("进程2", q, dict))
# p1.start()
# p2.start()
# print(q.qsize())
# print(q.get())
# print(q.get())
# print(q.empty())

# print(dict)

# p1.join()
# p2.join()
# print("主进程结束")

# for index in range(10):
#     lock = Lock()
#     p = Process(target=run1, args=(f'进程{index}', lock))
#     p.start()

# 比如在进行购票这个场景下的人  这里我可以并发20 个进程去模拟抢票


# class MyProcess(Process):
#     def __init__(self, msg, q):
#         super(MyProcess, self).__init__()
#         self.msg = msg
#         self.q = q

#     def run(self, name):
#         # print(f"{self.name}开始")
#         # time.sleep(2)
#         # print(f"{selfname}结束")
#         print(self.msg)
#         self.q.put(self.msg)


# if __name__ == "__main__":
#     queue = Queue()
#     p1 = MyProcess('进程1', queue)
#     p2 = MyProcess('进程2', queue)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print(queue)
#     print(queue.get())
#     print("主进程结束")

# 这里需要知道队列的最为基本的使用的  利用队列来进行进程间的通信  利用普通的字典可以吗  事实证明是不可以的
#
# 这里还有更为复杂的锁机制的

from multiprocessing import Process, Lock, Pool
import os
import time


def work(lock, index):
    # lock.acquire()
    # print('%s is running  索引：%d' % (os.getpid(), index))
    # time.sleep(2)
    # print('%s is done 索引：%d' % (os.getpid(), index))
    # lock.release()
    with open(r'practice/file.txt', 'a', encoding='utf-8') as f:  # /会被转义，加r
      # 现在需要解决的是 文件写入中文的问题   打开文件的时候   以 encoding = "utf-8"  这里有时候是utf8  有时候又是utf-8
      # 另一个如何换行添加写入呢  发现这种写入文件 这一块是一个原子操作的   with 它会自动获取  释放锁
        f.write('%s is start 索引：%d\n' % (os.getpid(), index))
        time.sleep(3)
        f.write('%s is done 索引：%d\n' % (os.getpid(), index))
    # lock.acquire()

    # # 这里我发现使用with进行写入的时候 是有使用锁机制来保证安全的
    # with open('practice/file.txt', 'a', encoding='utf-8') as f:
    #     f.write('%s is start 索引：%d\n' % (os.getpid(), index))
    # time.sleep(2)
    # with open('practice/file.txt', 'a', encoding='utf-8') as f:
    #     f.write('%s is done 索引：%d\n' % (os.getpid(), index))
    # lock.release()


'''
这里稍微的总结下的  字典的遍历可以使用items 而数组需要有索引 使用enumerate方法

锁能保存的是在一个进程的运行下 占用cpu资源时 其它进行不能同时参与的   
而不是说  我第一个 进程是排队执行的

我可以尝试下写文件的操作的
'''


def test(i):
    print(i)


if __name__ == '__main__':
    # lock = Lock()
    # p_list = []
    # for index in range(10):
    #     p = Process(target=work, args=(lock, index))
    #     p.start()
    #     p_list.append(p)
    # for index, item in enumerate(p_list):
    #     p_list[index].join()

    # print('主进程结束')
    pool = Pool(processes=10)
    for i in range(500):
        '''
        ('\n'
         '	（1）遍历500个可迭代对象，往进程池放一个子进程\n'
         '	（2）执行这个子进程，等子进程执行完毕，再往进程池放一个子进程，再执行。（同时只执行一个子进程）\n'
         '	 for循环执行完毕，再执行print函数。\n'
         '	')
        '''
        pool.apply_async(test, args=(i,))  # 维持执行的进程总数为10，当一个进程执行完后启动一个新进程.
    pool.close()
    pool.join()

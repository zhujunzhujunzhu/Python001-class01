'''
@Description 
@Autor 朱俊
@Date 2020-07-11 12:33:46
@LastEditors 朱俊
@LastEditTime 2020-07-11 19:02:39
'''
import multiprocessing


def scan(port):
    s = socket.socket()
    s.settimeout(0.1)
    if s.connect_ex(('localhost', port)) == 0:
        print(f"端口号{port}开启")
    s.close()


def worker(q):
    while not q.empty():
        port = q.get()
        try:
            scan(port)
        finally:
            q.task_done()


if __name__ == '__main__':
    # q = multiprocessing.JoinableQueue()
    # map(q.put, xrange(1, 65535))
    # jobs = [multiprocessing.Process(target=worker, args=(q,))
    #         for i in xrange(100)]
    # map(lambda x: x.start(), jobs)
    user_input = int(input("请输入 "))
    if 1 == user_input:
        print("成功了")
    else:
        print(user_input)

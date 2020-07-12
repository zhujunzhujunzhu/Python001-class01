'''
@Description 
@Autor 朱俊
@Date 2020-07-12 10:27:23
@LastEditors 朱俊
@LastEditTime 2020-07-12 10:27:24
'''
# -*- coding: UTF-8 -*-
import time
import threading
import subprocess
from queue import Queue
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import platform


def get_ip_list(net_segment, ip_num):
    # 创建一个队列
    IP_QUEUE = Queue()
    ip_list = []
    list_segment = net_segment.split('.')
    ip_index = 1
    # 将需要 ping 的 ip 加入队列
    for i in range(1, 254):
        list_segment[-1] = str(ip_index + i)
        addr = ('.').join(list_segment)
        IP_QUEUE.put(addr)

    # 定义一个执行 ping 的函数
    def ping_ip(ip):
        os_type = platform.system()
        if os_type == 'Windows':
            # linux 系统将 '-n' 替换成 '-c',增加 'shell=True'
            res = subprocess.call('ping -n 2 -w 5 %s' %
                                  ip, stdout=subprocess.PIPE)
        else:
            # linux 系统将 '-n' 替换成 '-c',增加 'shell=True'
            res = subprocess.call('ping -c 2 -w 5 %s' %
                                  ip, shell=True, stdout=subprocess.PIPE)
        # windows 系统，则使用 'ping -n 2 -w 5 $s'
        # 打印运行结果
        print(ip, True if res == 0 else False)
        if res != 0:
            if lock.acquire():
                if len(ip_list) < ip_num:
                    ip_list.append(ip)
                lock.release()

    # 创建一个最大任务为100的线程池
    pool = ThreadPoolExecutor(max_workers=100)
    lock = threading.Lock()
    start_time = time.time()
    all_task = []
    while not IP_QUEUE.empty():
        all_task.append(pool.submit(ping_ip, IP_QUEUE.get()))
    # 等待所有任务结束
    wait(all_task, return_when=ALL_COMPLETED)
    print('ping耗时：%s' % (time.time() - start_time))
    if len(ip_list) < ip_num:
        print("Warning：当前网段可用ip不够，需要数量：%s，可用数量：%s" %
              (str(ip_num), str(len(ip_list))))
    return ip_list


if __name__ == '__main__':
    print(platform.system())
    ip_list = get_ip_list("180.8.53.0", 100)
    ip_list.sort()
    print(ip_list)
    print(len(ip_list))

# ping  -n 2 -w 5 127.0.0.1
# ping  -n 2 -w 5 127.0.0.1

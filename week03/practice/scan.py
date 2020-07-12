'''
@Description 
@Autor 朱俊
@Date 2020-07-11 12:31:49
@LastEditors 朱俊
@LastEditTime 2020-07-11 22:33:01
'''

from multiprocessing import Process
import gevent.pool
import gevent
import time
import socket
from gevent import monkey
monkey.patch_all()


arg_flags = ['-n', '-f', '-ip', '-w']


def TCP_connect(ip, port):
    """模拟TCP连接"""
    TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_sock.settimeout(0.5)  # 设置连接超时
    try:
      # 这个看到了一个基本的小的用法的  TCP_sock 有方法 connect_ex 这样就是可以检测端口是否开启的
        result = TCP_sock.connect_ex((ip, int(port)))
        if result == 0:
            print("[*]%s 端口 开启\t" % port)
        else:
            # print("[!]%s端口 关闭"%port)
            pass
        TCP_sock.close()
    except socket.error as e:
        print("[!]错误:", e)


def scan_ip():
    """扫描目标IP"""
    ip = input("[+]输入扫描目标IP:")
    print("[*]正在扫描")
    scan_port(ip)


def scan_web():
    """扫描目标网址"""
    web = input("[+]输入扫描网址:")
    if "http://" in web or "https://" in web:
        web = web[web.find('://')+3:]
        print(web)
        print("[*]正在分析网站服务器IP")
    try:
        server_ip = socket.gethostbyname(str(web))
        print("[*]服务器IP为%s" % server_ip)
        scan_port(server_ip)
    except Exception as e:
        print("[!]服务器IP获取失败")
        print(e)


# 这里看到了 gevent的基本的使用的  gevent pool 线程池的设置  g.spawn 这个就是开启一个线程的 第一个参数是要执行的函数  其余的都是参数  开启了线程后 主线程需要进行
# 等待线程的执行完成的  需要使用gevent.joinall 方法的
def scan_port(ip):
    """扫描端口"""
    print("[*]开始扫描目标端口")
    start = time.time()
    g = gevent.pool.Pool(50)  # 设置线程数

    run_list = []
    # 这里可以看到的端口号 最大的是65535
    for port in range(1, 1024):
        # p = Process(target=TCP_connect, args=(ip, port))
        # p.start()
        # run_list.append(p)
        run_list.append(g.spawn(TCP_connect, ip, port))
    gevent.joinall(run_list)
    # for run_item in run_list:
    #     run_item.join()

    end = time.time()
    print("[*]总耗时%s" % time.strftime("%H:%M:%S", time.gmtime(end-start)))


def main():
    print(
        """
    1.通过IP扫描端口
    2.通过网址扫描端口
    """
    )
    # 关于输入操作这里我会了 是使用input 来的
    uc = int(input("[+]请输入选择:"))
    if 1 == uc:
        scan_ip()
    elif 2 == uc:
        scan_web()
    else:
        print("[!]输入有误")


if __name__ == "__main__":
    main()

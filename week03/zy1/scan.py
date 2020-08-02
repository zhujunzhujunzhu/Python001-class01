'''
@Description
@Autor 朱俊
@Date 2020-07-11 21:45:58
@LastEditors 朱俊
@LastEditTime 2020-07-12 23:08:42
'''
'''
背景： 网络安全工具中有一个常用软件称作端口扫描器，即通过一台主机发起向另一主机的常用端口发起连接，探测目标主机是否开放了指定端口（1-1024），用于改善目标主机的安全状况。
要求：编写一个基于多进程或多线程模型的主机扫描器。

使用扫描器可以基于 ping 命令快速检测一个 IP 段是否可以 ping 通，如果可以 ping 通返回主机 IP，如果无法 ping 通忽略连接。
使用扫描器可以快速检测一个指定 IP 地址开放了哪些 tcp 端口，并在终端显示该主机全部开放的端口。
IP 地址、使用 ping 或者使用 tcp 检测功能、以及并发数量，由命令行参数传入。
需考虑网络异常、超时等问题，增加必要的异常处理。
因网络情况复杂，避免造成网络拥堵，需支持用户指定并发数量。
命令行参数举例如下：
pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100

pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json

说明：

因大家学习的操作系统版本不同，建立 tcp 连接的工具不限，可以使用 telnet、nc 或 Python 自带的 socket 套接字。
-n：指定并发数量。
-f ping：进行 ping 测试
-f tcp：进行 tcp 端口开放、关闭测试。
-ip：连续 IP 地址支持 192.168.0.1-192.168.0.100 写法。
-w：扫描结果进行保存。
'''
# from gevent import monkey
# monkey.patch_all()


from multiprocessing  import Pool
import subprocess
import json
import sys
import socket
from  queue import Queue
import gevent.pool
import gevent, time
arg_flags = ['-n', '-f', '-ip', '-w']


def get_arg():
    '''
    获取脚本参数
    '''
    dict = {}
    for flag in arg_flags:
        if flag in sys.argv:
            num_index = sys.argv.index(flag)
            flag_value = sys.argv[num_index+1]
            dict[flag[1:]] = flag_value
    return dict


def write_json(q, config):
    dict = {
        "ip": config["ip"],
        "port": []
    }
    while not q.empty():
        dict['port'].append(q.get())

    print(dict)
    # config['w'] != None  这样是不行的 字典中都是不存在的 会直接有报错   判断字典中有无 属性
    if config.__contains("w"):
        with open(config["w"], "w", encoding='utf-8') as f:
            # json.dump(dict_var, f)  # 写为一行
            json.dump(dict, f, indent=2, sort_keys=True,
                      ensure_ascii=False)  # 写为多行


def TCP_connect(ip, port, q):
    """模拟TCP连接"""
    TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_sock.settimeout(0.5)  # 设置连接超时
    try:
        result = TCP_sock.connect_ex((ip, int(port)))
        if result == 0:
            print("[*]%s 端口 开启\t" % port)
            # 添加写入到文件的操作
            q.put({
                "ip": ip,
                "port": port,
                "msg": "[*]%s 端口 开启\t" % port
            })
        else:
            pass
        TCP_sock.close()
        # write_json(dict, config)
    except socket.error as e:
        print("[!]错误:", e)


def scan_port(config):
    """扫描端口"""
    print("[*]开始扫描目标端口")
    start = time.time()
    g = gevent.pool.Pool(int(config['n']))  # 设置线程数
    ip = config['ip']
    run_list = []
    #  使用队列
    q = Queue()
    # 65535
    for port in range(1, 330):
        run_list.append(g.spawn(TCP_connect, ip, port, q))
    gevent.joinall(run_list)
    write_json(q, config)

    end = time.time()
    print("[*]总耗时%s" % time.strftime("%H:%M:%S", time.gmtime(end-start)))

    # ping 网段ip


def ping_host(activeq, notactiveq, ipaddr):
    print(ipaddr)
    # ping -c1 -w1 中-c1是指ping的次数，-w是指执行的最后期限，也就是执行的时间，单位为秒
    if subprocess.call('ping -c1 -W 1 %s > /dev/null' % ipaddr, shell=True) != 0:
        activeq.put(ipaddr)
    else:
        notactiveq.put(ipaddr)

# 读取队列数据


def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print(value)
        else:
            break


def test(activeq, notactiveq, ipaddr):
    print(ipaddr)


def pint_test(config):
  # 创建进程间通信队列
    activeq = Queue()
    notactiveq = Queue()
    host_list = []
    ips = config["ip"].split("-")
    start_ip = ips[0].split('.')
    end_ip = ips[1].split('.')
    base_ip = '.'.join(start_ip[:3])
    start_num = start_ip[3]
    end_num = end_ip[3]
    for ipnum in range(int(start_num), int(end_num)):
        host_list.append(f'{base_ip}.{str(ipnum)}')
    # 创建进程池
    pool = Pool(processes=int(config['n']))
    for ipaddr in host_list:
        pool.apply_async(ping_host, args=(activeq, notactiveq, ipaddr))
    pool.close()
    pool.join()
    # 输出正在使用ip
    read(activeq)
    # 输出未被使用ip
    read(notactiveq)

    # pool = Pool(10)
    # for i in range(500):
    #     pool.apply(test, args=(1, 2, i,))  # 维持执行的进程总数为10，当一个进程执行完后启动一个新进程.
    # pool.close()
    # pool.join()


# python scan.py -n 10 -f tcp -ip 180.167.213.122 -w result.json
#  python scan.py -n 10 -f ping -ip 180.167.213.0-180.167.213.255
if __name__ == '__main__':
    config = get_arg()
    if config['f'] == 'tcp':
        scan_port(config)
    elif config['f'] == 'ping':
        pint_test(config)

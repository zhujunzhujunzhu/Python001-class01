'''
@Description 
@Autor 朱俊
@Date 2020-07-06 22:14:52
@LastEditors 朱俊
@LastEditTime 2020-07-10 14:33:04
'''

'''
先可以来看下这一段的  这个是事件驱动框架的使用的 
'''




from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor
def response(*args, **kwargs):
  # 这里其实发现 args里面返回的是 请求网页的内容的包装的 而 kwargs 这个是是字典的 参数的
  #  ** 两个是是解包吧  对关键字参数进行相应的处理的  我大概清楚了的 对关键字参数进行收集变成一个字典的
    print(kwargs)
    print('返回的网页的内容')


def callback():
    print("我是callback函数")


@defer.inlineCallbacks
def start(url):
  # 这里我看到了 可以对字符串有一个encode方法的 getPage 这个方法就是相当于requests.get?
    d = getPage(url.encode('utf-8'))
    d.addCallback(response, name="zhujun", age=25)
    d.addCallback(callback)
    yield d


def stop(*args, **kwargs):
    reactor.stop()


urls = ['http://www.baidu.com', 'http://www.sougou.com']
li = []

for url in urls:
  # 这一块是发现了一个报错的 to produce a generator; instead got None   是因为start里面最后少了一个yield 关键字的
    ret = start(url)
    li.append(ret)

print(li)

# 异步队列先添加到li中  然后将li作为参数传入defer.DeferredList 这个异步队列中  我现在需要看看  DefereedList这个是怎么使用的
'''
 DeferredList(deferrlist, fireOnOneCallback=0， fireOnOneErrback=1, consumeErrors=1).addCallback(deferrlist_suc).addErrback(deferrlist_suc)
    deferrlist： 其所需等待的defer对象列表
    fireOnOneCallback：deferrlist列表中任一defer对象callback后，DeferredList就回调callback
    fireOnOneErrback： deferrlist列表中任一defer对象errback后，如果deferr对象未指定errback，DeferredList就回调errback 
'''
d = defer.DeferredList(li)
d.addCallback(stop)
reactor.run()

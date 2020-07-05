## 本周学习内容

#### 异常

异常这一块我只知道了 try except 有一定的概念

#### pymysql 数据库操作

这个是本周学习的主要的内容的 操作数据库 通过 pymysql  
 通过将数据写入到数据库 知道了相关的知识 @classmethod
关于 python 的方法有 类方法 （@classmethod） 静态方法（@staticmethod） 还有成员方法
pipeline 管道文件的 一些函数 ：open_spider close_spider from_crawler

存储的数据如何自增 id？
查找到当前最大的 id
sql = "select max(id) as id from movies"
cursor = conn.cursor()
cursor.excute(sql)
往数据中添加 id
temps = []
for item in self.items:
temps.append(
{
id:max_id,
\*\*item
}
)

#### selenium webdriver

会感觉到这个是一个很神奇的东西的 安装 selenium 库 下载 chromdirver 执行程序就是可以对浏览器进行操作
与 time 库结合起来使用
找元素的方法 通过 id 类 或者 xpath 的方式
对元素的重要操作
.send_keys() 进行表单的填写
.click() 模拟点击

#### 自定义中间件与代理 ip

这里我主要学习到的东西是 重新写一个下载中间件 对包 模块 类 有了更深的认识

#### 整体感受

因为工作日比较忙 每天虽然有例行公事的去看视频 但是没有时间去实践 自己就是没有感觉的 觉得只有双休的实践还是不行的
觉得都是讲的东西还是挺多的 很多重要的东西还是不太清晰 第三周会每天利用早上的时间 听课并加上实践的

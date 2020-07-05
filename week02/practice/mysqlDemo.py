'''
@Description 
@Autor 朱俊
@Date 2020-07-02 07:00:16
@LastEditors 朱俊
@LastEditTime 2020-07-05 15:34:10
'''
# 导入pymysql库
import pymysql
CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": 'pytest',
    "charset": 'utf8mb4'
}

# 创建基本的数据库连接 端口号为数值类型
conn = pymysql.connect(host=CONFIG["host"], port=CONFIG["port"], user=CONFIG["user"],
                       passwd=CONFIG["password"], database=CONFIG["database"],
                       cursorclass=pymysql.cursors.DictCursor,
                       charset=CONFIG["charset"])
# 得到一个可以执行sql的 并且返回字典的游标
# cusor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 利用mysql创建基本的 电影列表

# create_table = '''
#    CREATE TABLE movies (
#      id INT(11),
#      name VARCHAR(255),
#      time VARCHAR(255),
#      short LONGTEXT
#    )
# '''
# cusor.excute(sql)


# 添加操作
'''
 现在这里面我其实是学到了几个基本的东西的  一个是使用excutemany  这个是可以执行带有占位符的sql语句的
 现在需要问的事情是
'''
sql = 'insert into movies(name,time,short,id) values(%s,%s,%s,%s);'
# data = [
#     ('test1', '2020-1-1', '基本的内容众1'),
#     ('test2', '2020-1-1', '基本的内容众2'),
#     ('test3', '2020-1-1', '基本的内容众3')
# ]
cursor = conn.cursor()
# 执行sql 通过占位符的方式
# cusor.executemany(sql, data)
# 找到最后一条数据的id
select_max_id = 'select max(id) as max_id from movies'
cursor.execute(select_max_id)


back = cursor.fetchone()
max_id = back["max_id"]
if max_id == None:
    max_id = 0


# 上面的这种写法  后面的还会执行吗 如果执行了 finally 又有什么用呢？
data = [
    {"name": "test1", "time": "2020-1-1", "short": "基本的内容11"},
    {"name": "test2", "time": "2020-1-1", "short": "基本的内容22"},
    {"name": "test3", "time": "2020-1-1", "short": "基本的内容33"},
]

for item in data:
    max_id += 1
    item["id"] = max_id


# 这里我尝试使用一下landama 表达式  如何将字典转换为元组 中间不需要 `,`   tuplue(dict) 这个是将键转换为元素  如果想让值转换为元组需要item.values()
# 这样得出来的顺序是id在最后面的
sqlData = [tuple(item.values()) for item in data]
try:
    cursor.executemany(sql, sqlData)
# # 提交修改操作，执行commit后才能成功修改
    conn.commit()
except Exception as e:
    raise e

finally:
    # # 关闭光标
    cursor.close()
# # 关闭数据连接
conn.close()


# 关于数据库的查询操作

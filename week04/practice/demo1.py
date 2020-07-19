'''
https://blog.csdn.net/qq_38251616/article/details/84752080
1 写csv文件
2 读csv文件
3 DataFrame 遍历 合并
4 行 查找  删除
5 重复项
6 元素
7 排序
'''
import os
import pandas as pd


'''
写文件：
关于这里可以看到的是  任意多组列表 
可以利用字典映射索引
可以设置mode  是否加上索引
可以添加上分隔符sep
mode = a 代表不覆盖原有的内容的

practice/csv/test0.csv 当写路径时  如果csv不存在时会报错
'''
# a = [1, 2, 3]
# b = [4, 5, 6]
# data_dict = {"a_name": a, "b_name": b}

# df = pd.DataFrame(data_dict, columns=['a_name', "b_name"])


# df.to_csv('practice/csv/test0.csv', index=True)
# df.to_csv('practice/csv/test1.csv', index=False, sep="|")
# df.to_csv('practice/csv/test2.csv', mode="a", index=False, sep="#")


'''
读csv文件
__file__ 这个代表的是当前目录  但是需要注意在交互模式下不可以的
os.path.join() 进行地址的拼接
os.path.dirname(__file__) 当前文件所在的目录 
pd.read_csv 
open(file_path,encoding="utf-8")
数据的遍历
data.iterrows  iterrows是行进行迭代的生成器

for column, row in data.iterrows()
关于python中的这一段   column row 这两个是固定的命名还是只是因为它们的位置？
需要记住的对于data.iterrows 来说进行迭代的话 有两个值  一个是索引 另一个是行

肯定这里还有关于列的迭代

'''

# file_path = os.path.join(os.path.dirname(__file__), 'csv/test0.csv')
# # print(os.path.abspath(__file__))
# # print(os.path.dirname(__file__))
# # print(file_path)

# data = pd.read_csv(open(file_path, 'r', encoding='utf-8'))

# print(data)
# a_name_list = []
# for index, row in data.iterrows():
#     print(index, row)
#     a_name_list.append(row['a_name'])

# print(a_name_list)

'''
 DataFrame 数据合并 concat 
 有纵向的合并  有横向的合并 行向的合并就会有主次之分的
 axis为1时是横向的
 concat传入的参数是　列表　元素类型为dp.DataFrame 
 当axis=1 为横向拼接 0 或者不写 为纵向的拼接
 此外还有join关键字 inner是得到交集 outer并集  交并  目前join 并没有看出加与不加的区别的
'''
a = [1, 2, 3]
b = [4, 5, 6]
data_dict = {'name': a, 'title': b}
pf = pd.DataFrame(data_dict, columns=['name', 'title'])
c = [7, 8, 9]
d = [9, 8, 7]
data_dict1 = {'name': c, 'title': d}
pf1 = pd.DataFrame(data_dict1, columns=['name', 'title'])


c_pf = pd.concat([pf, pf1])
# print(c_pf)
c_pf1 = pd.concat([pf, pf1], axis=1)
# print(c_pf1)

c_pf2 = pd.concat([pf, pf1], axis=1, join="inner")
c_pf3 = pd.concat([pf, pf1], join="inner")
# print(c_pf2, c_pf3)


'''
基本的行列的查找
看到的方法是 loc iloc ix
https://blog.csdn.net/qq_38251616/article/details/84752080

loc 进行行定位 pf.loc(index) 依赖的是索引   
    进行列定位 pf.loc(:,'name') 依赖的是列名
    进行多行  定义多列  添加 :
    可以认为它是根据行标签来的

iloc 利用自然行数来进行定位（依旧是从0开始的）  可以认为它是一个二维矩阵的定位  可以认为它是根据行索引来的
ix 进行混合的定位  这个ix现在是不能使用了的？？ 被弃用的
'''

c_pf4 = c_pf3.loc['name']
print(c_pf4)

'''
@Description 
@Autor 朱俊
@Date 2020-07-17 12:33:52
LastEditors 朱俊
LastEditTime 2020-08-16 13:56:37
'''
import pandas as pd
import numpy as np
# 我会觉得这个是一个比较常见的形式的
list_dict = [
    {"name": "zhujun", "age": 25},
    {"name": "zhujun1", "age": None},
    {"name": "zhujun2", "age": 27}
]

df = pd.DataFrame(list_dict)

print(df)


# df.count()
#  name 3
#  age 2  利用df.count 进行统计的时候是按照列进行统计的   None不作为统计结果


# 这里进行加操作的时候其实是没有改变原来的df的
df1 = df['age']+5

# https://www.pypandas.cn/docs/getting_started/10min.html#生成对象

# 进行缺失值的填充
df1.fillna(value=26)

# TypeError: cannot concatenate object of type '<class 'dict'>'; only Series and DataFrame objs are valid
# df1.append({"name": "append", "age": 25})
# 这里会提示只有series才可以进行追加的

# df1.append(pd.Series({"name": "append", "age": 25}))  这个name age是作为了替换了索引的
df.append(pd.Series(['append', 25]), ignore_index=True)


df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
s = df.iloc[3]
# 关于ignore_index 这个对索引进行忽略 还是需要经常性的用到的
df.append(s, ignore_index=True)
# 这样的方式是取的列的
df['A']

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
#  这个分组没有太明白的 A 分组 然后统计
df.groupby('A').sum()

df.loc[1, 1]
df.iloc[1, 'A']


df = pd.DataFrame(
    [{"A": "foo", "B": "one1"}, {"A": "foo", "B": "one2"}, {"A": "foo3", "B": "one3"}, {
        "A": "foo4", "B": "one4"}, {"A": "foo5", "B": "one5"}, {"A": "foo6", "B": "one6"}]
)



# 这里我能将pf转换为字典列表吗  我可以先通过遍历来进行实现的
dict_list = []
# index A　Ｂ　Ｃ D
for index, df_item in df.T.items():
    dict = {}
    for inner, inner_item in df_item.items():
        dict[inner] = inner_item
    dict_list.append(dict)
print(dict_list)

# 但是这个结果还是不想要的  我想到了采用转置的方式的
#  使用to_excel 它会依赖xlwt 模块的 这个是一个第三方模块的 因此首先是需要进行安装的
df.to_excel('practice/csv/test111.xls', index=False)
# 导入需要依赖的模块是xlrd    这个还是很强大的  读出来的数据直接是DataFrame格式的
excel = pd.read_excel('practice/csv/test111.xls')


for item in iter(dict_list):
    if '漫游' in item['内容']:
        item['内容'].replace('漫游', '测试')
'''
@Description
@Autor 朱俊
@Date 2020-07-19 15:30:18
@LastEditors 朱俊
@LastEditTime 2020-07-19 21:15:02
'''
'''
请将以下的 SQL 语句翻译成 pandas 语句：
1. SELECT * FROM data;

2. SELECT * FROM data LIMIT 10;

3. SELECT id FROM data;  //id 是 data 表的特定一列

4. SELECT COUNT(id) FROM data;

5. SELECT * FROM data WHERE id<1000 AND age>30;

6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

8. SELECT * FROM table1 UNION SELECT * FROM table2;

9. DELETE FROM table1 WHERE id=10;

10. ALTER TABLE table1 DROP COLUMN column_name;
'''
import pandas as pd
import pymysql
import os
path_file = os.path.dirname(__file__)+'/movies.csv'
con = pymysql.connect(
    host="localhost", user="root", password="root", db="pytest")


# 1. SELECT * FROM data;
df = pd.read_sql("SELECT * FROM movies", con)

# 2 SELECT * FROM data LIMIT 10;
# df.loc[:,'id':'type']   这里如果我选取指定两列  id type  df.loc[:,['id','type']]
df.iloc[:10]

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
id = df['id']
name = df.loc[:, 'name']


# 4. SELECT COUNT(id) FROM data;
row_num = df.shape[0]
col_num = df.shape[1]

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
# df[(df['id']<1000) & (df['age']>30)]
# 需要注意的是这里多条件进行筛选的时候需要进行加上（）
df[(df['id'] < 13) & (df['id'] > 10)]


# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
df = pd.DataFrame({'A': ['foo1', 'bar2', 'foo1', 'bar4',
                         'foo5', 'bar6', 'foo1', 'foo9'],
                   'B': [2, 3, 3, 3,
                         2, 2, 1, 4]})
df.groupby(["A"])['A'].value_counts()

df = pd.DataFrame({'A': ['foo1', 'bar2', 'foo3', 'bar4',
                         'foo5', 'bar6', 'foo7', 'foo9'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three']})
df1 = pd.DataFrame({'A': ['foo1', 'bar2', 'foo3', 'bar4',
                          'foo5', 'bar6', 'foo7', 'foo8'],
                    'B1': ['one1', 'one1', 'two1', 'three1',
                           'two1', 'two1', 'one1', 'three1']})


# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
#  可以看到merge的使用方式  与 concat的使用方式还是不同的 在传参上   concat传入一个df列表的
pd.merge(df, df1, how="inner", on='A')


# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([df, df1])
# 9. DELETE FROM table1 WHERE id=10;
# df[df['id']!=10]
df[df['A'] != 'foo1']
df.drop(df[df['A'] == 'foo1'].index)  # 这个也没有改变原来的df的

# 10. ALTER TABLE table1 DROP COLUMN column_name;
df2 = df.drop(['A'], axis=1)

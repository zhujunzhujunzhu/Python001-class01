import pymysql
import numpy as np
import pandas as pd
from snownlp import SnowNLP
from sqlalchemy import create_engine

MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'pytest'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'

conn = pymysql.connect(
    host=MYSQL_HOST, port=MYSQL_PORT,
    user=MYSQL_USER, password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE,
    charset="utf8")
sql = "select name,good_id,comment_info from qipaoshui_comment"

cursor = conn.cursor()


def main():
    df = pd.read_sql(sql, conn)
    df['sentiments'] = df['comment_info'].map(lambda x: SnowNLP(x).sentiments)
    df.replace({np.nan: None})
    df1 = df.groupby(['name', 'good_id']).mean()

    # 存储到数据库
    df_dict = df.T.to_dict()
    keys = df_dict.keys()
    values = [(df_dict[key]['sentiments'], df_dict[key]['good_id'])
              for key in keys]

    df_dict1 = df1.T.to_dict()
    keys1 = df_dict1.keys()
    values1 = [key+(df_dict1[key]['sentiments'],) for key in keys1]
    try:
        # commit_id_list上面已经说明
        cursor.executemany(
            "update qipaoshui_comment SET sentiments=(%s) where good_id = (%s)", values)
        # cursor.executemany(
        #     "insert into qipaoshui_sentiments(name,good_id,score) values(%s,%s,%s)", values1)
        conn.commit()
    except Exception as err:
        print(err)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    main()

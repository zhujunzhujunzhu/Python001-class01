# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import time
from itemadapter import ItemAdapter
import pymysql
from twisted.enterprise import adbapi
from .items import QpsItem, QpsCommentItem


class BasePipeline:
    def process_item(self, item, spider):
        crawl_time = time.strftime("%Y-%m-%d %H:%M:%S")
        item.update({
            'spider_name': spider.name,
            'crawl_time': crawl_time,
            'update_time': crawl_time,
        })
        return item


class QpsPipeline:
    def __init__(self, dbpool):
        self.dbpool = dbpool

    def process_item(self, item, spider):
        """
         使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
         """
        query = self.dbpool.runInteraction(self.do_insert, item)
        # 添加异常处理
        query.addCallback(self.handle_error)

    @classmethod
    def from_settings(cls, settings):
        """
          数据库建立连接
          :param settings: 配置参数
          :return: 实例化参数
        """
        adbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            cursorclass=pymysql.cursors.DictCursor  # 指定cursor类型
        )
        dbpool = adbapi.ConnectionPool('pymysql', **adbparams)
        return cls(dbpool)

    def do_insert(self, cursor, item):
        # 对数据库进行操作 不需要commit twisted 会自动commit
        if type(item) == QpsItem:
            self.insert_qipaoshui(cursor, item)
        elif type(item) == QpsCommentItem:
            self.insert_qipaoshui_comment(cursor, item)

    def insert_qipaoshui(self, cursor, item):
        insert_sql = """
          insert into qipaoshui(name,good_id,url,spider_name,crawl_time,update_time) values (%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(
            insert_sql, (item['name'], item['good_id'],
                         item['url'], item['spider_name'],
                         item['crawl_time'], item['update_time']))

    def insert_qipaoshui_comment(self, cursor, item):
        insert_sql = """
          insert into qipaoshui_comment(name,comment_info,good_id,comment_type,spider_name,crawl_time,update_time) 
          values (%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(
            insert_sql,
            (item['name'], item['comment_info'], item['good_id'],
             item['comment_type'], item['spider_name'],
             item['crawl_time'], item['update_time'],))

    def handle_error(self, failure):
      # 异常处理
        if failure:
            # 打印错误信息
            print(failure)

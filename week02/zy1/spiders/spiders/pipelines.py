# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class SpidersPipeline:
    def __init__(self, settings):
        self.settings = settings
        self.items = []
        # self.connect = pymysql.connect(
        #     host=self.settings.get('MYSQL_HOST'),
        #     port=self.settings.get('MYSQL_PORT'),
        #     db=self.settings.get('MYSQL_DBNAME'),
        #     user=self.settings.get('MYSQL_USER'),
        #     passwd=self.settings.get('MYSQL_PASSWD'),
        #     charset='utf8mb4',
        #     use_unicode=True)

        # # 通过cursor执行增删查改
        # self.cursor = self.connect.cursor()
        # self.get_max_id()

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        # def spider_opened(self, spider):
        # 连接数据库
        self.connect = pymysql.connect(
            host=self.settings.get('MYSQL_HOST'),
            port=self.settings.get('MYSQL_PORT'),
            db=self.settings.get('MYSQL_DBNAME'),
            user=self.settings.get('MYSQL_USER'),
            passwd=self.settings.get('MYSQL_PASSWD'),
            cursorclass=pymysql.cursors.DictCursor,
            charset='utf8mb4',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
        self.get_max_id()
        self.connect.autocommit(True)

    def close_spider(self, spider):
        # insert_db
        self.insert_db()
        # pass

    def get_max_id(self):
        sql = "select max(id) as max_id from movies"
        try:
            self.cursor.execute(sql)
            back = self.cursor.fetchone()
            max_id = back["max_id"]
            if max_id == None:
                max_id = 0
            self.max_id = max_id
        except Exception as e:
            raise e

    def insert_db(self):
        sql = 'insert into movies(id,name,type,grade,time,short) values(%s,%s,%s,%s,%s,%s);'
        temps = []
        for item in self.items:
            self.max_id += 1
            temps.append({
                "id": self.max_id,
                **item
            })
            # 本来是使用  会直接走不过去的  可以尝试在items 添加一个id定义下的 不行的
            # item["id"] = self.max_id
            # item = {
            #     "id": self.max_id,
            #     **item
            # }
        print(self.items)
        data = [tuple(item.values()) for item in temps]
        try:
            self.cursor.executemany(sql, data)
            self.connect.commit()
        except Exception:
            pass
        finally:
            self.cursor.close()
            self.connect.close()

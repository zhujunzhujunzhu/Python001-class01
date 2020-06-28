# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import json
import csv


class SpidersPipeline:
    # 利用pd写入到csv文件中去
    # def __init__(self):
    #     self.items = []

    # def process_item(self, item, spider):
    #     self.items.append(item)
    #     return item

    # def close_spider(self, spider):
    #     df = pd.DataFrame(self.items)
    #     df.to_csv('test_movies.csv')
    # 写入到json文件中去
    # def __init__(self):
    #     self.file = open('movies.json', "a+", encoding='utf8')

    # def process_item(self, item, spider):
    #     lines = json.dumps(dict(item), ensure_ascii=False) + ",\n"
    #     self.file.write(lines)
    #     # return item 这个是向控制台输出的
    #     return item

    # def close_spider(self, spider):
    #     self.file.close()
    def __init__(self):
        columns = ['name', 'href']
        file_name = 'test_.csv'
        # newline为空，写入时不会出现空行
        file = open(file_name, 'w', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(file, columns)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class SpidersPipeline:
    def __init__(self):
        columns = ['name', 'type', 'time', 'short']
        file_name = 'maoyan2.csv'
        # newline为空，写入时不会出现空行
        file = open(file_name, 'w', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(file, columns)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

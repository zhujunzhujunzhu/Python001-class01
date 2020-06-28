# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersItem(scrapy.Item):
    print(scrapy.Item)
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 可以认为就是为字典设置属性  然后呢在 具体爬取的时候是可以
    name = scrapy.Field()
    href = scrapy.Field()
    # pass

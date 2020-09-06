# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class BaseItem(Item):
    # goodid = Field()
    crawl_time = Field()
    update_time = Field()
    spider_name = Field()


class QpsItem(BaseItem):
    good_id = Field()
    name = Field()
    url = Field()


class QpsCommentItem(BaseItem):
    name = Field()
    good_id = Field()
    comment_type = Field()
    comment_info = Field()

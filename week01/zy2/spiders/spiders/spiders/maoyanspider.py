import scrapy
from lxml import etree
# import lxml.etree
from spiders.items import SpidersItem

'''
使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

猫眼电影网址： https://maoyan.com/films?showType=3

要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选
'''


class MaoyanspiderSpider(scrapy.Spider):
    name = 'maoyanspider'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.items = []
        html = etree.HTML(response.text)
        dls = html.xpath('//*/dd')
        for dl in dls:
            name = dl.xpath(
                './div[1]/div[2]/a/div/div[1]/span/text()')[0]
            type = dl.xpath(
                './div[1]/div[2]/a/div/div[2]/text()')[1].strip()
            time = dl.xpath(
                './div[1]/div[2]/a/div/div[4]/text()')[1].strip()
            href = dl.xpath("./div[1]/a/@href")[0]
            item = SpidersItem()
            item["name"] = name
            item["type"] = type
            item["time"] = time
            url = f'https://maoyan.com{href}'
            yield scrapy.Request(
                url=url, meta={"item": item}, callback=self.parse_detail)
            # self.items.append(item)
        # return self.items

    def parse_detail(self, response):
        item = response.meta["item"]
        html = etree.HTML(response.text)
        short = html.xpath(
            '//*[@id="app"]/div/div[1]/div/div[3]/div[1]/div[1]/div[2]/span/text()')[0]
        item["short"] = short
        yield item

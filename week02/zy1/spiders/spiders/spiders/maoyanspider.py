import scrapy
from lxml import etree
from spiders.items import SpidersItem


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
        # try:
        self.items = []
        html = etree.HTML(response.text)
        dls = html.xpath('//*/dd')
        for dl in dls[:20]:
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
        # except Exception as e:
        #     print(e)

    def parse_detail(self, response):
        item = response.meta["item"]
        html = etree.HTML(response.text)
        short = html.xpath(
            '//*[@id="app"]/div/div[1]/div/div[3]/div[1]/div[1]/div[2]/span/text()')[0]
        item["short"] = short
        yield item

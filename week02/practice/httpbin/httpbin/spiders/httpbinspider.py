import scrapy


class HttpbinspiderSpider(scrapy.Spider):
    name = 'httpbinspider'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        print(response.text())

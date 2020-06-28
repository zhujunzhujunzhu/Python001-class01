import scrapy
from bs4 import BeautifulSoup as bs
# import SpidersItem
from spiders.items import SpidersItem


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['moive.douban.com']
    start_urls = ['https://movie.douban.com/top250']
    # 注释默认parse函数  它是从start_users中去取
    # def parse(self, response):
    #     pass

    # 开始发起请求
    # 爬虫启动时 引擎自动调用该方法 并且只会被调用一次 用于生成初始的请求对象
    def start_requests(self):
        for i in range(0, 10):
            url = f"https://movie.douban.com/top250?start={i*25}"
            yield scrapy.Request(url=url, callback=self.parse)
    # 解析函数

    def parse(self, response):
        items = []
        soup = bs(response.text, 'html.parser')
        for index, tags in enumerate(soup.find_all('div', {'class': 'hd'})):
            for content in tags.find_all('a'):
                href = content.get('href')
                name = content.find('span').text
                # print(f'名称:{name} 电影链接:{href}')
                # 利用提供的Item
                item = SpidersItem()
                item["name"] = name
                item["href"] = href
                items.append(item)
        return items

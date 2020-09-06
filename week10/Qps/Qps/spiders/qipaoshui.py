import scrapy
from ..items import QpsItem, QpsCommentItem


class QipaoshuiSpider(scrapy.Spider):
    name = 'qipaoshui'
    allowed_domains = ['www.smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/qipaoshui/']

    def parse(self, response):
        qipaoshui_list = response.css('#feed-main-list .feed-row-wide')

        for qiaoshui_item in qipaoshui_list:
            good_id = qiaoshui_item.css('::attr(articleid)').get()
            name = qiaoshui_item.css('.feed-block-title a::text').get()
            url = qiaoshui_item.css(
                '.feed-block-title a::attr(href)').get()
            yield QpsItem(**{
                'good_id': good_id,
                'name': name,
                'url': url
            })
            yield scrapy.Request(
                url=url, meta={"name": name, "good_id": good_id}, callback=self.parse_detail)

    def parse_detail(self, response):
        comments_new = response.css('#commentTabBlockNew .comment_list')
        comments_history = response.css('#history-comments .comment_list')
        comments = [{"selectors": x, "type": 'new'} for x in comments_new] + \
            [{"selectors": x, "type": 'history'} for x in comments_history]
        if comments:
            for item in comments:
                comment = item["selectors"].css('p span::text').get()
                yield QpsCommentItem(**{
                    'name': response.meta['name'],
                    'good_id': response.meta['good_id'],
                    'comment_info': comment,
                    'comment_type': item["type"]
                })

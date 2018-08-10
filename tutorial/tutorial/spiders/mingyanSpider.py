# coding:utf-8
"""
爬虫实例
http://www.scrapyd.cn/doc/179.html
"""

import scrapy
from tutorial.items import *

class mingyanSpider(scrapy.Spider):
    name = 'quotes'
    # start_urls = [
    #     'http://lab.scrapyd.cn/'
    # ]

    def start_requests(self):
        """通过url爬取页面"""
        url = 'http://lab.scrapyd.cn/'
        tag = getattr(self, 'tag', None)  # 爬取时传过来的参数
        if tag:
            url += '/tag/' + tag
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in response.css('#main div'):
            mi = i.css('span.text::text').extract_first(),
            ar = i.xpath('span/small/text()').extract_first(),
            tag = ','.join(i.css('.tags .tag::text').extract())
            d = TutorialItem()
            d['content'] = mi[0]
            d['name'] = ar[0]
            d['tag'] = tag
            yield d

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
           yield scrapy.Request(next_page, self.parse)
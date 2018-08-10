# -*- coding: utf-8 -*-

"""美剧天堂最新更新爬取"""

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tutorial.items import *

class MeijuSpider(CrawlSpider):
    name = 'meiju'
    allowed_domains = ['meiju.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse(self, response):
        for i in response.xpath('//ul[@class="top-list  fn-clear"]/li'):
            d = MeijuItem()
            d['tag'] = i.xpath('./span[@class="mjjq"]/text()').extract_first()
            d['title'] = i.xpath('./h5/a/@title').extract_first()
            d['TV'] = i.xpath('./span[@class="mjtv"]/text()').extract_first()
            d['update_date'] = i.xpath('./div[@class="lasted-time new100time fn-right"]/text()').extract_first()
            yield d

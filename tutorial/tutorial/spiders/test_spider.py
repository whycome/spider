# coding:utf-8
"""爬虫"""

import scrapy

class TestScrapy(scrapy.Spider):

    name = 'test'
    # def start_requests(self):
    #     """通过url爬取页面"""
    #     urls = [
    #         'http://lab.scrapyd.cn/page/1/',
    #         'http://lab.scrapyd.cn/page/2/'
    #     ]
    #     for url in urls:
    #         # 爬去的页面提交给parse处理
            # yield scrapy.Request(url=url, callback=self.parse)
    """
        上述start_requests可以简写为一下形式，但必须定义方法parse, 其方法名必须为parse
    """
    start_urls = [
        'http://lab.scrapyd.cn/',
        'http://lab.scrapyd.cn/page/2/'
    ]

    def parse(self, response):
        """start_request已经爬取到页面，可在此提取数据"""
        page = response.url.split("/")[-2]
        fn = 'test_%s.html' % page
        with open(fn, 'wb') as f:
            f.write(response.body)
        self.log('保存文件： %s' % fn)
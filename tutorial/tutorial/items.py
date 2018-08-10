# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# 从非结构化源提取结构化数据
import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    content = scrapy.Field()
    name = scrapy.Field()
    tag = scrapy.Field()

class MeijuItem(scrapy.Item):
    title = scrapy.Field()
    tag = scrapy.Field()
    TV = scrapy.Field()
    update_date = scrapy.Field()

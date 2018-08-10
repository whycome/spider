# -*- coding: utf-8 -*-

# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class TutorialPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(host='127.0.0.1', port=3306, db='test', user='root', passwd='xxx', charset='utf8', use_unicode=True)
        self.cur = self.connect.cursor()
        self.connect.autocommit(True)

    def open_spider(self):
        """
        在spider开始的时候执行，在这个函数中我们一般会连接数据库，为数据存储做准备
        :return:
        """
        pass

    def process_item(self, item, spider):
        """
        在捕捉到item的时候执行，一般我们会在这里做数据过滤并且把数据存入数据库
        :param item:
        :param spider:
        :return:
        """
        if spider.name == 'meiju':
            sql = '''
                insert into meiju (tag, title, TV, update_date) values ('{tag}', '{title}', '{TV}', '{update_date}')
            '''.format(tag=item['tag'], title=item['title'], TV=item['TV'], update_date=item['update_date'])
            self.cur.execute(sql)
        else:
            sql = '''
                insert into tag(name, content, tag) values ('{name}', '{content}', '{tag}')
            '''.format(name=item['name'], content=item['content'], tag=item['tag'])
            print(sql)
            self.cur.execute(sql)
            return item

    def close_spider(self):
        """
        在spider结束的时候执行，一般用来断开数据库连接或者做数据收尾工作。
        :return:
        """

class MongodbPipeline(object):
    def open_spider(self):
        pass
    def process_item(self, item, spider):
        pass
    def close_spider(self):
        pass


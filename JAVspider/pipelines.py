# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
from scrapy.exceptions import DropItem


class JavspiderPipeline(object):
    def __init__(self):
        self.con=sqlite3.connect(database='vedio.db')
        self.cur=self.con.cursor()
    def process_item(self, item, spider):
        try:
            self.cur.execute(r'''INSERT INTO av VALUES ("%s","%s","%s")'''%(item['code'][0],item['title'][0],item['cover'][0]))
        except:
            raise DropItem
        return item
    def close_spider(self,spider):
        self.con.commit()
            

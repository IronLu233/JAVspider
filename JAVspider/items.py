# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JavspiderItem(scrapy.Item):
    code = scrapy.Field()
    title = scrapy.Field()
    cover = scrapy.Field()

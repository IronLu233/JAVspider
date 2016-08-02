import scrapy
from ..items import JavspiderItem
class JAVspider(scrapy.Spider):
    name = 'JAV'
    allowed_domains = ['javlibrary.com']
    start_urls=['http://www.javlibrary.com/cn/']
    def parse(self,response):
        av=JavspiderItem()
        for video in response.xpath('//div[@class="video"]'):
            av['title'] = video.xpath('a/@title').extract()
            av['number'] = video.xpath('a/div/text()').extract()
            av['cover'] = video.xpath('a/img/@src').extract()
            yield av
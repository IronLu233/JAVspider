from scrapy.http import Request
import scrapy
from ..items import JavspiderItem


class JAVspider(scrapy.Spider):
    name = 'JAV'
    allowed_domains = ['javlibrary.com']
    start_urls=['http://www.javlibrary.com/cn/vl_update.php']+['http://www.javlibrary.com/cn/vl_update.php?&mode=&page=%d'%i for i in range(2,251)]
    
    def parse(self,response):
        av=JavspiderItem()
        for video in response.xpath(r'//div[@class="video"]'):
            av['title'] = video.xpath(r'a/@title').extract()
            av['code'] = video.xpath(r'a/div/text()').extract()
            av['cover'] = video.xpath(r'a/img/@src').extract()
            yield av
        
        
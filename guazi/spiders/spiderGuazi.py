import scrapy


class SpiderguaziSpider(scrapy.Spider):
    name = 'spiderGuazi'
    allowed_domains = ['https://www.guazi.com/jn/buy/']
    start_urls = ['http://https://www.guazi.com/jn/buy//']

    def parse(self, response):
        pass

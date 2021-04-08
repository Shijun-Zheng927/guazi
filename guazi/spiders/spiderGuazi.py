import scrapy


class SpiderguaziSpider(scrapy.Spider):
    name = 'spiderGuazi'
    # allowed_domains = ['https://www.guazi.com/jn/buy/']
    start_urls = ['https://www.guazi.com/jn/buy/o1/#bread']

    def parse(self, response):
        title = response.xpath('//html/head/title/text()')
        print(title)
        pass

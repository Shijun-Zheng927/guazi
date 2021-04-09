import scrapy
from guazi.items import GuaziItem

class GuazidetailSpider(scrapy.Spider):
    name = 'guaziDetail'
    # allowed_domains = ['https://www.guazi.com/']
    start_urls = ['https://www.guazi.com/km/3e5c480840f87495x.htm#fr_page=list&fr_pos=city&fr_no=0',
                  'https://www.guazi.com/xm/befab89f749020afx.htm#fr_page=list&fr_pos=city&fr_no=1']

    def parse(self, response):
        item = GuaziItem()
        item['name'] = response.xpath('/html/body/div[4]/div[3]/div[2]/h1/text()').get().strip()
        item['img'] = response.xpath('//*[@id="page-slide"]/div[1]/ul/li[1]/img/@data-src').get()

        yield item

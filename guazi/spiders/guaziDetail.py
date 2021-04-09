import scrapy
from guazi.items import GuaziItem

class GuazidetailSpider(scrapy.Spider):
    name = 'guaziDetail'
    # allowed_domains = ['https://www.guazi.com/']
    # start_urls = ['https://www.guazi.com/km/3e5c480840f87495x.htm#fr_page=list&fr_pos=city&fr_no=0',
    #               'https://www.guazi.com/xm/befab89f749020afx.htm#fr_page=list&fr_pos=city&fr_no=1',
    #               'https://www.guazi.com/sy/4bc5ab60a7156e07x.htm#fr_page=list&fr_pos=city&fr_no=2']
    urls = []
    # 读取url列表
    with open("url_detail/default.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip("\n")
            # print(line)
            urls.append(line)
    # print(urls)
    start_urls = urls

    def parse(self, response):
        print(response.request.url)
        item = GuaziItem()
        item['name'] = response.xpath('/html/body/div[4]/div[3]/div[2]/h1/text()').get().strip()
        item['img'] = response.xpath('//*[@id="page-slide"]/div[1]/ul/li[1]/img/@data-src').get()
        item['mileage'] = response.xpath('/html/body/div[4]/div[3]/div[2]/ul/li[2]/span/text()').get()
        item['displacement0'] = response.xpath('/html/body/div[4]/div[3]/div[2]/ul/li[3]/span/text()').get()
        item['gearbox0'] = response.xpath('/html/body/div[4]/div[3]/div[2]/ul/li[4]/span/text()').get()
        item['price'] = response.xpath('/html/body/div[4]/div[3]/div[2]/div[1]/div[2]/span/text()').get()

        item['standard'] = response.xpath('/html/body/div[4]/div[5]/ul/li[3]/div/text()').get().strip()
        item['owner'] = response.xpath('/html/body/div[4]/div[5]/ul/li[6]/div/text()').get().strip()
        item['service'] = response.xpath('/html/body/div[4]/div[5]/ul/li[7]/div/text()').get()
        item['purpose'] = response.xpath('/html/body/div[4]/div[5]/ul/li[8]/div/text()').get()
        item['property'] = response.xpath('/html/body/div[4]/div[5]/ul/li[9]/div/text()').get()

        item['manufacturer'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[1]/tr[2]/td[2]/text()').get()
        item['level'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[1]/tr[3]/td[2]/text()').get()
        item['engine'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[1]/tr[4]/td[2]/text()').get()
        item['gearbox'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[1]/tr[5]/td[2]/text()').get()
        item['structure'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[1]/tr[6]/td[2]/text()').get()
        item['size'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[1]/tr[7]/td[2]/text()').get()
        item['wheelbase'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[1]/tr[8]/td[2]/text()').get()
        item['luggage'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[1]/tr[9]/td[2]/text()').get()
        item['weight'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[1]/tr[10]/td[2]/text()').get()

        item['displacement'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[2]/tr[2]/td[2]/text()').get()
        item['intake'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[2]/tr[3]/td[2]/text()').get()
        item['cylinder'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[2]/tr[4]/td[2]/text()').get()
        item['horsepower'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[2]/tr[5]/td[2]/text()').get()
        item['torque'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[2]/tr[6]/td[2]/text()').get()
        item['fuel'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[2]/tr[7]/td[2]/text()').get()
        item['fuelGrade'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[2]/tr[8]/td[2]/text()').get()
        item['fuelFeeding'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[2]/tr[9]/td[2]/text()').get()

        item['mode'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[3]/tr[2]/td[2]/text()').get()
        item['help'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[3]/tr[3]/td[2]/text()').get()
        item['frontSuspension'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[3]/tr[4]/td[2]/text()').get()
        item['backSuspension'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[3]/tr[5]/td[2]/text()').get()
        item['frontBraking'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[3]/tr[6]/td[2]/text()').get()
        item['backBraking'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[3]/tr[7]/td[2]/text()').get()
        item['braking'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[3]/tr[8]/td[2]/text()').get()
        item['frontWheel'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[3]/tr[9]/td[2]/text()').get()
        item['backWheel'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[3]/tr[10]/td[2]/text()').get()

        item['airbag'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[4]/tr[2]/td[2]/text()').get()
        item['sideAirbag'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[4]/tr[3]/td[2]/text()').get()
        item['headAirbag'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[4]/tr[4]/td[2]/text()').get()
        item['tirePressure'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[4]/tr[5]/td[2]/text()').get()
        item['centralLocking'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[4]/tr[6]/td[2]/text()').get()
        item['childSeat'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[4]/tr[7]/td[2]/text()').get()
        item['keylessStart'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[4]/tr[8]/td[2]/text()').get()
        item['abs'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[4]/tr[9]/td[2]/text()').get()
        item['esp'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[4]/tr[10]/td[2]/text()').get()

        item['electricSunroof'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[5]/tr[2]/td[2]/text()').get()
        item['panoramicSunroof'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[5]/tr[3]/td[2]/text()').get()
        item['softCloseDoors'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[5]/tr[4]/td[2]/text()').get()
        item['inductionTrunk'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[5]/tr[5]/td[2]/text()').get()
        item['inductionWiper'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[5]/tr[6]/td[2]/text()').get()
        item['backWiper'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[5]/tr[7]/td[2]/text()').get()
        item['electricWindow'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[5]/tr[8]/td[2]/text()').get()
        item['electricMirror'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[5]/tr[9]/td[2]/text()').get()
        item['mirrorHeating'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[5]/tr[10]/td[2]/text()').get()

        item['steeringWheel'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[6]/tr[2]/td[2]/text()').get()
        item['cruiseControl'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[6]/tr[3]/td[2]/text()').get()
        item['backAC'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[6]/tr[4]/td[2]/text()').get()
        item['ACControl'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[6]/tr[5]/td[2]/text()').get()
        item['GPS'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[6]/tr[6]/td[2]/text()').get()
        item['reversingRadar'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[6]/tr[7]/td[2]/text()').get()
        item['reversingImage'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[6]/tr[8]/td[2]/text()').get()
        item['leatherSeat'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[6]/tr[9]/td[2]/text()').get()
        item['seatHeating'] = response.xpath('/html/body/div[4]/div[5]/div[2]/table[6]/tr[10]/td[2]/text()').get()

        item['url'] = response.request.url

        yield item

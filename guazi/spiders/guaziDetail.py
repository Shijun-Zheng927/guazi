import csv

import scrapy
from guazi.items import GuaziItem

class GuazidetailSpider(scrapy.Spider):
    name = 'guaziDetail'
    # allowed_domains = ['https://www.guazi.com/']
    # start_urls = ['https://www.guazi.com/sh/ce4079f7e502d60dx.htm#fr_page=list&fr_pos=city&fr_no=14',
    #               'https://www.guazi.com/gz/2c4043854835345bx.htm#fr_page=list&fr_pos=city&fr_no=13']
    # urls = []
    # 读取url列表
    # with open("url_detail/honda.txt", "r", encoding="utf-8") as f:
    #     for line in f.readlines():
    #         line = line.strip("\n")
    #         # print(line)
    #         urls.append(line)
    # # print(urls)
    # start_urls = urls

    with open('data/honda.csv', "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        column = [row['链接'] for row in reader]
    print(len(column))
    allUrl = []
    with open("url_detail/honda.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip('\n')
            allUrl.append(line)
    # print(len(allUrl))
    urls = set(allUrl) - set(column)
    # print(list(urls))
    start_urls = list(urls)

    def parse(self, response):
        print(response.request.url)
        str = response.xpath('/html/body/div[4]/div[4]/div[1]/h2/text()').get()
        div = '5'
        if str == '瓜子严选车':
            div = '6'
            print("yanxuan:" + response.request.url)
        item = GuaziItem()
        item['name'] = response.xpath('/html/body/div[4]/div[3]/div[2]/h1/text()').get().strip()
        item['img'] = response.xpath('//*[@id="page-slide"]/div[1]/ul/li[1]/img/@data-src').get()
        item['mileage'] = response.xpath('/html/body/div[4]/div[3]/div[2]/ul/li[2]/span/text()').get()
        item['displacement0'] = response.xpath('/html/body/div[4]/div[3]/div[2]/ul/li[3]/span/text()').get()
        item['gearbox0'] = response.xpath('/html/body/div[4]/div[3]/div[2]/ul/li[4]/span/text()').get()
        item['price'] = response.xpath('/html/body/div[4]/div[3]/div[2]/div[1]/div[2]/span/text()').get()

        item['standard'] = response.xpath('/html/body/div[4]/div[' + div + ']/ul/li[3]/div/text()').get().strip()
        item['owner'] = response.xpath('/html/body/div[4]/div[' + div + ']/ul/li[6]/div/text()').get().strip()
        item['service'] = response.xpath('/html/body/div[4]/div[' + div + ']/ul/li[7]/div/text()').get()
        item['purpose'] = response.xpath('/html/body/div[4]/div[' + div + ']/ul/li[8]/div/text()').get()
        item['property'] = response.xpath('/html/body/div[4]/div[' + div + ']/ul/li[9]/div/text()').get()

        item['manufacturer'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[1]/tr[2]/td[2]/text()').get()
        item['level'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[1]/tr[3]/td[2]/text()').get()
        item['engine'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[1]/tr[4]/td[2]/text()').get()
        item['gearbox'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[1]/tr[5]/td[2]/text()').get()
        item['structure'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[1]/tr[6]/td[2]/text()').get()
        item['size'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[1]/tr[7]/td[2]/text()').get()
        item['wheelbase'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[1]/tr[8]/td[2]/text()').get()
        item['luggage'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[1]/tr[9]/td[2]/text()').get()
        item['weight'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[1]/tr[10]/td[2]/text()').get()

        item['displacement'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[2]/tr[2]/td[2]/text()').get()
        item['intake'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[2]/tr[3]/td[2]/text()').get()
        item['cylinder'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[2]/tr[4]/td[2]/text()').get()
        item['horsepower'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[2]/tr[5]/td[2]/text()').get()
        item['torque'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[2]/tr[6]/td[2]/text()').get()
        item['fuel'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[2]/tr[7]/td[2]/text()').get()
        item['fuelGrade'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[2]/tr[8]/td[2]/text()').get()
        item['fuelFeeding'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[2]/tr[9]/td[2]/text()').get()

        item['mode'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[3]/tr[2]/td[2]/text()').get()
        item['help'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[3]/tr[3]/td[2]/text()').get()
        item['frontSuspension'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[3]/tr[4]/td[2]/text()').get()
        item['backSuspension'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[3]/tr[5]/td[2]/text()').get()
        item['frontBraking'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[3]/tr[6]/td[2]/text()').get()
        item['backBraking'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[3]/tr[7]/td[2]/text()').get()
        item['braking'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[3]/tr[8]/td[2]/text()').get()
        item['frontWheel'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[3]/tr[9]/td[2]/text()').get()
        item['backWheel'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[3]/tr[10]/td[2]/text()').get()

        item['airbag'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[4]/tr[2]/td[2]/text()').get()
        item['sideAirbag'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[4]/tr[3]/td[2]/text()').get()
        item['headAirbag'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[4]/tr[4]/td[2]/text()').get()
        item['tirePressure'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[4]/tr[5]/td[2]/text()').get()
        item['centralLocking'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[4]/tr[6]/td[2]/text()').get()
        item['childSeat'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[4]/tr[7]/td[2]/text()').get()
        item['keylessStart'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[4]/tr[8]/td[2]/text()').get()
        item['abs'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[4]/tr[9]/td[2]/text()').get()
        item['esp'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[4]/tr[10]/td[2]/text()').get()

        item['electricSunroof'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[5]/tr[2]/td[2]/text()').get()
        item['panoramicSunroof'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[5]/tr[3]/td[2]/text()').get()
        item['softCloseDoors'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[5]/tr[4]/td[2]/text()').get()
        item['inductionTrunk'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[5]/tr[5]/td[2]/text()').get()
        item['inductionWiper'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[5]/tr[6]/td[2]/text()').get()
        item['backWiper'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[5]/tr[7]/td[2]/text()').get()
        item['electricWindow'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[5]/tr[8]/td[2]/text()').get()
        item['electricMirror'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[5]/tr[9]/td[2]/text()').get()
        item['mirrorHeating'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[5]/tr[10]/td[2]/text()').get()

        item['steeringWheel'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[6]/tr[2]/td[2]/text()').get()
        item['cruiseControl'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[6]/tr[3]/td[2]/text()').get()
        item['backAC'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[6]/tr[4]/td[2]/text()').get()
        item['ACControl'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[6]/tr[5]/td[2]/text()').get()
        item['GPS'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[6]/tr[6]/td[2]/text()').get()
        item['reversingRadar'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[6]/tr[7]/td[2]/text()').get()
        item['reversingImage'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[6]/tr[8]/td[2]/text()').get()
        item['leatherSeat'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[6]/tr[9]/td[2]/text()').get()
        item['seatHeating'] = response.xpath('/html/body/div[4]/div[' + div + ']/div[2]/table[6]/tr[10]/td[2]/text()').get()

        item['url'] = response.request.url

        yield item

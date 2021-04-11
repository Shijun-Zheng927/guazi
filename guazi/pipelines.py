# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

from itemadapter import ItemAdapter


class GuaziPipeline:
    def process_item(self, item, spider):
        # print('pipeline' + item['name'])
        with open('data/honda1.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            # writer.writerow(['名称', '图片'])
            # 名称,图片
            writer.writerow([item['name'], item['img'], item['mileage'], item['displacement0'], item['gearbox0'],
                             item['price'], item['standard'], item['owner'], item['service'], item['purpose'],
                             item['purpose'],
                             item['manufacturer'], item['level'], item['engine'], item['gearbox'], item['structure'],
                             item['size'], item['wheelbase'], item['luggage'], item['weight'],
                             item['displacement'], item['intake'], item['cylinder'], item['horsepower'],
                             item['torque'], item['fuel'], item['fuelGrade'], item['fuelFeeding'],
                             item['mode'], item['help'], item['frontSuspension'], item['backSuspension'],
                             item['frontBraking'], item['backBraking'], item['braking'], item['frontWheel'],
                             item['backWheel'],
                             item['airbag'], item['sideAirbag'], item['headAirbag'], item['tirePressure'],
                             item['centralLocking'], item['childSeat'], item['keylessStart'], item['abs'], item['esp'],
                             item['electricSunroof'], item['panoramicSunroof'], item['softCloseDoors'],
                             item['inductionTrunk'], item['inductionWiper'], item['backWiper'],
                             item['electricWindow'], item['electricMirror'], item['mirrorHeating'],
                             item['steeringWheel'], item['cruiseControl'], item['backAC'], item['ACControl'],
                             item['GPS'], item['reversingRadar'], item['reversingImage'], item['leatherSeat'],
                             item['seatHeating'], item['url']
                             ])
            print(item)
        return item

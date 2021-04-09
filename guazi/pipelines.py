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
        with open('data/default.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            # writer.writerow(['名称', '图片'])
            # 名称,图片
            writer.writerow([item['name'], item['img']])
        return item

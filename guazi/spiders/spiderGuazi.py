import scrapy


class SpiderguaziSpider(scrapy.Spider):
    name = 'spiderGuazi'
    # allowed_domains = ['https://www.guazi.com/jn/buy/']
    start_urls = ['https://www.guazi.com/jn/buy/o1/#bread']

    def parse(self, response):
        title = response.xpath('//html/head/title/text()')
        print(title)
        url = response.xpath('/html/body/div[6]/ul/li[1]/a/@href').get()
        print(url)
        for i in range(1, 41):
            print(i)
            url = response.xpath('/html/body/div[6]/ul/li[' + str(i) + ']/a/@href').get()
            print(url)


        # lists = response.xpath('//ul[@class="carlist clearfix js-top"]')
        # print(lists)
        # for i in lists:
        #     url = i.xpath('./li/a/@href').get()
        #     print("url:" + url)
        pass

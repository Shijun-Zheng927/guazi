import scrapy


class SpiderguaziSpider(scrapy.Spider):
    name = 'spiderGuazi'
    # allowed_domains = ['https://www.guazi.com/jn/buy/']
    urls = []
    #读取url列表
    with open("url_brif/volkswagen.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip("\n")
            print(line)
            urls.append(line)
    print(urls)
    start_urls = urls

    def parse(self, response):
        print(response.request.url)
        title = response.xpath('//html/head/title/text()')
        print(title)
        # url = response.xpath('/html/body/div[6]/ul/li[1]/a/@href').get()
        # print(url)
        #获取每个详情页的url
        result = ""
        for i in range(1, 41):
            url = response.xpath('/html/body/div[6]/ul/li[' + str(i) + ']/a/@href').get()
            url = "https://www.guazi.com" + url + "\n"
            print(url, end="")
            result += url
        #写入文件
        with open("url_detail/volkswagen.txt", "a", encoding="utf-8") as f:
            f.write(result)


        # lists = response.xpath('//ul[@class="carlist clearfix js-top"]')
        # print(lists)
        # for i in lists:
        #     url = i.xpath('./li/a/@href').get()
        #     print("url:" + url)
        pass

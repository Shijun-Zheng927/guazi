from scrapy import cmdline

# cmdline.execute('scrapy crawl spiderGuazi'.split())

cmdline.execute('scrapy crawl guaziDetail'.split())

# urls = []
# with open("url1.txt", "r") as f:
#     for line in f.readlines():
#         line = line.strip("\n")
#         print(line)
#         urls.append(line)
# print(urls)
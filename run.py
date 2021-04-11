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


# import csv
# with open('data/volkswagen.csv', "r", encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile)
#     column = [row['链接'] for row in reader]
# print(len(column))
# allUrl = []
# with open("url_detail/volkswagen.txt", "r", encoding="utf-8") as f:
#     for line in f.readlines():
#         line = line.strip('\n')
#         allUrl.append(line)
# print(len(allUrl))
# urls = set(allUrl) - set(column)
# print(list(urls))
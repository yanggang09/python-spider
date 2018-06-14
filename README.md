# python-spider
这主要存放写爬虫代码
#coding='utf-8'
import scrapy
import time

class GupiaoInfo(scrapy.Spider):
    name = "gupiao"
    start_urls = []
    file_path = "C:\\Users\\Administrator\\gitcode\\python-spider\\spider_gh"
    name = time.strftime("%Y%m%d", time.localtime(time.time()))
    file_path02 = file_path + '\\' + 'Data' + name + '\\' + 'final.txt'
    list_00 = []
    f08 = open(file_path02, 'ab+')
    for lines in f08.readlines():
        list_00.append(lines)
    list_01 = []
    for i in range(10,49):
        a = list_00[i].split(" ")[1]
        urls = 'http://so.eastmoney.com/web/s?keyword=' + a
        start_urls.append(urls)

    def parse(self, response):
        gp_daima = response.xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div/div[3]/div[1]/table/tbody/tr/td[1]/div/a/text()").extract()
        for i in gp_daima:
            print i


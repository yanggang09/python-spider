#coding=utf-8
#- * - coding: utf-8 - * -
import scrapy
from  ..items import GetfilmItem
import os
import time
import xlrd
from xlwt import *
from xlutils.copy import copy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def savetoexcel(dataname):
    name = time.strftime("%Y%m%d%H", time.localtime(time.time()))
    excel_name = 'FilmDownUrl.xls'
    file = Workbook(encoding='utf-8')
    table = file.add_sheet('data')
    ldata = []
    num = [a for a in dataname]
    num.sort()
    for x in num:
        t = [int(x)]
        for a in dataname[x]:
            t.append(a)
        ldata.append(t)

    for i, p in enumerate(ldata):
        for j, q in enumerate(p):
            table.write(i, j, q)
    file.save(excel_name)

class GetFilm(scrapy.Spider):
    name = "dianying"
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        # Dianying = GetfilmItem()
        test01 = response.xpath('//td[@height="26"]/b/a/@href').extract()
        test02 = response.xpath('//td[@height="26"]/b/a/text()').extract()
        list_00 = []
        list_01 = []
        data_00 = {0:["名称","链接"]}
        c = 1
        for i in test01:

            url_link = 'http://www.ygdy8.net' + i
            list_00.append(url_link)
        for a,b in zip(list_00,test02):
            data_00[c]=[b,a]
            c+=1
        for m in list_00:
            yield scrapy.Request(url=m,callback=self.parse02)
    def parse02(self,response):
        # print response
        test03 = response.xpath('//td[@style="WORD-WRAP: break-word"]/a/@thunderrestitle').extract()
        for k in test03:
            print k





#encoding=utf-8
# -*- coding: utf-8 -*-
import scrapy
import time
from ..items import SpiderGhItem
import json
import unicodedata
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')


def write_txt(filename, filestr):
    f0 = open(filename, 'ab+')
    f0.write(filestr)
    f0.close()

class ghYuBao(scrapy.Spider):
    name = "yubao"
    start_urls = [ 'http://www.178448.com/fjzt-1.html' ]
    for a in range(1,50):
        yb_url = 'http://www.178448.com/fjzt-1.html?'+ 'page=' + str(a)
        start_urls.append(yb_url)




    def parse(self, response):
        yb = SpiderGhItem()
        yb_name = response.xpath(".//*[@id='ct']/div/div[4]/table/tbody/tr/td[1]/a/text()").extract()
        yb_count = response.xpath(".//*[@id='ct']/div/div[4]/table/tbody/tr/td[2]/text()").extract()
        yb_successrate = response.xpath(".//*[@id='ct']/div/div[4]/table/tbody/tr/td[3]/text()").extract()
        yb_stock = response.xpath(".//*[@id='ct']/div/div[4]/table/tbody/tr/td[4]/text()").extract()
        yb_cause = response.xpath(".//*[@id='ct']/div/div[4]/table/tbody/tr/td[5]/text()").extract()

        # date = time.strftime("%Y%m%d%M%M",time.localtime(time.time()))
        text_01 = 'Name'  + '.txt'
        text_02 = 'Count'  + '.txt'
        text_03 ='Successrate'  + '.txt'
        text_04 = 'Stock' + '.txt'
        text_05 = 'Cause' + '.txt'


        for b,c,d,e,f in zip(yb_name,yb_count,yb_successrate,yb_stock,yb_cause):
           yb['Name'] = b
           yb['Count'] = c
           yb['Successrate'] = d
           yb['Stock'] = e
           yb['Cause'] = f
           # yb['Name'] = b.encode('utf-8')
           # yb['Count'] = c.encode('utf-8')
           # yb['Successrate'] = d.encode('utf-8')
           # yb['Stock'] = e.encode('utf-8')
           # yb['Cause'] = f.encode('utf-8')
           #str1 = "%s %s %s %s %s \n"%(yb['Name'],yb['Count'],yb['Successrate'],yb['Stock'],yb['Cause'])
           str1 = "%s %s\n"%(yb['Name'],yb['Stock'])
           # str2 = "%s\n"% yb['Count']
           # str3 = "%s\n" % yb['Successrate']
           str4 = "%s\n" % yb['Stock']
           # str5 = "%s\n" % yb['Cause']
           write_txt(text_01,str1)
           write_txt(text_04, str4)
           # yield yb
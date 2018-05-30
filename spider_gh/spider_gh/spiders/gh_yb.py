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
        # for c in yb_count:
        #     print b
            # b1,c1,d1,e1,f1 = str(b),str(c),str(d),str(e),str(f)
            # print (b1,c1,d1,e1,f1)
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
           # str1 = "%s:  %s %s %s %s \n"%(yb['Name'],yb['Count'],yb['Successrate'],yb['Stock'],yb['Cause'])
           str1 = "%s\n" % yb['Name']
           str2 = "%s\n"% yb['Count']
           str3 = "%s\n" % yb['Successrate']
           str4 = "%s\n" % yb['Stock']
           str5 = "%s\n" % yb['Cause']
           f0 = open(text_01,'ab+')
           f0.write(str1)
           f0.close()
           f1 = open(text_02, 'ab+')
           f1.write(str2)
           f1.close()
           f2 = open(text_03, 'ab+')
           f2.write(str3)
           f2.close()
           f3 = open(text_04, 'ab+')
           f3.write(str4)
           f3.close()
           f4 = open(text_05, 'ab+')
           f4.write(str5)
           f4.close()
           # yield yb
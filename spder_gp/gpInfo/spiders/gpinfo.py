#coding='utf-8'
# -*- UTF-8 -*-
import scrapy 
import time
from scrapy.selector import Selector
import pickle
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class GupiaoInfo(scrapy.Spider):
	name = "gupiao"
	start_urls = []
	for m in range(1,35):
		urls01 = 'http://app.finance.ifeng.com/list/stock.php?t=sa&f=symbol&o=asc&p=' + str(m)
		start_urls.append(urls01)
	for i in range(1,35):
		urls = 'http://app.finance.ifeng.com/list/stock.php?t=ha&f=symbol&o=asc&p=' + str(i)
		start_urls.append(urls)


	def parse(self, response):

		gp_daima = response.xpath('//td/a[@target="_blank"]/text()').extract()
		gp_bodong = response.xpath("//span[contains(@class,'A')]/text()").extract()
		list_ZD = []
		list_IF = []
		for i in gp_bodong:
			list_ZD.append(i)
		list_ZD01 = list_ZD[1::6]
		for j in gp_daima:
			list_IF.append(j)
		list_IF01 = list_IF[1::2]
		list_IF02 = list_IF[::2]
		dict_IF = {}
		for b,c in zip(list_IF01,list_ZD01):
			dict_IF[b] = c
		Info01 = sorted(dict_IF.items(),key = lambda  x:x[1],reverse=True)
		for k in Info01:
			m = ":".join(k)
			str01 = "%s\n"%m
			f1 = open("GUpiaoinfo01.txt",'ab+')
			f1.write(str01)
			f1.close()
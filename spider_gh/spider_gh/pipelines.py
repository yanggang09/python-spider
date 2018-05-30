# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class SpiderGhPipeline(object):
    def open_spider(self,spider):
        self.con = sqlite3.connect("yubao.sqlite")
        self.cu = self.con.cursor()
    def process_item(self, item, spider):
        print (spider.name,'yubao')
        # insert_sql = "insert into yubao (ybname,ybcount,ybsuccessrate,ybstock,ybcause) \
        #            values ('{}','{}','{}','{}','{}')".format(item['Name'],item['Count'],\
        #                                                      item['Successrate'],item['Stock'],item['Cause'])
        # print(insert_sql)
        # insert_sql = "insert into yubao (ybname) values('{}')".format(item['Name'])
        # insert_sql = "insert into yubao (ybname,ybcount,ybsuccessrate,ybstock,ybcause) \
        #                  values ('{}','{}','{}','{}','{}')".format( item['Name'], "", \
        #                                                             "", "", "" )
        # self.cu.execute(insert_sql)
        return item
    def spider_close(self,spider):
        self.con.close()

#coding=utf-8
# -*- UTF-8 -*-

import os
import time
import xlrd
from xlwt import *
from xlutils.copy import copy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

xlsfile = "test1.xls"

file = Workbook(encoding= 'utf-8')

table = file.add_sheet('data')

file_path = os.getcwd()
name = time.strftime("%Y%m%d%H",time.localtime(time.time()))
excel_name = name + 'StockInfo.xls'
file_path02 = 'GUpiaoinfo.txt'
list_00 = []
f08 = open(file_path02, 'ab+')
c = 1
data1 = {0:["股票名称","涨跌详情"]}
for i in f08.readlines():
    list_01 = []
    i = i.split("\n")[0]
    e = i.split(":")[0]
    try:
        if i.split(":")[1]:
             b =i.split(":")[1]
    except:
        b = "数据丢失"
    list_01.append(e)
    list_01.append(b)
    data1[c] = list_01
    c +=1

ldata = []
num = [a for a in data1]
num.sort()
for x in num:
    t = [int(x)]
    for a in data1[x]:
        t.append(a)
    ldata.append(t)

for i, p in enumerate(ldata):
    for j, q in enumerate(p):
        table.write(i, j, q)
file.save(excel_name)

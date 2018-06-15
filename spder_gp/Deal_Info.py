#coding='utf-8'
# -*- UTF-8 -*-
import scrapy
import time
from scrapy.selector import Selector
import pickle
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

f2 = open("GUpiaoinfo01.txt", 'ab+')
dict_02 = {}
for h in f2.readlines():
    a = h.split(":")[0]
    dict_02[a] = h.split(":")[1]
f2.close()
Info02 = sorted(dict_02.items(), key=lambda x: x[1], reverse=True)

file_path = "C:\Users\Administrator\gitcode\python-spider\spider_gh"
date = time.strftime("%Y%m%d", time.localtime(time.time()))
file_path02 = file_path + '\\' + 'Data' + date + '\\' + 'final.txt'
list_00 = []
f08 = open(file_path02, 'ab+')
for i in f08.readlines():
    a  = i.split(" ")[1]
    list_00.append(a.split("\n")[0])
for j in range(10,50):
    if dict_02.has_key(list_00[j]):
        str02 = "%s:%s"%(list_00[j],dict_02[list_00[j]])
        f3 = open("GUpiaoinfo.txt", 'ab+')
        f3.write(str02)
        f3.close()
    else:
        str03 = "%s\n"%list_00[j]
        f3 = open("GUpiaoinfo.txt", 'ab+')
        f3.write(str03)
        f3.close()
for z in Info02[:99]:
        y = ":".join(z)
        str02 = "%s" %y
        f3 = open("GUpiaoinfo.txt", 'ab+')
        f3.write(str02)
        f3.close()


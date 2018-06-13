#encoding=utf-8
import os
import collections
# print (os.getcwd())
f1_path = 'C:\\Users\\Administrator\\gitcode\\python-spider\\spider_gh\\Stock.txt'
f2_path = 'C:\\Users\\Administrator\\gitcode\\python-spider\\spider_gh\\final.txt'

name_list = []
dict_01 = {}
#将数据读取出来进行统计并排序
f1 = open(f1_path, 'ab+' )
lines = f1.readlines()
for i in lines:
    name_list.append( i )
f1.close()
d = collections.Counter( name_list )
s=sorted(d.items(),key = lambda x:x[1],reverse = True)
for a in s:
    str002 = '%d %s'%(a[1],a[0])
    f2 = open(f2_path,'ab+')
    f2.write(str002)
f2.close()
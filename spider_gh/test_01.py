#encoding=utf-8
import os
import collections
# print (os.getcwd())
f1_path =  'C:\\Users\\Administrator\\PycharmProjects\\spider_gh\\Stock.txt'
f2_path = 'C:\\Users\\Administrator\\PycharmProjects\\spider_gh\\final.txt'
name_list = []
f1 = open(f1_path, 'ab+' )
lines = f1.readlines()
for i in lines:
    name_list.append( i )
f1.close()
d = collections.Counter( name_list )
for k in d:
   str001 = '%d apper %s'%(d[k],k)
   f2 = open(f2_path,'ab+')
   f2.write(str001)
f2.close()
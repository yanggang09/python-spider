#coding=utf-8
import os
file_path = "C:\\Users\\Administrator\\PycharmProjects\\spider_gh\\Name.txt"
f2_path = 'C:\\Users\\Administrator\\PycharmProjects\\spider_gh\\final.txt'


UN01 = '\u4e09\u4e25\u4e09\u5b9e'#三严三实
UN02= '\u62db\u725b\u8fdb\u5b9d'#招牛进宝
UN03='\u957f\u7a7a\u98de\u96ea'#长空飞雪
UN04 = 'maosc01'
UN05= 'cyq_3'
UN06= '\u6f58\u524d\u8c79'#潘前豹
UN07='\u98de\u9ec4\u817e\u8fbe'#飞黄腾达
UN08='\u5929\u8d4b\u95f2\u8361'#天赋闲荡
UN09='\u9ec4\u8fde\u7d20'#黄连素
UN10='\u98ce\u54e5\u0030\u0030\u0031'#风哥001
list_00 = [UN01,UN02,UN03,UN04,UN05,UN06,UN07,UN08,UN09,UN10]
name_00 = ['三严三实','招牛进宝','长空飞雪','maosc01','cyq_3','潘前豹','飞黄腾达','天赋闲荡','黄连素','风哥001']
list_01 = []

#把所取到的数据按行取出以字典的形式存入列表
f01 = open(file_path,'ab+')
lines = f01.readlines()
for i in lines:
    dict_01 = {}
    # print i.split()[0]
    dict_01[i.split()[0]] = i.split()[1]
    # print dict_01
    list_01.append(dict_01)
#把列表中每个字典元素value对应的多个key取出存入字典
def writeData(name01,forcaster):
    for a in list_01:
        list_02.append(a.get(forcaster,'0'))

    for c in list_02:
        if c!='0':
            list_03.append(c)

    str001 = "%s 预报了 %s \n"%(name01 ,"\t".join(list_03))
    f1=open(f2_path,'ab+')
    f1.write(str001)
    f1.close()
if __name__ == "__main__":
    for a,b in zip(name_00,list_00):
        list_02 = []
        list_03 = []
        writeData(a,b)

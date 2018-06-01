#coding=utf-8
import os
import sys
import shutil

file_path = os.getcwd()
name = raw_input(u"请输入要创建文件夹名称：")
file_path02 = file_path + '\\' + 'Data' + name
os.mkdir(file_path02)
def movefile(filename):
    file_path03 = file_path02  + '\\' + filename
    shutil.copyfile(filename,file_path03)
    os.remove(filename)

if __name__ == "__main__":
    movefile('Name.txt')
    movefile('final.txt')
    movefile('Stock.txt')
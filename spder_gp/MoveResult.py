#coding=utf-8
import os
import sys
import shutil
import time

file_path = os.getcwd()
name = time.strftime("%Y%m%d%H",time.localtime(time.time()))
file_path02 = file_path + '\\' + 'Data' + name
os.mkdir(file_path02)
def movefile(filename):
    file_path03 = file_path02  + '\\' + filename
    shutil.copyfile(filename,file_path03)
    os.remove(filename)

if __name__ == "__main__":
    movefile('GUpiaoinfo.txt')
    movefile('GUpiaoinfo01.txt')

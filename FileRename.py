# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:30:23 2019
Windows10 + Anaconda python3.6 Tested Pass.
@author: feng_xiaosai
"""
#import sys
import os
###############################################################################
# filepath：需要修改文件的路径
filepath = (r"E:\无人机图片")
# 名称变量
cnt = 1
prename = "0100000" # 六位序列
###############################################################################

fileList = os.listdir(filepath) # 获取目标文件夹下所有文件
#print("修改前：" + str(fileList)) # 输出此文件夹中包含的文件名称
currentpath = os.getcwd() # 得到进程当前工作目录
os.chdir(filepath) # 将当前工作目录修改为待修改文件夹的位置
# 遍历文件夹中所有文件
for fileName in fileList:
    
    #生成新文件名。 fileName[-4:]:后缀名
    newname = prename[0:len(prename)-len(str(cnt))] + str(cnt) + fileName[-4:]
    #newname = fileName.replace("京", "I1") # replace(old,new)
    #newname = fileName[13:18] + fileName[-4:]
    print(str(fileName) + "======>" + newname)
    os.rename(fileName, newname) # 执行文件重新命名
    # 改变编号，继续下一项
    cnt = cnt + 1
print("******************重命名完成,共计修改" + str(cnt - 1) + "个文件*********************")
os.chdir(currentpath)# 改回程序运行前的工作目录
#sys.stdin.flush()# 刷新
# 输出修改后文件夹中包含的文件名称
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:30:23 2019
Windows10 + Anaconda python3.6 Tested Pass.
@author: feng_xiaosai
"""
#import sys
import os
from xml.etree.ElementTree import parse
###############################################################################
# filepath：需要修改文件的路径
filepath = (r"D:\数据集\无人机+飞机数据集\label\label")

###############################################################################

fileList = os.listdir(filepath) # 获取目标文件夹下所有文件
#print("修改前：" + str(fileList)) # 输出此文件夹中包含的文件名称
currentpath = os.getcwd() # 得到进程当前工作目录
os.chdir(filepath) # 将当前工作目录修改为待修改文件夹的位置
# 遍历文件夹中所有文件
for fileName in fileList:
    if '.xml' in fileName: # 只读取xml文件
        tree = parse(fileName) # 读取xml文件
        root = tree.getroot() # 解析xml文件
        
        tag_path_text = root.find('path', namespaces=None).text # 获取标签为path的内容
        new_tag_path_text = tag_path_text[-10:] # 取路径的六位序号和后缀名4位，即后10位
        new_tag_path_text = './' + new_tag_path_text
        root.find('path', namespaces=None).text = new_tag_path_text
        print('修改标签<path>:' + tag_path_text + '=====>' + new_tag_path_text)
        
        root.find('folder', namespaces=None).text = 'JPEGImages' # 修改folder为JPEGImages
        print('修改标签<folder>为:JPEGImages')
        
        tag_name_text = root.find('object').find('name').text
        new_tag_name_text = tag_name_text.replace(" ", "") # 去除name中的空格
        root.find('object').find('name').text = new_tag_name_text
        print('修改标签<name>:' + tag_name_text + '=====>' + new_tag_name_text)
        
        tree.write(fileName) # 保存
    else : # 跳过非xml文件
        pass
print("******************修改完成*********************")
os.chdir(currentpath)# 改回程序运行前的工作目录
#sys.stdin.flush()# 刷新
# 输出修改后文件夹中包含的文件名称
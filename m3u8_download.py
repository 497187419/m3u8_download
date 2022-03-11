#!/usr/bin/python
# coding=utf8
# coding:utf8
# -*- coding: UTF-8 -*-

from urllib.parse import urlparse,parse_qsl,unquote
from subprocess import call
import urllib.request
import requests
import hashlib
import base64
import json
import time
import re
import os

# 【脚本】直接解析m3u8并下载

# 根据unix或win，DS为\或/
DS = os.sep

# 定义缓存文件路径
runtime_path = os.getcwd() + DS + "runtime" + DS + "temp"

# 定义IDM地址
IDM = r'D:\Program Files\idman_lv\IDMan.exe'

m3u8_list = [
	'https://yun.66dm.net/SBDM/OusamaRanking21.m3u8'
]
output_filename = [
	'国王排名 第21集'
]
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
	'Connection':'close'
}

def download(url, save_name):
	download_path = os.getcwd() + DS + "download"
	if not os.path.exists(download_path):
		os.mkdir(download_path)
	# 获取M3U8的文件内容
	all_content = requests.get(url).text
	# 读取文件里的每一行
	file_line = all_content.split("\n")
	# 通过判断文件头来确定是否是M3U8文件
	if file_line[0] != "#EXTM3U":
		raise BaseException(u"非M3U8的链接")
	else:
		var_num = 0
		unknow = True   # 用来判断是否找到了下载的地址
		for index, line in enumerate(file_line):
			# print(index, line)
			if "EXTINF" in line:
				# 递增视频序号
				var_num = var_num + 1
				unknow = False
				# pd_url = 'https://gzmu.rondom.cn'+ file_line[index + 1]
				pd_url = file_line[index + 1]
				# print(pd_url)
				res = requests.get(url=pd_url, headers=headers, verify=False)
				# print(res)
				# os._exit(0)
				c_fule_name = str(var_num).rjust(4, "0")
				print('下载到 '+ download_path + DS + c_fule_name)
				with open(download_path + DS + c_fule_name, 'wb') as f:
					f.write(res.content)
					f.flush()
				# # 调用IDM执行下载
				# call([IDM, '/n','/d', pd_url, '/f', '..\\..\\phpStudy\\PHPTutorial\\WWW\\scan_tool_p\\download\\'+ c_fule_name])
				# os._exit(0)
		if unknow:
			raise BaseException("未找到对应的下载链接")
		else:
			print("下载完成")
			time.sleep(10)
			# 修改保存文件名
			save_name = save_name.replace("《", "").replace("》", "").replace(" ", "").replace("！", "").replace(":", "").replace("\\", "").replace("/", "").replace("：", "").replace("*", "").replace("？", "").replace("?", "").replace("|", "").replace("\"", "").replace("\"", "").replace("<", "").replace(">", "")+'.mp4'
			# cmd合并视频
			os.system(r"copy /b "+ download_path + DS +"*   "+ os.getcwd() + DS + save_name)
			time.sleep(5)
			# 删除原视频
			os.system("del /f /q /s "+ download_path + DS +"*.*")
			time.sleep(1)

# 定义IDM地址
IDM = r'D:/Program Files/idman_lv/IDMan.exe'

# 遍历list
for i, val in enumerate(m3u8_list):
	download(val, output_filename[i])
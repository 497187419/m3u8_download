#!/usr/bin/python
# coding=utf8
# coding:utf8
# -*- coding: UTF-8 -*-

import urllib.request
import requests
import time
import os

# 【脚本】直接解析m3u8文件并下载

file_path = 'demo.m3u8'

headers = {
	'Host':'yef.coderatian.top',
	'Connection':'keep-alive',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
	'Accept':'*/*',
	'Origin':'https://www.kelatv.com',
	'Sec-Fetch-Site':'cross-site',
	'Sec-Fetch-Mode':'cors',
	'Sec-Fetch-Dest':'empty',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
	'Referer':'https://www.kelatv.com/api/haliapi.php?v=a284w0fU5JH9HYrH1a2z1G5VDsnWMddP3Zp06hcIHScAkkbqtWIEXvnq6xfZj-bQE2wIyVoVw-2Wt2HKFjt4cz1ekG5gRw&name=noY&sign=dacf3238bc125e7cd74991d14580db56&time=1647239740'
}

with open(file_path, "r") as f:
	file_line = f.readlines()
	if file_line[0].strip('\n') != "#EXTM3U":
		print(u"非M3U8的链接")
		os._exit(0)
	else:
		var_num = 0
		unknow = True   # 用来判断是否找到了下载的地址
		for index, line in enumerate(file_line):
			if "EXTINF" in line:
				# 递增视频序号
				var_num = var_num + 1
				unknow = False
				pd_url = 'https://yef.coderatian.top'+ file_line[index + 1]
				# pd_url = file_line[index + 1]
				print(42, pd_url)
				res = requests.get(url=pd_url, headers=headers)
				c_fule_name = str(var_num).rjust(4, "0")
				print('下载到 '+ download_path + DS + c_fule_name)
				with open(download_path + DS + c_fule_name, 'wb') as f:
					f.write(res.content)
					f.flush()
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
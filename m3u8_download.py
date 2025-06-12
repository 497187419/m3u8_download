#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import os
import time
from typing import List
from tqdm import tqdm

class M3u8Downloader:
    def __init__(self):
        self.DS = os.sep
        self.download_path = os.path.join(os.getcwd(), "download")
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Connection': 'close'
        }
        self._init_folders()

    def _init_folders(self):
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)

    def download(self, url: str, save_name: str) -> bool:
        try:
            print(f"开始下载: {save_name}")
            content = self._get_m3u8_content(url)
            success = self._download_ts_files(content)
            if success:
                self._merge_and_cleanup(save_name)
            return success
        except Exception as e:
            print(f"下载失败: {str(e)}")
            return False

    def _get_m3u8_content(self, url: str) -> List[str]:
        response = requests.get(url=url, headers=self.headers, timeout=30)
        content = response.text.split("\n")
        if content[0] != "#EXTM3U":
            raise ValueError("非M3U8格式文件")
        return content

    def _download_ts_files(self, content: List[str]) -> bool:
        ts_urls = [line.strip() for i, line in enumerate(content) 
                  if "EXTINF" in content[i-1]]
        
        if not ts_urls:
            print("未找到视频片段")
            return False
            
        for i, url in enumerate(tqdm(ts_urls, desc="下载进度")):
            filename = str(i+1).rjust(4, "0")
            self._download_segment(url, filename)
        return True

    def _download_segment(self, url: str, filename: str):
        filepath = os.path.join(self.download_path, filename)
        try:
            response = requests.get(url=url, headers=self.headers, timeout=30)
            with open(filepath, 'wb') as f:
                f.write(response.content)
        except Exception as e:
            print(f"片段 {filename} 下载失败: {str(e)}")

    def _merge_and_cleanup(self, save_name: str):
        save_name = self._sanitize_filename(save_name) + '.mp4'
        output_path = os.path.join(os.getcwd(), save_name)
        
        print("正在合并视频片段...")
        os.system(f'copy /b "{self.download_path}{self.DS}*" "{output_path}"')
        time.sleep(2)
        
        print("清理临时文件...")
        os.system(f'del /f /q /s "{self.download_path}{self.DS}*.*"')

    @staticmethod
    def _sanitize_filename(filename: str) -> str:
        invalid_chars = ['《', '》', ' ', '！', ':', '\\', '/', '：', '*', '？', 
                        '?', '|', '"', '<', '>']
        for char in invalid_chars:
            filename = filename.replace(char, '')
        return filename

if __name__ == "__main__":
    m3u8_list = ['https://yun.66dm.net/SBDM/AinoUtagoewoKikasete.m3u8']
    output_filename = ['聆听爱的歌声吧']
    
    downloader = M3u8Downloader()
    for url, filename in zip(m3u8_list, output_filename):
        downloader.download(url, filename)
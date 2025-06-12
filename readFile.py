#!/usr/bin/python
# -*- coding: UTF-8 -*-

from m3u8_download import M3u8Downloader
import os
from urllib.parse import urljoin

class LocalM3u8Reader(M3u8Downloader):
    def __init__(self, file_path: str, base_url: str = ''):
        super().__init__()
        self.file_path = file_path
        self.base_url = base_url
        self.headers.update({
            'Host': 'yef.coderatian.top',
            'Origin': 'https://www.kelatv.com',
            'Accept': '*/*'
        })

    def process_file(self, save_name: str) -> bool:
        try:
            with open(self.file_path, "r") as f:
                content = [line.strip() for line in f.readlines()]

            if not content or content[0] != "#EXTM3U":
                print("无效的M3U8文件")
                return False

            # 处理ts文件URL
            ts_urls = []
            for i, line in enumerate(content):
                if "EXTINF" in line and i + 1 < len(content):
                    url = content[i + 1]
                    if self.base_url:
                        url = urljoin(self.base_url, url)
                    ts_urls.append(url)

            if not ts_urls:
                print("未找到视频片段")
                return False

            for i, url in enumerate(ts_urls):
                self._download_segment(url, str(i+1).rjust(4, "0"))

            self._merge_and_cleanup(save_name)
            return True

        except Exception as e:
            print(f"处理失败: {str(e)}")
            return False

if __name__ == "__main__":
    reader = LocalM3u8Reader('demo.m3u8', 'https://yef.coderatian.top')
    reader.process_file('测试视频')
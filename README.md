# m3u8视频下载脚本
Python下载m3u8，支持调用IDMan批量下载，但某些含重定向的请求建议使用原生requests；针对有重定向和指定格式的连接，支持header定义；

## 使用
  - m3u8_list 内填写m3u8地址
  - output_filename 内填写视频名称
  - 执行 python m3u8_download.py
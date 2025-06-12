# M3U8视频下载工具

一个简单高效的M3U8视频下载工具，支持在线链接和本地文件解析下载。

## ✨ 特性

- 🚀 支持在线M3U8链接下载
- 📁 支持本地M3U8文件解析
- 🔄 自动合并视频片段
- 🎯 断点续传支持
- 🛠 可自定义请求头
- 📦 支持批量下载任务

## 🔧 安装要求

- Python 3.6+
- requests
- tqdm (进度条显示)

```bash
pip install requests tqdm
```

## 📖 使用说明

### 在线M3U8下载

```python
from m3u8_download import M3u8Downloader

# 创建下载器实例
downloader = M3u8Downloader()

# 设置下载任务
m3u8_url = 'https://example.com/video.m3u8'
save_name = '视频名称'

# 开始下载
downloader.download(m3u8_url, save_name)
```

### 本地M3U8文件解析

```python
from readFile import LocalM3u8Reader

# 创建本地文件解析器
reader = LocalM3u8Reader('your_file.m3u8', 'https://base.url')

# 开始解析下载
reader.process_file('视频名称')
```

## ⚙️ 配置项

```python
# 自定义请求头
headers = {
    'User-Agent': 'Your User Agent',
    'Referer': 'Your Referer',
    # ...其他请求头
}
downloader.headers.update(headers)
```

## 📌 注意事项

- 下载文件将保存在 `download` 目录
- 视频片段自动合并为MP4格式
- 支持自动清理临时文件
- 异常处理确保下载稳定性

## 🔒 异常处理

- 自动重试失败的片段下载
- 详细的错误日志输出
- 网络异常自动恢复

## 📝 示例

```python
# 批量下载示例
m3u8_list = [
    'https://example1.com/video1.m3u8',
    'https://example2.com/video2.m3u8'
]
output_names = ['视频1', '视频2']

downloader = M3u8Downloader()
for url, name in zip(m3u8_list, output_names):
    downloader.download(url, name)
```

## 📅 更新日志

- 添加进度条显示
- 优化文件合并逻辑
- 增加异常处理机制
# 模板字符串

str = 'hello world'
f'{str}'

# 利用 requirements.txt 文件来安装所依赖的三方库

pip install -r requirements.txt

## requirement.txt 文件的生成方式

推荐使用：
安装
pip install pipreqs
在当前目录生成
pipreqs . --encoding=utf8 --force

# requests 库的基本使用

import requests
requests.get(url,headers=header)

# bs4 库的基本使用

from bs4 import BeautifulSoup as bs
soup = bs(response.text, 'html.parser')
soup.find_all('div', {"class": "movie-hover-info"})
soup.find() ...

# lxml 库的基本使用

from lxml import etree
html = etree.HTML(response.text)
dls = html.xpath('//\*/dd')
// 绝对路径
./ 相对路径
@ 拿到相应的属性
/text() 拿到文本

# pandas 库的基本使用

import pandas as pd
df = dp.DataFrame(list)
df.to_csv(url) ...

# scrapy 框架

重要的几个文件，以自己的作业二为例：
maoyanspider.py start_requests parse
items.py  
pipelines.py **init** process_item close_spider

# scrapy 项目在 vscode 中的断点调试

launch.json
{
"version": "0.2.0",
"configurations": [
{
"name": "Python: 当前文件",
"type": "python",
"request": "launch",
"program": "${file}",
      "console": "integratedTerminal"
    },
    {
      "name": "MaoyanScrapy",
      "type": "python",
      "request": "launch",
      "module": "scrapy",
      "args": ["crawl", "maoyanspider"],
      // 切换到指定的目录下的 默认的直接是工作区的
      "cwd": "${workspaceFolder}/zy2/spiders"
}
]
}

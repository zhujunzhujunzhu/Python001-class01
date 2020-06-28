'''
@Description 
@Autor 朱俊
@Date 2020-06-27 18:03:11
@LastEditors 朱俊
@LastEditTime 2020-06-27 18:27:51
'''
# from scrapy.cmdline import execute
# import sys
# import os
# # 获取当前脚本路径
# dirpath = os.path.dirname(os.path.abspath(__file__))
# # 切换到scrapy项目路径下
# os.chdir(dirpath[:dirpath.rindex("\\")])
# # 启动爬虫,第三个参数为爬虫name
# execute(['scrapy', 'crawl', 'movies'])

from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "moives"])

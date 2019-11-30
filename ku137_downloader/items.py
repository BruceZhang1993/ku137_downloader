# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Ku137ResourceItem(scrapy.Item):
    name = scrapy.Field()       # 标题
    category = scrapy.Field()   # 标签分类
    from_uri = scrapy.Field()   # 来源页
    files = scrapy.Field()      # 文件
    file_urls = scrapy.Field()  # 下载链接

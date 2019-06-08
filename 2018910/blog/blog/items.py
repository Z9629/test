# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class BlogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # Title = Field()  # 标题
    Name = Field()  # 作者
    # # data = Field()      #发布日期
    # num = Field()  # 阅读量

    # path = Field()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class BossItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

#items定义要爬取的字段
class BossItem(scrapy.Item):
    # job_title = scrapy.Field()  #岗位
    # compensation = scrapy.Field()   #薪资
    # company = scrapy.Field()    #公司
    # address = scrapy.Field()    #地址
    # seniority = scrapy.Field()  #工作年薪
    # education = scrapy.Field()  #教育程度
    # company_type = scrapy.Field()   #公司类型
    # company_finance = scrapy.Field()    #融资
    # company_quorum = scrapy.Field() #公司人数

    name = scrapy.Field()   #公司名
    title = scrapy.Field()  #岗位名
    wage = scrapy.Field()   #工资
    site = scrapy.Field()   #地点

# # -*- coding: utf-8 -*-
#
# # Define here the models for your scraped items
# #
# # See documentation in:
# # https://doc.scrapy.org/en/latest/topics/items.html
#
# import scrapy
# import urlparse
#
# #慕课网爬取
# class ImoocSpider(scrapy.Spider):
#     #spider的名字定义了Scrapy如何定位（并初始化）spider，所以其必须是唯一的；
#     name = "imooc"
#
#     #url列表
#     start_urls = ['http://www.imooc.com/course/list']
#     #域名不在列表中的url不会被爬取
#     allowed_domains = ['www.imooc.com']
#
#     def parse(self, response):
#         learn_nodes = response.css('a.course-card')
#         for learn_node in learn_nodes:
#             learn_url = learn_node.css("::attr(href)").extract_first()
#             yield scrapy.Request(url=urlparse.urljoin(response.url,learn_url),callback=self.parse_learn)
#     def parse_learn(self,response):
#         title = response.xpath('//h2[@class="1"]/text()').extract_first()
#         content = response.xpath('//div[@class="course-brief"]/p/text()').extract_first()
#         url = response.url
#         print('标题：' + title)
#         print('地址：' + url)
#
# # class ScrapydemoItem(scrapy.Item):
# #     # define the fields for your item here like:
# #     # name = scrapy.Field()
# #     pass
#############################
from scrapy import Item,Field
class ImoocItem(Item):
    Course_name = Field()  # 课程名称

    Course_content = Field()  # 课程内容

    Course_level = Field()  # 课程等级

    Course_attendance = Field()  # 课程学习人数
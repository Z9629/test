# # -*- coding: utf-8 -*-
#
# # Define here the models for your scraped items
# #
# # See documentation in:
# # https://doc.scrapy.org/en/latest/topics/items.html
#
# import scrapy
# import urlparse
# #
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
###############################
# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
# from scrapy.items import ImoocItem
from scrapy.
from scrapy.http import Request


class Imooc(CrawlSpider):
    name='imooc'
    allowed_domains = ['imooc.com']
    start_urls = []
    for pn in range(1,31):
        url = 'http://www.imooc.com/course/list?page=%s' % pn
        start_urls.append(url)

    def parse(self,response):
        item=ImoocItem()
        selector=Selector(response)
        Course = selector.xpath('//a[@class="course-card"]')

        for eachCourse in Course:
            Course_name = eachCourse.xpath('div[@class="course-card-content"]/h3[@class="course-card-name"]/text()').extract()[0]
            Course_content = eachCourse.xpath('div[@class="course-card-content"]/div[@class="clearfix course-card-bottom"]/p[@class="course-card-desc"]/text()').extract()
            Course_level = eachCourse.xpath('div[@class="course-card-content"]/div[@class="clearfix course-card-bottom"]/div[@class="course-card-info"]/span/text()').extract()[0]
            Course_attendance = eachCourse.xpath('div[@class="course-card-content"]/div[@class="clearfix course-card-bottom"]/div[@class="course-card-info"]/span/text()').extract()[1]
            item['Course_name'] = Course_name
            item['Course_content'] = ';'.join(Course_content)
            item['Course_level'] = Course_level
            item['Course_attendance'] = Course_attendance
            yield item
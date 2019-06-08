# -*- coding: utf-8 -*-
import scrapy
# from items.py import BossItem
from boss.items import BossItem

# class BossZhipinSpider(scrapy.Spider):
#     name = 'boss_zhipin'
#     allowed_domains = ['zhipin.com']
#     start_urls = ['http://zhipin.com/']
#
#     def parse(self, response):
#         pass

class ZhipinSpider(scrapy.Spider):
    #定义spider的名字
    name = 'job'
    #定义爬取的域
    allowed_domains = ['www.zhipin.com']
    #定义入口url
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&scity=101010100&industry=&position=']
    #定义解析规则,这个方法必须叫parse
    def parse(self, response):
        # item = BossItem()
        body = response.css(".job-primary")
        for head in body:
            item = BossItem()
            item["title"] = head.css(".job-title::text").extract()[0]
            item["wage"] = head.css(".red::text").extract()[0]
            item["site"] = head.css(".info-primary p::text").extract_first().strip()
            item["name"] = head.css(".company-text .name a::text").extract_first()
            yield item
        #翻页
        next_page = response.css(".page .next::attr(href").extract()[0]
        if next_page is not None:
            yield response.follow('https://www.zhipin.com'+next_page,callback=self.parse)
            #链接不完全，需要补充






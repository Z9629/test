# import requests
# import json
# url = 'https://www.baidu.com'
# r = requests.post(url)
# # print(r.text)
# # print(r.encoding)
# r.encoding='utf-8'
# print(r.text.replace('&nbsp',' '))
# print(r.headers)
#
# # #------------
# # from bs4 import BeautifulSoup
# #
# # #-----------------
# # # import scrapy
# # # #引入容器
# # # from scrapytest.CourseItems import CourseItem
# # #
# # # class MySpider(scrapy.Spider):
# # #     #设置name
# # #     name = "MySpider"
# # #     #设定域名
# # #     allowed_domains = ["imooc.com"]
# # #     #填写爬取地址
# # #     start_urls = ["http://www.imooc.com/course/list"]
# # #     #编写爬取方法
# # #     def parse(self, response):
# # #         #实例一个容器保存爬取的信息
# # #         item = CourseItem()
# # #         #这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
# # #         #先获取每个课程的div
# # #         for box in response.xpath('//div[@class="moco-course-wrap"]/a[@target="_self"]'):
# # #             #获取每个div中的课程路径
# # #             item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
# # #             #获取div中的课程标题
# # #             item['title'] = box.xpath('.//img/@alt').extract()[0].strip()
# # #             #获取div中的标题图片地址
# # #             item['image_url'] = box.xpath('.//@src').extract()[0]
# # #             #获取div中的学生人数
# # #             item['student'] = box.xpath('.//span/text()').extract()[0].strip()[:-3]
# # #             #获取div中的课程简介
# # #             item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
# # #             #返回信息
# # #             yield item
# #
# # #---------------------------
# #
# # import re
# # import sys
# # from bs4 import BeautifulSoup
# # import urllib.request
# # import time
# #
# # headers = ('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1')
# # opener = urllib.request.build_opener()
# # opener.addheaders = {headers}
# # urllib.request.install_opener(opener)
# #
# #
# # def get_download(url):
# #     file = urllib.request.urlopen(url)
# #     data = BeautifulSoup(file, from_encoding="utf8")
# #     section_name = data.title.string
# #     section_text = data.select('#bgdiv .border_l_r #content p')[0].text
# #     section_text = re.sub('\s+', '\r\n\t', section_text).strip('\r\n')
# #     fp = open('2.txt', 'a')
# #     fp.write(section_name + "\n")
# #     fp.write(section_text + "\n")
# #     fp.close()
# #     pt_nexturl = 'var next_page = "(.*?)"'
# #     nexturl_num = re.compile(pt_nexturl).findall(str(data))
# #     nexturl_num = nexturl_num[0]
# #     return nexturl_num
# #
# #
# # if __name__ == '__main__':
# #     url = "http://www.lewendu8.com/books/21/21335/6381842.html"
# #     num = 228
# #     index = 1
# #     get_download(url)
# #     while (True):
# #         nexturl = get_download(url)
# #         index += 1
# #         sys.stdout.write("已下载:%.3f%%" % float(index / num * 100) + '\n')
# #         sys.stdout.flush()
# #         url = "http://www.lewendu8.com/books/21/21335/" + nexturl
# #         if (nexturl == 'http://www.lewendu8.com/books/21/21335/'):
# #             break
# #     print(time.clock())


##################
print "hello"

#encoding=utf8
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from blog.items import BlogItem


class Blog(CrawlSpider):
    name = 'blog'
    allowed_domains = ['cnblogs.com']
    start_urls = []
    for pn in range(1,31):
        url = 'https://www.cnblogs.com/#p%s' % pn
        start_urls.append(url)

    def parse(self, response):
        item = BlogItem()
        selector = Selector(response)
        Course = selector.xpath('//div[@class="post_item_body"]')

        for eachCourse in Course:
            # Title = eachCourse.xpath('h3/a[@class="titlelnk"]/text()').extract()
            # Name = eachCourse.xpath('div[@class="post_item_foot"]/a[@class="lightblue"]/text()').extract()[0]
            # path1 = eachCourse.xpath('p[@class="post_item_summary"]/a/img/@src').extract()[0]
            # [ @

            # class ="pfs"]
            # path = "http:" + path1
            Name = eachCourse.xpath('div[@class="post_item_foot"]/a["@class=lightblue"]/text()').extract()[0]
            #
            # # data = eachCourse.xpath()
            # num = eachCourse.xpath('span[@class="article_view"]/a["@class="gray"]/text()').extract()

            # item['Title'] = Title
            item['Name'] = Name
            # item['path'] = path
            # item['num'] = num
            yield item

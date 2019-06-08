# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


# class BossPipeline(object):
#     def process_item(self, item, spider):
#         return item

class BossPipeline(object):
    def process_item(self, item, spider):
        # return item
        self.cursor.execute(
            '''insert into pachong(name,title,site,wage) 
            values(%s,%s,%s,%s)''',
            # 将item['name'],item['title'],item['site'],item['wage']数据插入表51job中，注意，必须相对应
            (item['name'], item['title'], item['site'], item['wage'])
        )
        #提交sql语句
        self.connect.commit()
        return item
    def __init__(self):
        #连接数据库·
        self.connect = pymysql.connect(
            host = 'localhost',  #数据库地址
            port = 3306,         #数据库端口
            db = 'bosszhipin',         #数据库名
            user = 'root',         #用户名
            passwd = 123456,         #密码
            charset = 'utf8',         #编码方式，如果不注意可能会乱码
            use_unicode = True,

        )
        #通过cursor执行增删改查
        self.cursor = self.connect.cursor()

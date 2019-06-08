# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import copy
import pymysql
import pymysql.cursors
from scrapy import log
from twisted.enterprise import adbapi


class BlogPipeline(object):
    def __init__(self):
        self.file = codecs.open('blog.json','w',encoding='utf-8')


    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False)+ "\n"
        self.file.write(line)
        return item
    def spider_closed(self,spider):
        self.file.close()

class MysqlPip(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool("pymysql",
                                            db = "blogyuan",
                                            user = "root",
                                            passwd = "123456",
                                            cursorclass = pymysql.cursors.DictCursor,
                                            charset = "utf8",
                                            use_unicode = True)
    def process_item(self,item,spider):
        asItem = copy.deepcopy(item)
        query = self.dbpool.runInteraction(self._conditional_insert,asItem)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self,tb,item):
        # tb.execute("""insert into test( title,Name,num) values(%s,%s,%s) """,(item['Title'],item['Name'],item['num']))
        # tb.execute("""insert into test3( Name,path ) values(%s,%s) """,(item['Name'],item['path']))
        tb.execute("""insert into test4( Name ) values(%s) """,(item['Name']))

        log.msg("Item data in db : %s" % item,level=log.DEBUG)

    def handle_error(self,e):
        log.err(e)


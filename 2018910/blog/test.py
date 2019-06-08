# # !/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time    : 2017/8/18 11:37
# # @File    : Picture.py
# import pymysql as mysql
# import sys
#
# conn = mysql.connect(host='localhost', user='root', passwd='123456', db='blogyuan')
#
# fp = open(r"C:\Users\14813\Pictures\Camera Roll\f.png")
# img = fp.read()
# fp.close()
#
#
# # 存入图片
# def insert_imgs(img):
#     # mysql连接
#
#     cursor = conn.cursor()
#     # 注意使用Binary()函数来指定存储的是二进制
#     # cursor.execute("insert into img set imgs='%s'" % mysql.Binary(img))
#     cursor.execute("Insert into test2(name,img) values(%s,%s)", ('sdf',mysql.Binary(img)))
#     # 如果数据库没有设置自动提交，这里要提交一下
#     conn.commit()
#     cursor.close()
#     # 关闭数据库连接
#     conn.close()
#
#
# # 提取图片
# def select_imgs(img):
#     cursor = conn.cursor()
#     cursor.execute('select img from img')
#     print cursor.fetchall()
#     cursor.close()
#     conn.close()
#
# if __name__ == '__main__':
#     conn = mysql.connect(host='localhost', user='root', passwd='123456', db='blogyuan')
#
#     fp = open(r"C:\Users\14813\Pictures\Camera Roll\f.png")
#     img = fp.read()
#     fp.close()
#     insert_imgs(img)
#     select_imgs(img)


# !/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql as mysql
import sys

try:
    # 读取图片文件
    fp = open(r"C:\Users\14813\Pictures\Camera Roll\f.png")
    img = fp.read()
    fp.close()
except IOError, e:
    print "Error %d %s" % (e.args[0], e.args[1])
    sys.exit(1)
try:
    # mysql连接
    conn = mysql.connect(host='localhost', user='root', passwd='123456', db='blogyuan')
    cursor = conn.cursor()
    # 注意使用Binary()函数来指定存储的是二进制
    cursor.execute("INSERT INTO test2 SET data='%s'" % mysql.Binary(img))
    # 如果数据库没有设置自动提交，这里要提交一下
    conn.commit()
    cursor.close()
    # 关闭数据库连接
    conn.close()
except mysql.Error, e:
    print "Error %d %s" % (e.args[0], e.args[1])
    sys.exit(1)
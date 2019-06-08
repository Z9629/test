#-*- coding: UTF-8 -*-

# #PUT一个请求
# import urllib.request
# DATA=b'some data'
# req = urllib.request.Request(url='http://localhost:8080', data=DATA,method='PUT')
# with urllib.request.urlopen(req) as f:
#     pass
#     print(f.status)
#     print(f.reason)
#
#
#-*- coding: UTF-8 -*-
import urllib2,urllib
import json
request = urllib2.Request('http://www.cnblogs.com/huangxie/p/5476812.html')

# response = urllib2.urlopen(request)
# req = urllib.urlencode('utf-8')
# print(req.encode())
# print(request.read())

req = urllib2.urlopen(request)
data = req.read()
data = data.decode('utf-8')
print(data)
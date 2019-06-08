#-*- coding: UTF-8 -*-

# import urllib2,urllib,re
# url = 'https://www.baidu.com'
# User_Agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
# headers = {'User_Agent': User_Agent}
# request = urllib2.Request(url,headers)
# # print(requests)
# respons = urllib2.urlopen(request)
# # html = response.read()
# print(respons.read())


import urllib2
import urllib
import re

url = "http://www.baidu.com/"
User_Agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"


headers = {'User_Agent': User_Agent}
req = urllib2.Request(url, headers=headers)
getdata = urllib2.urlopen(req)
gd = getdata.read()

# g = urllib.urlencode(getdata)
g = gd.decode('utf-8')
# print(g)


def get(html):
    reg = r'src="(.*?\.png)"'
    data = re.findall(reg, g)
    x = 0
    for i in data:
        urllib.urlretrieve(i, '%s.jpg' % x)
        x += 1


s = get(getdata)

print(s)
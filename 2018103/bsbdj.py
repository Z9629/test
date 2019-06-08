# -*- coding:utf-8 -*-
import re ,urllib,urllib2

def getVedio(page):
    req = urllib2.Request('http://www.budejie.com/%s' % page)#
    req.add_header("User-Agent"," Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
    html = urllib2.urlopen(req).read()
    # reg = r'img src="(.*?)"' #正则表达式匹配
    reg = r'http://.*?.gif' #正则表达式匹配
    for i in re.findall(reg,html):
        filename = i.split("/")[-1] #分割i内容并取最后一部分
        print(filename)
        print("正在下载%s" % filename)
        urllib.urlretrieve(i,"mp4/%s" %filename)#下载
if __name__ == '__main__':
    for i in range(10):
        getVedio(i)


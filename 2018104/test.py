# #PUT一个请求
# import urllib.request
# DATA=b'some data'
# req = urllib.request.Request(url='http://127.0.0.1:8000', data=DATA,method='PUT')
# with urllib.request.urlopen(req) as f:
#     pass
#     print(f.status)
#     print(f.reason)
#
#


import requests
import json

url = 'http://music.163.com/api/song/lyric?'+ 'id=' + str(27566765)+ '&lv=1&kv=1&tv=-1'
r = requests.get(url)
json_obj = r.text

j = json.loads(json_obj)
print(j['lrc']['lyric'])



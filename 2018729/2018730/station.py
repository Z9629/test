import re
import json
import requests

def store(data):
    with open('station_code.json','w') as f:
        f.write(json.dumps(data))


header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9025'
res = requests.get(url,headers=header,verify=False)
stations_text = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',res.text)
stations = dict(stations_text)

if __name__ == '__main__':
    store(stations)
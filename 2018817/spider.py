import requests
from requests.exceptions import RequestException
import re
import json
def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None
def parse_one_page(html):
    pattern = re.compile('<div.*?class.*?><ul',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5].strip()[6:]

        }
    # print(items)
def write_to_file(content):
    with open('result.txt','a') as f:
        f.write(json.dumps(content) + '\n')
        f.close()
def main():
    url = 'http://www.jntv8.com/dsj_hot.asp?ToPage=4&id=8'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
if __name__ == '__main__':
    main()
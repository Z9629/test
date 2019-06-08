import re
import requests
def main():
    url = 'http://www.jntv8.com/dsj_hot.asp?ToPage=4&id=8'
    response = requests.get(url)
    print(response.text)
    s = str(response.text)
    with open('a.txt','a') as c:
        c.write(str(s).encode())
        c.close()
if __name__ == '__main__':
    main()
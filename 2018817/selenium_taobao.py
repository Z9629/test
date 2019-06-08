# import re
#
# from pyquery import PyQuery as pq
# from config2 import *
# import pymongo
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# client = pymongo.MongoClient(MONGO_URL)
# db = client[MONGO_DB]
# # browser = webdriver.Chrome()
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
# wait = WebDriverWait(browser,10)
#
# browser.set_window_size(1400,900)
#
# def search():
#     print('正在搜索')
#     try:
#         browser.get('https://www.taobao.com')
#         input = wait.until(
#             EC.presence_of_element_located((By.CSS_SELECTOR,'#q'))
#         )
#         submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_SearchForm > button')))
#         input.send_keys('美食')
#         submit.click()
#         total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
#         return total.text
#     except TimeoutException:
#         return search()
# def next_page(page_number):
#
# def main():
#     search()
#
# if __name__ == '__main__':
#     main()
#


#---------------------------
import re
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config2 import *
import pymongo

#MogoDB配置
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

#创建WebDriver对象
browser = webdriver.Chrome()
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS,executable_path=r'C:\Users\14813\DesktopC:\Users\14813\Desktop\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

#等待变量
wait = WebDriverWait(browser,10)

#模拟搜索美食
def search():
    try:
        browser.get('https://www.taobao.com/')#打开淘宝首页
        tb_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )#等待输入框加载完成
        search_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button'))
        )#等待搜索按钮加载完成
        tb_input.send_keys('美食')#输入框中传入“美食”
        search_btn.click()#点击搜索
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total'))
        )#加载完成，获取页数元素
        get_products()
        return total.text#获取元素中的文本
    except TimeoutException:
        return search()#若发生异常，重新调用自己

#翻页函数
def next_page(page_number):
    try:
        page_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )#等待翻页输入框加载完成
        confirm_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit'))
        )#等待确认按钮加载完成
        page_input.clear()#清空翻页输入框
        page_input.send_keys(page_number)#传入页数
        confirm_btn.click()#确认点击翻页
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number))
        )#确认已翻到page_number页
        get_products()
    except TimeoutException:
        next_page(page_number)#若发生异常，重新调用自己

#获取商品信息
def get_products():
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item'))
    )#等待商品信息加载完成，商品信息的CSS选择器分析HTML源码得到
    html = browser.page_source#得到页面HTML源码
    doc = pq(html)#创建PyQuery对象
    items = doc('#mainsrp-itemlist .items .item').items()#获取当前页所有商品信息的html源码
    for item in items:
        product = {
            'image':item.find('.pic .img').attr('src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        print(product)
        save_to_mongoDB(product)#保存到MongoDB

#保存到MongoDB
def save_to_mongoDB(product):
    try:
        if db[MONGO_TABLE].insert(product):
            print('存储到MongoDB成功',product)
    except Exception:
        print('存储到MongoDB失败',product)

def main():
    total = search()#获取商品页数，字符串类型
    total = int(re.compile('(\d+)').search(total).group(1))#利用正则表达式提取数字，并强制转换为int类型
    for i in range(2, total+1):
        next_page(i)
    browser.close()

if __name__ == '__main__':
    main()
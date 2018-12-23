from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pymongo
SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
MONGO_URL = 'localhost'
MONGO_DB = 'brief_introduction'
MONGO_TABLE = 'zyjm20181222'
browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
'''PhantomJS   '''
wait = WebDriverWait(browser, 10)
browser.set_window_size(1400, 900)

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def search(key):
    print("正在搜索")
    try:
        browser.get('http://www.zybus.com/')

        inp = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#j-searchTxt'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.head_top > div.search > div.form > form > input.btn')))

        '''submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#searchform > button')))'''
        inp.send_keys(key)

        submit.click()
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#jiemu > div > ul > li > div > a > img')))
        submit.click()
        content=browser.find_element_by_css_selector('body > div.list_toptxt > div:nth-child(4) > p')
        time=browser.find_element_by_css_selector('body > div.list_toptxt > ul > li:nth-child(2)')
        host=browser.find_element_by_css_selector('body > div.list_toptxt > ul > li:nth-child(1)')
        TV=browser.find_element_by_css_selector('body > div.list_toptxt > ul > li:nth-child(4)')
        update=browser.find_element_by_css_selector('body > div.list_toptxt > ul > li:nth-child(5)')
        area=browser.find_element_by_css_selector('body > div.list_toptxt > ul > li:nth-child(6)')
        type=browser.find_element_by_css_selector('body > div.list_toptxt > ul > li:nth-child(3)')
        print(content.text)
        zyjm_content = {
            'title': key,
            'content': content.text,
            'host':host.text,
            'time':time.text,
            'TV':TV.text,
            'update':update.text,
            'area':area.text,
            'type':type.text
        }
        save_to_mongo(zyjm_content)

    except TimeoutException:
        print(key+" 的简介获取失败")


def main():
    yljm=['娱乐百分百','大学生了没','命运好好玩','国光帮帮忙','美食好简单','爱玩客','WTO姐妹会','康熙来了','SS小燕之夜','2分之一强','来自星星的事','综艺大热门','别让身体不开心','女人我最大','上班这党事','美凤有约','风水有关系','旅行应援团','超级夜总会','冠军任务','天才冲冲冲'
        ,'综艺玩很大','疯神无双','综艺大集合','大陆寻奇','三星报喜'
        ,'MIT台湾志','疯狂开心果','宠物大联萌','天王猪哥秀'
        ,'美食凤味','小明星大跟班','请你跟我这样过','健康NO.1','食尚玩家','最美的歌']
    for i in range(0,len(yljm)):
        search(yljm[i])

def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('存储到MONGODB成功', result)
    except Exception:
        print('存储到MONGODB失败', result)


if __name__ == '__main__':
    main()

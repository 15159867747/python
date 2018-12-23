from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import pymongo

SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
MONGO_URL = 'localhost'
MONGO_DB = 'brief_introduction'
MONGO_TABLE = 'zyjmpf'
browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
'''PhantomJS   '''
wait = WebDriverWait(browser, 10)
browser.set_window_size(1400, 900)

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def search(key):
    print("正在搜索")
    try:
        browser.get('https://movie.douban.com/')

        inp = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#inp-query'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                        '#db-nav-movie > div.nav-wrap > div > div.nav-search > form > fieldset > div.inp-btn > input[type="submit"]')))

        '''submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#searchform > button')))'''
        inp.send_keys(key)

        submit.click()
        '''print(browser.page_source)'''
        url = re.search(
            '<div class="sc-dnqmqq.*?">.*?<div class="title".*?<a.*?class="title-text">.*?' + key + '.*?<span class="rating_nums">(.*?)</span>.*? class="pl">(.*?)</span>',
            browser.page_source, re.S)
        if url:

            pf = url.group(1)
            num = url.group(2)
        else:

            pf = "null"
            num = "null"

        douban_pf = {
            'title': key,
            'pf': pf,
            'num': num
        }
        save_to_mongo(douban_pf)

    except TimeoutException:
        print(key + " 的豆瓣评分获取失败")


def main():
    yljm = ['娱乐百分百', '大学生了没', '命运好好玩', '国光帮帮忙', '美食好简单', '爱玩客', 'WTO姐妹会', '康熙来了', 'SS小燕之夜', '2分之一强', '来自星星的事', '综艺大热门',
            '别让身体不开心', '女人我最大', '上班这党事', '美凤有约', '风水有关系', '旅行应援团', '超级夜总会', '冠军任务', '天才冲冲冲'
        , '综艺玩很大', '疯神无双', '综艺大集合', '大陆寻奇', '三星报喜'
        , 'MIT台湾志', '疯狂开心果', '宠物大联萌', '天王猪哥秀'
        , '美食凤味', '小明星大跟班', '请你跟我这样过', '健康NO.1', '食尚玩家', '最美的歌']
    '''search(yljm[0])'''
    for i in range(0, len(yljm)):
        search(yljm[i])
    browser.close()

def save_to_mongo(result):
    try:

        if db[MONGO_TABLE].insert(result):
            print('存储到MONGODB成功', result)
    except Exception:
        print('存储到MONGODB失败', result)


if __name__ == '__main__':
    main()

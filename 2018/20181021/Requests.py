import requests
from requests.exceptions import RequestException
import re


def get_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_url(html):


    pattern2 = re.compile('<dt>.*?href="(.*?)">(.*?)</a>.*?</td>', re.S)
    items = re.findall(pattern2, html)
    for item in items:
        yield{
            'title':item[0],
            'url' :item[1]
        }



def main():
    url = 'http://bbs.taiwan123.cn/'
    html = get_url(url)
    for item in parse_url(html):
        print(item)



if __name__ == '__main__':
    main()

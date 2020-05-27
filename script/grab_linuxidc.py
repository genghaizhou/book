import requests
import re
from bs4 import BeautifulSoup

domain = 'https://linux.linuxidc.com/'

# f = open('/home/work/data/liunxc.csv', 'w+')
f = open('~/Desktop/liunxc.csv', 'w+')

''' 
  抓取 linux公社 文档
  https://linux.linuxidc.com/index.php
'''

def getUrl(url):
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, 'lxml')
    tr_list = soup.find_all('tr', class_='folder_bg')

    d = []
    for tr in tr_list:
        uri = domain + tr.a['href']
        text = tr.a.text

        d.append([text, uri])
    return d

def printText(text, url):
    print(text, file=f, flush=True)
    print('   ' + url, file=f, flush=True)


def searchUrl(url):
    ds = getUrl(url)

    for d in ds:
        t, u = d

        temp = t.strip().replace(r' +', '')
        res = re.search(r'(\d+)|(\d+月)|(\d+日)', temp)

        print(t, url)

        # 查到则
        if res:
            searchUrl(u)
        else:
            printText(t, u)


if __name__ == "__main__":
    searchUrl(domain + "index.php")

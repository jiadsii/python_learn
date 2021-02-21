# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     11_阿里v站
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/21/21
"""
import requests

from bs4 import BeautifulSoup


def main():
    resp = requests.get('https://v.taobao.com/v/content/live?catetype=704&from=taonvlang')
    soup = BeautifulSoup(resp.text, 'lxml')
    for img_tag in soup.select('img[src]'):
        print(img_tag.attrs['src'])


if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     08_redis数据缓存
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/21/21
"""
import hashlib
import pickle
import re
import zlib
from urllib.parse import urljoin

import bs4
import redis
import requests


def main():
    base_url = 'https://www.zhihu.com/'
    seed_url = urljoin(base_url, 'explore')
    client = redis.Redis(host='1.2.3.4', port=6379, password='1qaz2wsx')
    headers = {'user-agent': 'Baiduspider'}
    resp = requests.get(seed_url, headers=headers)
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    href_regex = re.compile(r'^/question')
    for a_tag in soup.find_all('a', {'href': href_regex}):
        href = a_tag.attrs['href']
        full_url = urljoin(base_url, href)
        field_key = hashlib.sha1(full_url.encode()).hexdigest()
        if not client.hexists('spider:zhihu:explore', field_key):
            html_page = requests.get(full_url, headers=headers).text
            zipped_page = zlib.compress(pickle.dumps(html_page))
            client.hset('spider:zhihu:explore', field_key, zipped_page)
    print('Total %d question pages found.' % client.hlen('spider:zhihu:explore'))


if __name__ == '__main__':
    main()
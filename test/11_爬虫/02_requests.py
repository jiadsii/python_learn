# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     02_requests
   Description :
   email:         17334029932@163.com
   Author :       duweixiao
   date：          2/21/21
"""
import requests

resp = requests.get('http://www.baidu.com/index.html')
print(resp.status_code)
print(resp.headers)
print(resp.cookies)
print(resp.content.decode('utf-8'))

resp = requests.post('http://httpbin.org/post', data={'name': 'Hao', 'age': 40})
print(resp.text)
data = resp.json()
print(type(data))

resp = requests.get(
    url='https://movie.douban.com/top250',
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.97 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;'
                  'q=0.9,image/webp,image/apng,*/*;'
                  'q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
)
print(resp.status_code)

# resp = requests.post(
# 	url='http://httpbin.org/post',
#     files={'file': open('data.xlsx', 'rb')}
# )
# print(resp.text)


cookies = {'key1': 'value1', 'key2': 'value2'}
resp = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(resp.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
resp = requests.get('http://httpbin.org/cookies', cookies=jar)
print(resp.text)


requests.get('https://www.taobao.com', proxies={
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
})


requests.get('https://github.com', timeout=10)
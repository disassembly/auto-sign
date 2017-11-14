# -*- coding: utf-8 -*-
import requests
import re

cookies={
    'BAIDUID':'get your BAIDUID through firefox',
    'BDUSS': 'get your BDUSS through firefox'
    }
base_url = "https://www.baidu.com"
session = requests.session()
session.cookies.update(cookies)
session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
res = session.get(base_url)
match = re.search("=user-name>(.+?)<", res.text)
if match:
    print("Login:",match.group(1))
res = session.get("http://tieba.baidu.com/mo/")
likes_url = "http://tieba.baidu.com" + re.search('"([^"]+tab=favorite)"', res.text).group(1).replace("&amp;", "&")
res = session.get(likes_url)
likes = re.findall('kw.+?">(.+?)<', res.text)
print(likes)
for name in likes:
    res = session.get("http://tieba.baidu.com/mo/m?kw=" + name)
    if "已签到" in res.text:
        print("Already signed in", name)
    else:
        tieba_url = "http://tieba.baidu.com/mo/m?kw=" + name
        res = session.get(tieba_url)
        match = re.search('(/mo/q[^<]+?)">签到', res.text)
        if match:
            sign_url = "http://tieba.baidu.com" + match.group(1)
            sign_url = sign_url.replace("&amp;", "&")
            res = session.get(sign_url)
        if "已签到" in res.text:
            print("Signed successfully in", name)
        else:
            print("Fail to sign in", name)

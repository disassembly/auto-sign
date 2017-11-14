#!/usr/bin/python3
#-*-coding:utf8-*-
import re
import requests
import time
import json
import sys

login_url="https://forum.51nb.com/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&inajax=1"
postdata = {
          'username':"Your username",
          'password':"password get it in firefox,crypted with md5",
          'questionid':3,#安全问题设置
          'answer':"xxx".encode('gbk'),#问题回答,如果是中文,要以gbk编码
           }
#以上postdata请问firefox开发者工具获取
headers = {
	'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:54.0) Gecko/20100101 Firefox/54.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding':'gzip, deflate,br',
	'Content-Type':'text/html;charset=gbk',
	'Content-Encoding':'gzip',
	'Connection':'keep-alive',
	
	  }
session=requests.Session()
r=session.post(login_url,data=postdata)
print(r.text)
sign_url ="https://forum.51nb.com/plugin.php?id=dsu_paulsign:sign"
qiandao_url ="https://forum.51nb.com/plugin.php?id=dsu_paulsign:sign&infloat=1&operation=qiandao&inajax=1"
r=session.get(sign_url)
m = re.search('name="formhash" value="([^"]+)"', r.text)
formhash = m.group(1)
form = {
	'formhash': formhash,
        'qdxq':'ng',
        }
if '您今天已经签到过了或者签到时间还未开始' in r.text:
    print("You have already signed today.")
else:
    r = session.post(qiandao_url,data=form)
    print(r.text)

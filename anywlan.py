#!/usr/bin/python
#-*-coding:utf8-*-

import re
import requests
import time
import random
import commands
import sys
reload(sys)
sys.setdefaultencoding('gbk')

#sleeptime=random.randint(0,10)
#time.sleep(sleeptime)
#time.sleep(sleeptime*60)
print(commands.getoutput('date'))

header= {
	'Connection': 'keep-alive',   
 	'Accept-Language': 'zh-CN,zh;q=0.8',   
	'Accept': 'application/json, text/javascript, */*; q=0.01',   
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',  
	'Accept-Encoding': 'gzip, deflate, br',
	'Host':'account.oneplus.cn',    
	'X-Requested-With':'XMLHttpRequest',    
	'Origin': 'http://account.oneplus.cn',
	
	}
postdata = {
          'username':"username",
          'password':"password",#encrypted,use wireshark to get it
          'questionid':"0",
          'answer':"",
          'cookietime':"2592000",
           }

login_url="http://forum.anywlan.com/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=Lgh33&inajax=1"
session = requests.Session()
r=session.post(login_url,data=postdata)
print r.text.decode('gbk').encode('utf-8')
sign_url="http://www.anywlan.com/plugin.php?id=dsu_paulsign:sign"
r = session.get(sign_url)
m = re.search('name="formhash" value="([^"]+)"', r.text)
formhash = m.group(1)
#print(formhash)
qiandao_url ="http://www.anywlan.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&sign_as=1&infloat=1&inajax=1"
form = {'formhash': formhash,
        'qdxq':'kx',
        'qdmode':1,
        'todaysay':u'helloworld,你好世界'
        }
r = session.post(qiandao_url,data=form)
print r.text.decode('gbk').encode('utf-8')

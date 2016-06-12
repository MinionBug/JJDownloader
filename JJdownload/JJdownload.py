# -*- coding:utf-8 -*-

import cookielib
import urllib2, urllib
from bs4 import BeautifulSoup

filename= "cookie.txt"

cookies = cookielib.MozillaCookieJar()


def login():
    url="http://my.jjwxc.net/login.php?action=login&referer="
    postdata = urllib.urlencode({'loginname':'darkdancer0@gmail.com','loginpassword':'19880929a'})

    handler = urllib2.HTTPCookieProcessor(cookies)
    opener= urllib2.build_opener(handler)
    #如果要加head用addheader方法
    urllib2.install_opener(opener)
    opener.open(url,postdata) #.read().decode('gbk').encode('utf-8') #需要head重定向,需要utf-8转化
    cookies.save(filename,ignore_discard=True,ignore_expires=True)
    print cookies
    return opener

def midload():

    global opener

    mid = 'http://my.jjwxc.net/backend/logininfo.php'
    try:
        cookies.load(filename,ignore_discard=False,ignore_expires=False)
        handler = urllib2.HTTPCookieProcessor(cookies)
        opener = urllib2.build_opener(handler)
        print '1'
    except Exception:
        login()
        print '2'

    #开始构造BS
    midfile= opener.open(mid).read().decode('gbk') #.encode('utf-8')
    soup = BeautifulSoup(midfile, "lxml")
    content= soup.find('a',string='收藏列表')
    print content
    favlink = 'http://my.jjwxc.net/'+'%s' %content.get('href')
    print favlink
    return  favlink

def favload(url):
    favfile=opener.open(url).read().decode('gbk')
    soupF = BeautifulSoup(favfile, "lxml")
    print soupF


favlink=midload()
favload(favlink)

